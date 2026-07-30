import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@bayzidsignals"


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
        "✅ Telegram Signal Bot is Running!"
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
        "✅ Test signal sent to channel!"
    )


def main():
    threading.Thread(
        target=run_web_server,
        daemon=True
    ).start()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
