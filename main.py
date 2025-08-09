import asyncio
import os
from dotenv import load_dotenv

from bot.core.config import load_config
from bot.core.bot import DiscordBot
from bot.core.logger import setup_logging
from bot.web.healthcheck import start_web_app

async def main() -> None:
    load_dotenv()
    config = load_config("config.yaml")
    setup_logging()
    bot = DiscordBot(config)
    await start_web_app(bot)
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set")
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
