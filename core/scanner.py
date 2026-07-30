from config import (
    SYMBOLS,
    LOWER_TIMEFRAME,
    HIGHER_TIMEFRAME
)

from core.binance_api import BinanceAPI
from core.indicators import Indicators
from core.strategy import Strategy
from core.telegram_sender import TelegramSender
from utils.helpers import can_send_signal


class Scanner:

    def __init__(self):

        self.telegram = TelegramSender()

    async def scan_market(self):

        for symbol in SYMBOLS:

            try:

                df15 = BinanceAPI.get_klines(
                    symbol,
                    LOWER_TIMEFRAME
                )

                df1h = BinanceAPI.get_klines(
                    symbol,
                    HIGHER_TIMEFRAME
                )

                if df15 is None or df1h is None:
                    continue

                df15 = Indicators.add_indicators(df15)
                df1h = Indicators.add_indicators(df1h)

                signal = Strategy.generate_signal(
                    df15,
                    df1h,
                    symbol
                )

                if signal is None:
                    continue

                if not can_send_signal(
                    signal["symbol"],
                    signal["side"]
                ):
                    continue

                await self.telegram.send_signal(signal)

            except Exception as e:

                print(f"{symbol} Scanner Error : {e}")
