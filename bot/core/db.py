from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import Config

Base = declarative_base()


class GuildConfig(Base):
    __tablename__ = "guild_configs"

    id = Column(Integer, primary_key=True)
    language = Column(String, default="en")
    prefixes = Column(String, nullable=True)
    welcome_channel_id = Column(Integer, nullable=True)
    goodbye_channel_id = Column(Integer, nullable=True)
    autorole_id = Column(Integer, nullable=True)
    starboard_channel_id = Column(Integer, nullable=True)
    star_threshold = Column(Integer, default=5)
    xp_enabled = Column(Boolean, default=True)
    xp_rate = Column(Integer, default=1)
    economy_currency = Column(String, default="₺")
    muted_role_id = Column(Integer, nullable=True)
    automod_badwords = Column(Text, nullable=True)
    automod_caps_threshold = Column(Integer, default=0)
    automod_links = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserProfile(Base):
    __tablename__ = "user_profiles"
    user_id = Column(Integer, primary_key=True)
    guild_id = Column(Integer, primary_key=True)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=0)
    reputation = Column(Integer, default=0)
    wallet = Column(Integer, default=0)
    bank = Column(Integer, default=0)
    last_message_at = Column(DateTime, nullable=True)


class Infraction(Base):
    __tablename__ = "infractions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    guild_id = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    reason = Column(Text, nullable=True)
    moderator_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    guild_id = Column(Integer, nullable=False)
    opener_id = Column(Integer, nullable=False)
    channel_id = Column(Integer, nullable=False)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
    closed_at = Column(DateTime, nullable=True)


class ReactionRole(Base):
    __tablename__ = "reaction_roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    guild_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    emoji = Column(String, nullable=False)
    role_id = Column(Integer, nullable=False)


async def create_engine(config: Config) -> AsyncEngine:
    return create_async_engine(config.database_url, echo=False, future=True)


def create_sessionmaker(engine: AsyncEngine) -> sessionmaker[AsyncSession]:
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


__all__ = [
    "Base",
    "GuildConfig",
    "UserProfile",
    "Infraction",
    "Ticket",
    "ReactionRole",
    "create_engine",
    "create_sessionmaker",
]
