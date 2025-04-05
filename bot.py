from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

# Create Flask app
app = Flask(__name__)

# Get token from environment variable or paste directly
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7024375117:AAECTpwnoqAbIp4xUT1bZstiSVgBXgSLMh0")

# Create Telegram app instance
telegram_app = Application.builder().token(BOT_TOKEN).build()


# Bot command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your Reminder Bot! ⏰ Send /remind <text> to get started.")


# Bot command: /remind
async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reminder_text = " ".join(context.args)
    if reminder_text:
        await update.message.reply_text(f"✅ Reminder set: {reminder_text}")
        # (Real logic like storing and triggering reminder would go here)
    else:
        await update.message.reply_text("❗ Usage: /remind <what to remind>")


# Add handlers
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("remind", remind))


# Flask route to handle webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    telegram_app.update_queue.put(update)
    return "ok"


# Set webhook when the app starts
@app.before_first_request
def set_webhook():
    url = os.environ.get("WEBHOOK_URL", "https://labour-karrah-voidx-ae980523.koyeb.app/webhook")
    telegram_app.bot.delete_webhook()
    telegram_app.bot.set_webhook(url)


# Run Flask app on port 8080
if __name__ == "__main__":
    app.run(port=8080)
