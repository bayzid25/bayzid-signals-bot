# =========================
# File Name: strategy.py
# =========================


def calculate_signal(data_15m, data_1h):


    score = 0

    reasons = []


    trend = "NONE"



    # -------------------------
    # 1H Trend Confirmation
    # -------------------------

    if data_1h["ema50"] > data_1h["ema200"]:

        trend = "LONG"

        score += 2

        reasons.append(
            "1H Trend Bullish"
        )


    elif data_1h["ema50"] < data_1h["ema200"]:

        trend = "SHORT"

        score += 2

        reasons.append(
            "1H Trend Bearish"
        )



    # -------------------------
    # 15M Entry Confirmation
    # -------------------------

    if trend == "LONG":


        if data_15m["ema50"] > data_15m["ema200"]:

            score += 2

            reasons.append(
                "15M EMA Confirmed"
            )



    elif trend == "SHORT":


        if data_15m["ema50"] < data_15m["ema200"]:

            score += 2

            reasons.append(
                "15M EMA Confirmed"
            )



    # -------------------------
    # RSI Filter
    # -------------------------

    if 35 <= data_15m["rsi"] <= 65:

        score += 1

        reasons.append(
            "RSI Healthy"
        )



    # -------------------------
    # MACD Confirmation
    # -------------------------

    if trend == "LONG":


        if data_15m["macd"] > data_15m["signal"]:

            score += 2

            reasons.append(
                "MACD Bullish"
            )



    elif trend == "SHORT":


        if data_15m["macd"] < data_15m["signal"]:

            score += 2

            reasons.append(
                "MACD Bearish"
            )



    # -------------------------
    # Volume Confirmation
    # -------------------------

    if data_15m["volume"] > data_15m["avg_volume"]:

        score += 1

        reasons.append(
            "Volume Confirmed"
        )



    # -------------------------
    # Final Result
    # -------------------------

    if score >= 7 and trend != "NONE":


        return {

            "signal": trend,

            "score": score,

            "reasons": reasons

        }



    return {

        "signal": "NO SIGNAL",

        "score": score,

        "reasons": reasons

    }
