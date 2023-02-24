from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from command import *
from game import *
import emoji

app = ApplicationBuilder().token("6219488423:AAGmXrfxMx1wIyamayMTpKXbMMULR_lkO_E").build()


app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("play", play_command))
print(emoji.emojize(f'Привет :thumbs_up:'))
app.run_polling()
