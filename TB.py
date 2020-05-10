
import telebot
from ast import literal_eval
from pprint import pprint

bot = telebot.TeleBot("TOKEN")
def SlashDecode(a):

    s=(a.index("'entities'"))
    end="'caption_entities'"
    e=(a.index(end))
    a=a.replace(a[s:e],"")
    Message = literal_eval(str(a))
    return Message
@bot.message_handler()
def send_welcome(message):
    
    bot.reply_to(message, "Got Your Message")
    message=str(message).replace("None","False")
    try:
        Message = literal_eval(str(message))
        print ("No Slash")
    except:
        Message = SlashDecode(str(message))
        print ("Slash")
    
    pprint (Message)


bot.polling()



