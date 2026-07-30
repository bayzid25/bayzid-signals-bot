import os
import threading
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
        text="🚀 Test Signal\n\n✅ Channel connection OK"
    )

    await update.message.reply_text(
        "✅ Test signal sent!"
    )


async def scan_market(app):

    while True:

        for symbol in SYMBOLS:

            try:
                data_15m = get_market_data(
                    symbol,
                    "15m"
                )

                data_1h = get_market_data(
                    symbol,
                    "1h"
                )


                result = calculate_signal(
                    data_15m,
                    data_1h
                )


                if result["signal"] != "NO SIGNAL":

                    message = f"""
🚀 Crypto Futures Signal

📌 Pair: {symbol}

📈 Direction: {result['signal']}

⭐ Score: {result['score']}/8

📝 Reason:
{', '.join(result['reasons'])}

⚠️ Manage Risk Properly
"""

                    await app.bot.send_message(
                        chat_id=CHANNEL_ID,
                        text=message
                    )


            except Exception as e:
                print(e)


        time.sleep(900)



def main():

    threading.Thread(
        target=run_web_server,
        daemon=True
    ).start()


    app = Application.builder().token(TOKEN).build()


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
