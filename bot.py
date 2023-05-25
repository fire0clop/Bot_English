import telebot
bot = telebot.TeleBot('6027228281:AAHNU5lgWna1Oi42s9LhUIsOPiQ14oXsP5Q')#токен(ссылка) на бота к которому обращаемся

@bot.message_handler(commands = ['start'])
def start(message):
    hello_message = 'Хаюшки {}, меня зовут картошка-бот, я могу продавать слонов'.format(message.from_user.first_name)
    bot.send_message(message.chat.id, hello_message)# можно писать без parse_mode, а можно использовать параметры html для текста
    bot.send_message(message.chat.id, 'Давай начнем, итак... Хочешь купить слона?')



@bot.message_handler(content_types = ['text'])
def get_user_text(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Поздравляю! теперь у тебя есть слон, купишь еще слона?')
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'а ты купи слона и у тебя будет слон')
        bot.send_message(message.chat.id, 'Хочешь купить слона?')
    else:
        bot.send_message(message.chat.id, 'все так говорят а ты купи слона')



bot.polling(none_stop=True)