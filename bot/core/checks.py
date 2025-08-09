from __future__ import annotations

import os

from discord import app_commands


async def is_owner(interaction: app_commands.Interaction) -> bool:
    owner_id = int(os.getenv("BOT_OWNER", "0"))
    return interaction.user.id == owner_id


owner_only = app_commands.check(is_owner)

__all__ = ["owner_only"]
