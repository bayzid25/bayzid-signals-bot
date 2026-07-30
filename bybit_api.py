# =========================
# File Name: bybit_api.py
# =========================

import requests


BASE_URL = "https://api.bybit.com/v5/market/kline"


SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "XRPUSDT"
]


def get_market_data(symbol="BTCUSDT", interval="15"):

    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": interval,
        "limit": 200
    }


    try:

        response = requests.get(
    BASE_URL,
    params=params,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=10
        )
        )

        response.raise_for_status()

        data = response.json()


    except Exception as e:

        raise Exception(
            f"Bybit Connection Error: {e}"
        )



    if data.get("retCode") != 0:

        raise Exception(
            f"Bybit API Error: {data}"
        )


    candles = data["result"]["list"]


    if len(candles) < 50:

        raise Exception(
            "Not enough candle data"
        )



    closes = []
    volumes = []


    for candle in reversed(candles):

        closes.append(
            float(candle[4])
        )

        volumes.append(
            float(candle[5])
        )



    ema50 = calculate_ema(
        closes,
        50
    )


    ema200 = calculate_ema(
        closes,
        200
    )


    rsi = calculate_rsi(
        closes
    )


    macd = (
        calculate_ema(closes, 12)
        -
        calculate_ema(closes, 26)
    )


    signal = calculate_ema(
        closes,
        9
    )


    avg_volume = (
        sum(volumes[-20:])
        /
        20
    )


    return {

        "symbol": symbol,

        "ema50": ema50,

        "ema200": ema200,

        "rsi": rsi,

        "macd": macd,

        "signal": signal,

        "volume": volumes[-1],

        "avg_volume": avg_volume

    }



def calculate_ema(values, period):

    if len(values) < period:

        return sum(values) / len(values)


    multiplier = 2 / (period + 1)

    ema = values[0]


    for price in values[1:]:

        ema = (
            (price - ema)
            *
            multiplier
            +
            ema
        )


    return ema




def calculate_rsi(closes, period=14):

    gains = []
    losses = []


    for i in range(1, len(closes)):

        change = (
            closes[i]
            -
            closes[i-1]
        )


        if change >= 0:

            gains.append(change)
            losses.append(0)

        else:

            gains.append(0)
            losses.append(abs(change))



    avg_gain = (
        sum(gains[-period:])
        /
        period
    )


    avg_loss = (
        sum(losses[-period:])
        /
        period
    )


    if avg_loss == 0:

        return 100


    rs = avg_gain / avg_loss


    return (
        100 -
        (
            100 /
            (1 + rs)
        )
    )
