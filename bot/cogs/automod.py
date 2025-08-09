from __future__ import annotations

from discord.ext import commands


class AutoMod(commands.Cog):
    """Automatic moderation features (placeholder)."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AutoMod(bot))
