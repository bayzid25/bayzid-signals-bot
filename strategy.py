from config import *

class Strategy:

    @staticmethod
    def generate_signal(df15, df1h, symbol):

        last15 = df15.iloc[-1]
        last1h = df1h.iloc[-1]

        # ==========================
        # 1H Trend Filter
        # ==========================
        bullish_trend = (
            last1h["ema50"] > last1h["ema200"]
        )

        bearish_trend = (
            last1h["ema50"] < last1h["ema200"]
        )

        # ==========================
        # Long Conditions
        # ==========================
        long_signal = (
            bullish_trend
            and last15["ema20"] > last15["ema50"]
            and last15["rsi"] > RSI_BUY
            and last15["macd"] > last15["macd_signal"]
            and last15["volume"] > last15["volume_ma20"]
        )

        # ==========================
        # Short Conditions
        # ==========================
        short_signal = (
            bearish_trend
            and last15["ema20"] < last15["ema50"]
            and last15["rsi"] < RSI_SELL
            and last15["macd"] < last15["macd_signal"]
            and last15["volume"] > last15["volume_ma20"]
        )

        # ==========================
        # LONG
        # ==========================
        if long_signal:

            entry = round(last15["close"], 2)

            stop = round(
                entry - (last15["atr"] * ATR_MULTIPLIER),
                2
            )

            tp1 = round(
                entry + ((entry - stop) * 2),
                2
            )

            tp2 = round(
                entry + ((entry - stop) * 3),
                2
            )

            tp3 = round(
                entry + ((entry - stop) * 4),
                2
            )

            return {
                "side": "LONG",
                "symbol": symbol,
                "entry": entry,
                "stop": stop,
                "tp1": tp1,
                "tp2": tp2,
                "tp3": tp3
            }

        # ==========================
        # SHORT
        # ==========================
        if short_signal:

            entry = round(last15["close"], 2)

            stop = round(
                entry + (last15["atr"] * ATR_MULTIPLIER),
                2
            )

            tp1 = round(
                entry - ((stop - entry) * 2),
                2
            )

            tp2 = round(
                entry - ((stop - entry) * 3),
                2
            )

            tp3 = round(
                entry - ((stop - entry) * 4),
                2
            )

            return {
                "side": "SHORT",
                "symbol": symbol,
                "entry": entry,
                "stop": stop,
                "tp1": tp1,
                "tp2": tp2,
                "tp3": tp3
            }

        return None
