import asyncio
import logging

from utils.logger import setup_logger
from core.scanner import Scanner

logger = setup_logger()


async def run_bot():

    logger.info("===================================")
    logger.info(" Binance Futures Signal Bot Started ")
    logger.info("===================================")

    scanner = Scanner()

    while True:

        try:

            await scanner.scan_market()

        except Exception as e:

            logger.exception(f"Scanner Error: {e}")

        await asyncio.sleep(900)


if __name__ == "__main__":
    asyncio.run(run_bot())
