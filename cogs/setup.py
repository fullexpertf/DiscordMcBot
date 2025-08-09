import json
from pathlib import Path

import discord
from discord.ext import commands


CONFIG_PATH = Path("config.json")


class Setup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = self._load_config()

    def _load_config(self) -> dict:
        if CONFIG_PATH.exists():
            with CONFIG_PATH.open(encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save_config(self) -> None:
        with CONFIG_PATH.open("w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    @commands.hybrid_command()
    @commands.has_permissions(administrator=True)
    async def setup(
        self,
        ctx: commands.Context,
        welcome_channel: discord.TextChannel,
        log_channel: discord.TextChannel,
        level_up_channel: discord.TextChannel,
    ) -> None:
        """Sunucu kanallarını yapılandırır."""

        await ctx.defer()
        self.config["welcome_channel_id"] = welcome_channel.id
        self.config["log_channel_id"] = log_channel.id
        self.config["level_up_channel_id"] = level_up_channel.id
        self._save_config()
        await ctx.send("Kanallar kaydedildi.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Setup(bot))

