import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===========================
# Telegram Settings
# ===========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# ===========================
# Binance Futures Settings
# ===========================

SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT"
]

# ===========================
# Timeframes
# ===========================

TREND_TIMEFRAME = "1h"
ENTRY_TIMEFRAME = "15m"

# ===========================
# EMA Settings
# ===========================

EMA_FAST = 20
EMA_MIDDLE = 50
EMA_SLOW = 200

# ===========================
# RSI Settings
# ===========================

RSI_LENGTH = 14
RSI_BUY = 55
RSI_SELL = 45

# ===========================
# MACD Settings
# ===========================

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# ===========================
# ATR Settings
# ===========================

ATR_LENGTH = 14
ATR_MULTIPLIER = 1.5

# ===========================
# Risk Management
# ===========================

RISK_REWARD = 2.0

# ===========================
# Scanner
# ===========================

CHECK_INTERVAL = 900

# ===========================
# Signal Protection
# ===========================

MAX_SIGNALS_PER_DAY = 10
COOLDOWN_MINUTES = 120

# ===========================
# Volume Filter
# ===========================

VOLUME_PERIOD = 20
VOLUME_MULTIPLIER = 1.2

# ===========================
# Logging
# ===========================

LOG_LEVEL = "INFO"
