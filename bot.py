from telegram import *
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6577485256:AAE3rDnfLWPecsRJXbYJd8BX-UGzgJ5Gy0A").build()

app.add_handler(CommandHandler("start", hello))

app.run_polling()