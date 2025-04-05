import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "7024375117:AAECTpwnoqAbIp4xUT1bZstiSVgBXgSLMh0"

async def remind_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Get delay and message
        delay = int(context.args[0])
        reminder_text = " ".join(context.args[1:])

        # Confirm to user
        await update.message.reply_text(f"✅ Got it! I'll remind you in {delay} minutes.")

        # Wait the specified time (in seconds)
        await asyncio.sleep(delay * 60)

        # Send the reminder
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⏰ Reminder: {reminder_text}")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /remind <minutes> <message>")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("remind", remind_command))
    app.run_polling()
