from telebot.types import Message
from time import sleep

from keyboards.inline import default_inline_keyb
from loader import bot
from database.db import User, Word
from handlers.custom_handlers.word_quantity import level_ask_quantity


# Добавление пользователя в базу данных


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")
    # sleep(1)

    try:  # проверяем существует ли юзер если да то вытаскиваем его уровень и передаем в функцию
        old_user = User.get(User.user_id == message.from_user.id)
        bot.send_message(
            message.from_user.id,
            "Рад твоему возвращению :)",
            reply_markup=default_inline_keyb.main_menu(),  # Отправляем клавиатуру.
        )

    except: # Если юзер не найденто отправляем функцию с фейк значением
        bot.send_message(message.chat.id, "Меня зовут Potato Bot, Моя задача помочь вам в изучении слов английского языка")
#       sleep(1)
        bot.send_message(
            message.from_user.id,
            "Какой у тебя текущий уровень знаний?",
            reply_markup=default_inline_keyb.level_checking(),  # Отправляем клавиатуру.
        )

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "noob"
    )
)
def noob_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    # Отправляем сообщение пользователю.
    bot.send_message(
        callback_query.from_user.id,
        "Отлично! тогда начнем сначала",
    )
    new_user = User.create(
        user_id=callback_query.from_user.id,
        full_name=callback_query.from_user.full_name,
        username=callback_query.from_user.username,
        level="noob",  # Уровень можно задать по умолчанию или спросить у пользователя
    )

    print(f"Пользователь добавлен с ID {new_user.id}")
    level_ask_quantity(callback_query)


@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "middle"
    )
)
def middle_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    # Отправляем сообщение пользователю.
    bot.send_message(
        callback_query.from_user.id,
        "Отлично! Продолжим совершенствоваться",
    )
    new_user = User.create(
        user_id=callback_query.from_user.id,
        full_name=callback_query.from_user.full_name,
        username=callback_query.from_user.username,
        level="middle",  # Уровень можно задать по умолчанию или спросить у пользователя
    )
    print(f"Пользователь добавлен с ID {new_user.id}")
    level_ask_quantity(callback_query)

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "profi"
    )
)
def profi_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    # Отправляем сообщение пользователю.
    bot.send_message(
        callback_query.from_user.id,
        "ОГО! Даже не знаю смогу ли я тебя чему-нибудь научить, но я постараюсь",
    )
    new_user = User.create(
        user_id=callback_query.from_user.id,
        full_name=callback_query.from_user.full_name,
        username=callback_query.from_user.username,
        level="profi",  # Уровень можно задать по умолчанию или спросить у пользователя
    )
    print(f"Пользователь добавлен с ID {new_user.id}")
    level_ask_quantity(callback_query)