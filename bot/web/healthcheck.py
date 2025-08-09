from __future__ import annotations

import asyncio
import os
from aiohttp import web
from datetime import datetime

start_time = datetime.utcnow()


async def start_web_app(bot) -> None:
    app = web.Application()

    async def healthz(request: web.Request) -> web.Response:
        return web.json_response({"status": "ok"})

    async def metrics(request: web.Request) -> web.Response:
        uptime = (datetime.utcnow() - start_time).total_seconds()
        guilds = len(bot.guilds) if bot else 0
        users = sum(g.member_count or 0 for g in bot.guilds) if bot else 0
        return web.json_response({"uptime": uptime, "guilds": guilds, "users": users})

    app.router.add_get("/healthz", healthz)
    app.router.add_get("/metrics", metrics)

    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", "8080"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    bot.web_runner = runner  # type: ignore

async def stop_web_app(bot) -> None:
    runner = getattr(bot, "web_runner", None)
    if runner:
        await runner.cleanup()

__all__ = ["start_web_app", "stop_web_app"]
