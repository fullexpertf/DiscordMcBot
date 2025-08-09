class BotError(Exception):
    """Base exception for the bot."""


class ConfigError(BotError):
    pass


__all__ = ["BotError", "ConfigError"]
