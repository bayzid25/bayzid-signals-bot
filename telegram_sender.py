from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID


class TelegramSender:

    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)

    async def send_signal(self, signal):

        message = f"""
🚨 <b>{signal['side']} SIGNAL</b>

💰 Coin : <b>{signal['symbol']}</b>

📍 Entry : <code>{signal['entry']}</code>

🛑 Stop Loss : <code>{signal['stop']}</code>

🎯 Take Profit 1 : <code>{signal['tp1']}</code>
🎯 Take Profit 2 : <code>{signal['tp2']}</code>
🎯 Take Profit 3 : <code>{signal['tp3']}</code>

⏰ Timeframe : 15M + 1H

⚠️ Trade with proper risk management.
"""

        await self.bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode="HTML"
        )
