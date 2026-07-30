import asyncio

from utils.logger import setup_logger
from core.scanner import Scanner
from config import SCAN_INTERVAL

logger = setup_logger()


async def main():

    logger.info("====================================")
    logger.info(" Binance Futures Signal Bot Started ")
    logger.info("====================================")

    scanner = Scanner()

    while True:

        try:
            await scanner.scan_market()

        except Exception as e:
            logger.exception(f"Scanner Error: {e}")

        await asyncio.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())
