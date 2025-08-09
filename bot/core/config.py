from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel


class Modules(BaseModel):
    leveling: bool = True
    economy: bool = True
    automod: bool = True


class Config(BaseModel):
    message_content: bool = False
    locale: str = "en"
    database_url: str = "sqlite+aiosqlite:///bot.db"
    economy_currency: str = "₺"
    modules: Modules = Modules()
    test_guild_id: Optional[int] = None


def load_config(path: str | Path) -> Config:
    data = {}
    p = Path(path)
    if p.exists():
        with p.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    return Config(**data)

__all__ = ["Config", "load_config"]
