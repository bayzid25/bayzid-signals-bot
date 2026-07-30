import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Coins
SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT"
]

# Timeframes
LOWER_TIMEFRAME = "15m"
HIGHER_TIMEFRAME = "1h"

# Binance
KLINE_LIMIT = 300

# Indicator Settings
EMA_FAST = 20
EMA_MID = 50
EMA_SLOW = 200

RSI_PERIOD = 14
RSI_BUY = 55
RSI_SELL = 45

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

ATR_PERIOD = 14
ATR_MULTIPLIER = 1.5

VOLUME_MA = 20

# Scanner
SCAN_INTERVAL = 900  # 15 Minutes

# Signal
COOLDOWN_MINUTES = 120

# Risk Management
RISK_REWARD_1 = 2
RISK_REWARD_2 = 3
RISK_REWARD_3 = 4

# Logging
LOG_LEVEL = "INFO"
