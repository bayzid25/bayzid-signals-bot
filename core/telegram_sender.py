from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID


class TelegramSender:

    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)

    async def send_signal(self, signal):

        message = f"""
🚀 <b>{signal['side']} SIGNAL</b>

💰 <b>Coin:</b> {signal['symbol']}

📊 <b>Entry:</b> <code>{signal['entry']}</code>

🛑 <b>Stop Loss:</b> <code>{signal['stop']}</code>

🎯 <b>Take Profit 1:</b> <code>{signal['tp1']}</code>
🎯 <b>Take Profit 2:</b> <code>{signal['tp2']}</code>
🎯 <b>Take Profit 3:</b> <code>{signal['tp3']}</code>

⏰ <b>Timeframes:</b> 15M + 1H

⚠️ <b>Risk Management Recommended</b>
"""

        await self.bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode="HTML"
        )
