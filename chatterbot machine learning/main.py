import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
bot=ChatBot("Vishal")
bot.set_trainer(ChatterBotCorpusTrainer)
#train on data learning yml filrs
bot.train("chatterbot.corpus.english")

while(True):
    message=input("You:")
    
    if (message!="Bye") or (message!="bye"):
        print("{}:{}".format(bot.name,bot.get_response(message)))
        
    if (message=="Bye") or (message=="bye"):
        print("{} Bye!".format(bot.name))
        break
