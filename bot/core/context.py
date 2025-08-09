from __future__ import annotations

from typing import Any

from discord.ext import commands


class BotContext(commands.Context):
    bot: "DiscordBot"  # type: ignore


__all__ = ["BotContext"]
