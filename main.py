import os
import threading
import asyncio
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from binance_api import get_market_data
from strategy import calculate_signal


TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@bayzidsignals"

SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT"
]

last_signals = {}


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    print(f"Web server running on port {port}")
    server.serve_forever()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Crypto Futures Signal Bot Running!"
    )


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=(
            "🚀 Crypto Futures Signal Test\n\n"
            "📌 Pair: BTC/USDT\n"
            "📈 Direction: LONG\n"
            "✅ Bot connected successfully!"
        )
    )

    await update.message.reply_text(
        "✅ Test signal sent!"
    )


async def scan_market(app):

    while True:

        for symbol in SYMBOLS:

            try:
                data_15m = get_market_data(symbol, "15m")
                data_1h = get_market_data(symbol, "1h")

                result = calculate_signal(
                    data_15m,
                    data_1h
                )

                signal_key = f"{symbol}_{result['signal']}"

                if (
                    result["signal"] != "NO SIGNAL"
                    and last_signals.get(symbol) != signal_key
                ):

                    message = f"""
🚀 Crypto Futures Signal

📌 Pair: {symbol}

📈 Direction: {result['signal']}

⭐ Confidence Score:
{result['score']}/8

📝 Confirmation:
{', '.join(result['reasons'])}

⚠️ Use Proper Risk Management
"""

                    await app.bot.send_message(
                        chat_id=CHANNEL_ID,
                        text=message
                    )

                    last_signals[symbol] = signal_key


            except Exception as e:
                print("Scanner Error:", e)


        await asyncio.sleep(900)


async def after_start(app):

    asyncio.create_task(
        scan_market(app)
    )


def main():

    threading.Thread(
        target=run_web_server,
        daemon=True
    ).start()


    app = (
        Application.builder()
        .token(TOKEN)
        .post_init(after_start)
        .build()
    )


    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("test", test)
    )


    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
