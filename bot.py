from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("7024375117:AAECTpwnoqAbIp4xUT1bZstiSVgBXgSLMh0")
WEBHOOK_PATH = "/webhook"

app = Flask(__name__)
bot_app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your reminder bot.")

bot_app.add_handler(CommandHandler("start", start))

@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put(update)
    return "ok"

if __name__ == "__main__":
    bot_app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=os.getenv("https://labour-karrah-voidx-ae980523.koyeb.app/webhook") + WEBHOOK_PATH
    )
