        )
    )
# =========================
# File Name: binance_api.py
# =========================

import requests


BASE_URL = "https://fapi.binance.com/fapi/v1/klines"


# =========================
# Get Market Data
# =========================

def get_market_data(
    symbol="BTCUSDT",
    interval="15m",
    limit=200
):

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }


    try:

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=15
        )


        response.raise_for_status()


        candles = response.json()



    except Exception as e:

        raise Exception(
            f"Binance Connection Error: {e}"
        )



    # Binance Error Check

    if not isinstance(candles, list):

        raise Exception(
            f"Binance API Error: {candles}"
        )



    if len(candles) < 50:

        raise Exception(
            "Not enough candle data"
        )



    closes = []
    volumes = []



    for candle in candles:


        closes.append(
            float(candle[4])
        )


        volumes.append(
            float(candle[5])
        )



    return {

        "ema50":
            calculate_ema(
                closes,
                50
            ),


        "ema200":
            calculate_ema(
                closes,
                200
            ),


        "rsi":
            calculate_rsi(
                closes
            ),


        "macd":
            (
                calculate_ema(
                    closes,
                    12
                )
                -
                calculate_ema(
                    closes,
                    26
                )
            ),


        "signal":
            calculate_ema(
                closes,
                9
            ),


        "volume":
            volumes[-1],


        "avg_volume":
            (
                sum(volumes[-20:])
                /
                20
            )

    }



# =========================
# EMA
# =========================

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



# =========================
# RSI
# =========================

def calculate_rsi(
    closes,
    period=14
):


    gains = []
    losses = []


    for i in range(1,len(closes)):


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
