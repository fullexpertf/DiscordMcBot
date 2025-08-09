from __future__ import annotations

from discord.ext import commands


class ReactionRoles(commands.Cog):
    """Reaction role management (placeholder)."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReactionRoles(bot))
