import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


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
    await update.message.reply_text("✅ Telegram Signal Bot is Running!")


def main():
    threading.Thread(target=run_web_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
