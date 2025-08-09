from __future__ import annotations

from discord.ext import commands


class Moderation(commands.Cog):
    """Moderation related commands (placeholder)."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Moderation(bot))
