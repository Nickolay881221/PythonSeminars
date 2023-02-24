import game
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from game import *
import emoji

app = ApplicationBuilder().token("6219488423:AAGmXrfxMx1wIyamayMTpKXbMMULR_lkO_E").build()

app.add_handler(CommandHandler("hi", play_command))

""" playData = [1,2,3,4,5,6,7,8,9]
game.playground(playData)
while game.winner(playData):
    for i in range(1,10):
        if i % 2 != 0:
            game.checkPlaygroud(playData, game.playerstep())
            game.playground(playData)
            if game.winner(playData) == False:
                break
        else:
            game.AIstep(playData)
            game.playground(playData)
            if game.winner(playData) == False:
                break """
