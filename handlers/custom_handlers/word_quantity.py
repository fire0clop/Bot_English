from telebot.types import Message
from database.db import User
from keyboards.inline import default_inline_keyb
from loader import bot


def level_ask_quantity(callback_query):
    """
    Запрашивает у пользователя количество слов для изучения за раз.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    bot.send_message(
        callback_query.from_user.id,
        "Сколько слов ты хочешь изучать за раз?",
        reply_markup=default_inline_keyb.word_quantity()
    )


def update_word_quantity(callback_query, quantity):
    """
    Обновляет количество изучаемых слов в базе данных и отправляет сообщение пользователю.

    :param callback_query: Объект callback-запроса от Telegram API.
    :param quantity: Новое количество слов для изучения.
    """
    user = User.get(User.user_id == callback_query.from_user.id)
    user.word_quantity = quantity
    user.save()

    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )

    intro_message = (
        "Отлично! Первичная настройка твоей учебной программы проведена. "
        "У тебя будет собственный словарь, там ты сможешь узнать, какие слова ты уже выучил и какие только изучаешь."
    )
    instruction_message = (
        "Я буду скидывать тебе слова, соответствующие твоему уровню знаний. "
        "Если ты их знаешь, нажимай соответствующую кнопку, и они сразу будут в словаре помечены как уже изученные."
    )

    bot.send_message(callback_query.from_user.id, intro_message)
    bot.send_message(callback_query.from_user.id, instruction_message)
    bot.send_message(
        callback_query.from_user.id,
        "Все готово! Дальше дело за тобой :)",
        reply_markup=default_inline_keyb.main_menu()
    )


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "five")
def quantity_five(callback_query):
    """
    Обновляет количество изучаемых слов до 5.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    update_word_quantity(callback_query, 5)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "ten")
def quantity_ten(callback_query):
    """
    Обновляет количество изучаемых слов до 10.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    update_word_quantity(callback_query, 10)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "twenty")
def quantity_twenty(callback_query):
    """
    Обновляет количество изучаемых слов до 20.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    update_word_quantity(callback_query, 20)
