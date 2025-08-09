from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands

from ..core.checks import owner_only


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(description="Reload a cog")
    @owner_only
    async def reload(self, interaction: discord.Interaction, cog: str) -> None:
        try:
            await self.bot.reload_extension(f"bot.cogs.{cog}")
        except Exception as e:
            await interaction.response.send_message(f"Failed to reload: {e}", ephemeral=True)
        else:
            await interaction.response.send_message("Reloaded.", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))
