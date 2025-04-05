import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running.'

def run_web():
    app.run(host='0.0.0.0', port=8080)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot.")

if __name__ == '__main__':
    threading.Thread(target=run_web).start()
    app = ApplicationBuilder().token("7024375117:AAECTpwnoqAbIp4xUT1bZstiSVgBXgSLMh0").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
