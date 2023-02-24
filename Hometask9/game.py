""" Написать программу для игру в крестики-нолики в формате: человек-компьютер """
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from game import *
import emoji

""" функция печати игрового поля по списку """
def playground(dataPlay): 
    for item in range(0,len(dataPlay),3):
        print("_"*13)
        print(f"| {dataPlay[item]} | {dataPlay[item+1]} | {dataPlay[item+2]} |")
    print("_"*13)

""" функция запроса от пользователя информации о ходе """

""" await update.message.reply_text(f'Привет {update.effective_user.first_name} хотите сыграть в крестики-нолики?') """

def playerstep():
    step = int(input('введите номер клетки для хода >'))
    return step


""" функция проверки и заполнения поля исходя из выбранного числа """

def checkPlaygroud(dataPlay, stepPlayer):
    for item in range(len(dataPlay)):
        if dataPlay[item] == stepPlayer:
            dataPlay[item] = "X"
    return dataPlay

""" функция хода AI """

def AIstep(dataPlay):
    print("Ход противника:")
    possibleStep = []
    for item in range(len(dataPlay)):
        if dataPlay[item] != 'X' and dataPlay[item] != 'O':
            possibleStep.append(dataPlay[item])
    choice = random.choice(possibleStep)
    for item in range(len(dataPlay)):
        if dataPlay[item] == choice:
            dataPlay[item] = "O"
    return dataPlay


""" функция проверки выигрыша """

def winner(dataPlay):
    if dataPlay[0] == dataPlay[1] == dataPlay [2]:
        print(f'Победили {dataPlay[0]}')
        return False
    if dataPlay[3] == dataPlay[4] == dataPlay [5]:
        print(f'Победили {dataPlay[3]}')
        return False
    if dataPlay[6] == dataPlay[7] == dataPlay [8]:
        print(f'Победили {dataPlay[6]}')
        return False
    if dataPlay[0] == dataPlay[3] == dataPlay [6]:
        print(f'Победили {dataPlay[0]}')
        return False
    if dataPlay[1] == dataPlay[4] == dataPlay [7]:
        print(f'Победили {dataPlay[1]}')
        return False
    if dataPlay[2] == dataPlay[5] == dataPlay [8]:
        print(f'Победили {dataPlay[2]}')
        return False
    if dataPlay[0] == dataPlay[4] == dataPlay [8]:
        print(f'Победили {dataPlay[0]}')
        return False
    if dataPlay[2] == dataPlay[4] == dataPlay [6]:
        print(f'Победили {dataPlay[2]}')
        return False
    return True

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name} хотите сыграть в крестики-нолики?')
    mess = update.message.text
    if mess == "да" or mess == "Да":
        playData = [1,2,3,4,5,6,7,8,9]
        playground(playData)
        while winner(playData):
            for i in range(1,10):
                if i % 2 != 0:
                    checkPlaygroud(playData, playerstep())
                    playground(playData)
                if winner(playData) == False:
                    break
                else:
                    AIstep(playData)
                    playground(playData)
                if winner(playData) == False:
                    break
    else: return



""" playData = [1,2,3,4,5,6,7,8,9]
winner(playData)
print(winner(playData)) """

""" def PlayTime()
playData = [1,2,3,4,5,6,7,8,9]
playground(playData)
playData = checkPlaygroud(playData, playerstep())
playground(playData)
playData = AIstep(playData)
playground(playData)
playData = checkPlaygroud(playData, playerstep())
playground(playData)
playData = AIstep(playData)
playground(playData)
playData = checkPlaygroud(playData, playerstep())
playground(playData)
playData = AIstep(playData)
playground(playData)
winner(playData)
playData = AIstep(playData)
playground(playData)
winner(playData)
playData = AIstep(playData)
playground(playData)
winner(playData) """
""" playData = checkPlaygroud(playData, playerstep())
playground(playData)
playData = AIstep(playData)
playground(playData) """
