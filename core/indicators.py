import ta


class Indicators:

    @staticmethod
    def add_indicators(df):

        # EMA
        df["ema20"] = ta.trend.ema_indicator(
            close=df["close"],
            window=20
        )

        df["ema50"] = ta.trend.ema_indicator(
            close=df["close"],
            window=50
        )

        df["ema200"] = ta.trend.ema_indicator(
            close=df["close"],
            window=200
        )

        # RSI
        df["rsi"] = ta.momentum.RSIIndicator(
            close=df["close"],
            window=14
        ).rsi()

        # MACD
        macd = ta.trend.MACD(
            close=df["close"]
        )

        df["macd"] = macd.macd()
        df["macd_signal"] = macd.macd_signal()
        df["macd_hist"] = macd.macd_diff()

        # ATR
        atr = ta.volatility.AverageTrueRange(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            window=14
        )

        df["atr"] = atr.average_true_range()

        # Volume MA
        df["volume_ma20"] = (
            df["volume"]
            .rolling(20)
            .mean()
        )

        return df
