from telebot.types import Message
from database.db import User

from keyboards.inline import default_inline_keyb
from loader import bot

def level_ask_quantity(callback_query):
    bot.send_message(
        callback_query.from_user.id,
        "Сколько слов ты хочешь изучать за раз?",
        reply_markup=default_inline_keyb.word_quantity(),  # Отправляем клавиатуру.
    )

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "five"
    )
)
def quantity_five(callback_query):
    """Обновление базы данных с изучением 5 слов"""
    user = User.get(User.user_id == callback_query.from_user.id)  # Получаем объект
    user.word_quantity = 5  # Изменяем поле
    user.save()
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    bot.send_message(callback_query.from_user.id,
                     "Отлично! первичная настройка твоей учебной программы проведена. "
                     "У тебя будет собственный словарь, там ты сможешь узнать какие слова ты уже выучил и какие только изучаешь")
    bot.send_message(callback_query.from_user.id,
                     "Я буду скидывать тебе слова соответствующие твоему уровню знаний, "
                     "если ты их знаешь нажимай соответсвующую кнопку и они сразу будут в словаре помечены как уже изученные")
    bot.send_message(
        callback_query.from_user.id,
        "Все готово! Дальше дело за тобой :)",
        reply_markup=default_inline_keyb.main_menu(),  # Отправляем клавиатуру.
    )





@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "ten"
    )
)
def quantity_ten(callback_query):
    """Обновление базы данных с изучением 10 слов"""
    user = User.get(User.user_id == callback_query.from_user.id)  # Получаем объект
    user.word_quantity = 10  # Изменяем поле
    user.save()
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    bot.send_message(callback_query.from_user.id,
                     "Отлично! первичная настройка твоей учебной программы проведена. "
                     "У тебя будет собственный словарь, там ты сможешь узнать какие слова ты уже выучил и какие только изучаешь")
    bot.send_message(callback_query.from_user.id,
                     "Я буду скидывать тебе слова соответствующие твоему уровню знаний, "
                     "если ты их знаешь нажимай соответсвующую кнопку и они сразу будут в словаре помечены как уже изученные")
    bot.send_message(
        callback_query.from_user.id,
        "Все готово! Дальше дело за тобой :)",
        reply_markup=default_inline_keyb.main_menu(),  # Отправляем клавиатуру.
    )





@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "twenty"
    )
)
def quantity_twenty(callback_query):
    """Обновление базы данных с изучением 20 слов"""
    user = User.get(User.user_id == callback_query.from_user.id)  # Получаем объект
    user.word_quantity = 20  # Изменяем поле
    user.save()
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    bot.send_message(callback_query.from_user.id,
                     "Отлично! первичная настройка твоей учебной программы проведена. "
                     "У тебя будет собственный словарь, там ты сможешь узнать какие слова ты уже выучил и какие только изучаешь")
    bot.send_message(callback_query.from_user.id,
                     "Я буду скидывать тебе слова соответствующие твоему уровню знаний, "
                     "если ты их знаешь нажимай соответсвующую кнопку и они сразу будут в словаре помечены как уже изученные")
    bot.send_message(
        callback_query.from_user.id,
        "Все готово! Дальше дело за тобой :)",
        reply_markup=default_inline_keyb.main_menu(),  # Отправляем клавиатуру.
    )