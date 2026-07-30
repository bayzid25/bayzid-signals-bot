import requests


BASE_URL = "https://api.binance.com/api/v3/klines"


def get_market_data(symbol="BTCUSDT", interval="1h", limit=200):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(BASE_URL, params=params)
    candles = response.json()

    closes = []
    volumes = []

    for candle in candles:
        closes.append(float(candle[4]))
        volumes.append(float(candle[5]))

    return {
        "symbol": symbol,
        "closes": closes,
        "volumes": volumes
    }
