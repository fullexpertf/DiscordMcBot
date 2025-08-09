from loguru import logger
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def setup_logging() -> None:
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level="INFO")
    logger.add(LOG_DIR / "bot.log", rotation="1 MB", retention=5, level="INFO")
    logger.add(LOG_DIR / "errors.log", rotation="1 MB", retention=5, level="ERROR")

__all__ = ["logger", "setup_logging"]
