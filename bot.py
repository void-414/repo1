from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace this with your token
TOKEN = "7024375117:AAECTpwnoqAbIp4xUT1bZstiSVgBXgSLMh0"

# Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your simple bot. How can I help you?")

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()
