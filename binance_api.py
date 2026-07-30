from binance.client import Client
import pandas as pd
import logging

# Public client (API Key ছাড়াও মার্কেট ডেটা পড়া যায়)
client = Client()

logger = logging.getLogger(__name__)


class BinanceAPI:

    @staticmethod
    def get_klines(symbol: str, interval: str, limit: int = 300):
        """
        Fetch futures candlestick data
        """

        try:

            klines = client.futures_klines(
                symbol=symbol,
                interval=interval,
                limit=limit
            )

            df = pd.DataFrame(klines, columns=[
                "open_time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_asset_volume",
                "number_of_trades",
                "taker_buy_base",
                "taker_buy_quote",
                "ignore"
            ])

            numeric_columns = [
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]

            for col in numeric_columns:
                df[col] = df[col].astype(float)

            df["open_time"] = pd.to_datetime(
                df["open_time"],
                unit="ms"
            )

            df["close_time"] = pd.to_datetime(
                df["close_time"],
                unit="ms"
            )

            return df

        except Exception as e:

            logger.error(f"{symbol} {interval} : {e}")

            return None
