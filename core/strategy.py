from core.risk_manager import RiskManager


class Strategy:

    @staticmethod
    def generate_signal(df15, df1h, symbol):

        last15 = df15.iloc[-1]
        last1h = df1h.iloc[-1]

        bullish_trend = (
            last1h["ema50"] > last1h["ema200"]
        )

        bearish_trend = (
            last1h["ema50"] < last1h["ema200"]
        )

        long_signal = (
            bullish_trend
            and last15["ema20"] > last15["ema50"]
            and last15["rsi"] > 55
            and last15["macd"] > last15["macd_signal"]
            and last15["volume"] > last15["volume_ma20"]
        )

        short_signal = (
            bearish_trend
            and last15["ema20"] < last15["ema50"]
            and last15["rsi"] < 45
            and last15["macd"] < last15["macd_signal"]
            and last15["volume"] > last15["volume_ma20"]
        )

        if long_signal:

            trade = RiskManager.calculate_long(
                entry=last15["close"],
                atr=last15["atr"]
            )

            return {
                "side": "LONG",
                "symbol": symbol,
                **trade
            }

        if short_signal:

            trade = RiskManager.calculate_short(
                entry=last15["close"],
                atr=last15["atr"]
            )

            return {
                "side": "SHORT",
                "symbol": symbol,
                **trade
            }

        return None
