from __future__ import annotations

from discord.ext import commands


class Starboard(commands.Cog):
    """Starboard feature (placeholder)."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Starboard(bot))
