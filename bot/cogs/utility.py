from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands


class Utility(commands.Cog):
    """General utility commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction) -> None:
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! {latency}ms")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Utility(bot))
