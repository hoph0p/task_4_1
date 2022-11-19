import re

import telebot

token = '5615832687:AAEyK0k_SmHRWWvlv5jcuVX67H5xh8LCB4c'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    #Убираем из строки лишние символы
    re_string = re.sub("[&|?|,|.]", '', message.text)
    re_string = str(re_string)

    for word in re_string.split():
        if word in str(message.from_user.full_name):
            return bot.send_message(message.chat.id, text='Ба! Знакомые все лица!' )

    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
