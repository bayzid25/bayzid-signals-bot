import logging
import os

from config import LOG_LEVEL


def setup_logger():

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("SignalBot")
    logger.setLevel(getattr(logging, LOG_LEVEL))

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        "logs/bot.log",
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
