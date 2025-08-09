from __future__ import annotations

from discord.ext import commands


class AutoRole(commands.Cog):
    """Automatic role assignment (placeholder)."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AutoRole(bot))
