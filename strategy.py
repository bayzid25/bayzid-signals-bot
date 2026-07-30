def generate_signal(data):
    score = 0
    reasons = []

    # Trend Check
    if data["ema50"] > data["ema200"]:
        score += 2
        reasons.append("EMA Trend Bullish")

    elif data["ema50"] < data["ema200"]:
        score += 2
        reasons.append("EMA Trend Bearish")


    # RSI Check
    if data["rsi"] < 35:
        score += 1
        reasons.append("RSI Oversold")

    elif data["rsi"] > 65:
        score += 1
        reasons.append("RSI Overbought")


    # MACD Check
    if data["macd"] > data["signal"]:
        score += 2
        reasons.append("MACD Positive")

    else:
        score += 2
        reasons.append("MACD Negative")


    # Volume Check
    if data["volume"] > data["avg_volume"]:
        score += 1
        reasons.append("High Volume")


    # Final Decision
    if score >= 7:
        if data["ema50"] > data["ema200"]:
            return {
                "signal": "LONG",
                "score": score,
                "reasons": reasons
            }
        else:
            return {
                "signal": "SHORT",
                "score": score,
                "reasons": reasons
            }

    return {
        "signal": "NO SIGNAL",
        "score": score,
        "reasons": reasons
    }
