import logging

from app.config import settings


def get_logger(name: str) -> logging.Logger:
    """Create a configured logger."""
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)

    logger.setLevel(log_level)

    handler = logging.StreamHandler()
    handler.setLevel(log_level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
