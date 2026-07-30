import requests


BASE_URL = "https://api.binance.com/api/v3/klines"


def get_market_data(symbol="BTCUSDT", interval="15m", limit=200):

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

    ema50 = sum(closes[-50:]) / 50
    ema200 = sum(closes[-200:]) / 200

    avg_volume = sum(volumes[-20:]) / 20
    current_volume = volumes[-1]

    rsi = calculate_rsi(closes)

    macd = ema(closes, 12) - ema(closes, 26)
    signal = ema(closes, 9)

    return {
        "ema50": ema50,
        "ema200": ema200,
        "rsi": rsi,
        "macd": macd,
        "signal": signal,
        "volume": current_volume,
        "avg_volume": avg_volume
    }


def ema(values, period):
    if len(values) < period:
        return sum(values) / len(values)

    return sum(values[-period:]) / period


def calculate_rsi(closes, period=14):

    gains = []
    losses = []

    for i in range(1, len(closes)):
        change = closes[i] - closes[i-1]

        if change >= 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))
