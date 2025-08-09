from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path

import discord
from discord.ext import commands

from .config import Config
from .logger import logger
from .scheduler import start_scheduler, shutdown_scheduler


class DiscordBot(commands.Bot):
    def __init__(self, config: Config) -> None:
        intents = discord.Intents.default()
        intents.members = True
        if config.message_content:
            intents.message_content = True
        super().__init__(command_prefix=None, intents=intents)
        self.config = config

    async def setup_hook(self) -> None:
        start_scheduler()
        await self.load_cogs()
        if self.config.test_guild_id:
            guild = discord.Object(self.config.test_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            logger.info("Synced commands to test guild {guild}", guild=self.config.test_guild_id)
        else:
            await self.tree.sync()
            logger.info("Synced global commands")

    async def load_cogs(self) -> None:
        base = Path(__file__).parent.parent / "cogs"
        for module in pkgutil.iter_modules([str(base)]):
            if module.ispkg:
                continue
            name = f"bot.cogs.{module.name}"
            try:
                await self.load_extension(name)
                logger.info("Loaded cog {name}", name=name)
            except Exception as e:  # pragma: no cover - log
                logger.exception("Failed to load cog {name}: {e}", name=name, e=e)

    async def on_ready(self) -> None:
        logger.info("Logged in as {0} ({0.id})".format(self.user))

    async def close(self) -> None:
        shutdown_scheduler()
        await super().close()

__all__ = ["DiscordBot"]
