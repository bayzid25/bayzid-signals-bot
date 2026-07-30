# =========================
# File Name: okx_api.py
# =========================

import requests


BASE_URL = "https://www.okx.com/api/v5/market/candles"


SYMBOLS = [
    "BTC-USDT-SWAP",
    "ETH-USDT-SWAP",
    "SOL-USDT-SWAP",
    "XRP-USDT-SWAP"
]


def get_market_data(symbol="BTC-USDT-SWAP", interval="15m", limit=200):

    params = {
        "instId": symbol,
        "bar": interval,
        "limit": limit
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

        response.raise_for_status()

        data = response.json()

    except Exception as e:
        raise Exception(
            f"OKX Connection Error: {e}"
        )


    if data.get("code") != "0":

        raise Exception(
            f"OKX API Error: {data}"
        )


    candles = data["data"]


    closes = []
    volumes = []


    for candle in reversed(candles):

        closes.append(
            float(candle[4])
        )

        volumes.append(
            float(candle[5])
        )


    if len(closes) < 50:
        raise Exception(
            "Not enough candle data"
        )


    return {

        "close": closes[-1],

        "closes": closes,

        "volume": volumes[-1],

        "avg_volume": sum(volumes[-20:]) / 20

    }
