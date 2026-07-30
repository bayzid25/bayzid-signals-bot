# =========================
# File Name: main.py
# =========================

import os
import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from binance_api import get_market_data
from strategy import calculate_signal


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID", "@bayzidsignals")


SYMBOL = "BTCUSDT"


# -------------------------
# Render Health Check
# -------------------------

class HealthCheckHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")


def run_server():

    port = int(os.environ.get("PORT", 10000))

    server = HTTPServer(
        ("0.0.0.0", port),
        HealthCheckHandler
    )

    print(f"Web server running on port {port}")

    server.serve_forever()



# -------------------------
# Telegram Commands
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ Bayzid Signal Bot is Running!"
    )



async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=(
            "🚀 Test Signal\n\n"
            "📌 Pair: BTC/USDT\n"
            "📈 Direction: LONG\n"
            "✅ Channel Connected"
        )
    )

    await update.message.reply_text(
        "✅ Test signal sent!"
    )



# -------------------------
# Scanner
# -------------------------

async def scan_market(application):

    while True:

        try:

            data_15m = get_market_data(
                SYMBOL,
                "15m"
            )

            data_1h = get_market_data(
                SYMBOL,
                "1h"
            )


            result = calculate_signal(
                data_15m,
                data_1h
            )


            if result["signal"] != "NO SIGNAL":

                message = (
                    "🚀 Crypto Futures Signal\n\n"
                    f"📌 Pair: {SYMBOL}\n"
                    f"📈 Direction: {result['signal']}\n"
                    f"⭐ Score: {result['score']}\n\n"
                    "Reasons:\n"
                )

                for r in result["reasons"]:
                    message += f"✅ {r}\n"


                await application.bot.send_message(
                    chat_id=CHANNEL_ID,
                    text=message
                )


            print(
                "Scanner running:",
                result
            )


        except Exception as e:

            print(
                "Scanner Error:",
                type(e).__name__,
                str(e)
            )


        await asyncio.sleep(60)



# -------------------------
# Main Function
# -------------------------

async def main():

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        CommandHandler(
            "test",
            test
        )
    )


    asyncio.create_task(
        scan_market(app)
    )


    print("Bot Started...")


    await app.run_polling()



if __name__ == "__main__":

    threading.Thread(
        target=run_server,
        daemon=True
    ).start()


    asyncio.run(
        main()
    )
