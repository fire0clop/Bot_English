from telebot.types import Message
from loader import bot
from database.db import User
from keyboards.inline.default_inline_keyb import menu_settings, main_menu, level_update, quantity_update


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "change_lvl")
def change_lvl(callback_query):
    """
    Обрабатывает запрос на изменение уровня языка.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    user = User.get(User.user_id == callback_query.from_user.id)
    levels = {
        'noob': "Начальный",
        'middle': "Средний",
        'profi': "Продвинутый"
    }
    current_level = levels.get(user.level, "Неизвестный")

    bot.send_message(
        callback_query.from_user.id,
        f"Текущий уровень: {current_level} \nНа что хочешь изменить его?",
        reply_markup=level_update(user.level)
    )


def update_level(callback_query, new_level, level_name):
    """
    Обновляет уровень языка пользователя.

    :param callback_query: Объект callback-запроса от Telegram API.
    :param new_level: Новый уровень ('noob', 'middle', 'profi').
    :param level_name: Название уровня для вывода пользователю.
    """
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.level = new_level
        user.save()
        bot.send_message(callback_query.from_user.id, f"Ваш уровень успешно обновлен на {level_name}")
    except:
        bot.send_message(callback_query.from_user.id, "Произошла неизвестная ошибка")
    finally:
        bot.send_message(callback_query.from_user.id, "Вернемся в настройки", reply_markup=menu_settings())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "noob_up")
def noob_up_answer(callback_query):
    update_level(callback_query, "noob", "Начальный")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "middle_up")
def middle_up_answer(callback_query):
    update_level(callback_query, "middle", "Средний")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "profi_up")
def profi_up_answer(callback_query):
    update_level(callback_query, "profi", "Продвинутый")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "change_quantity_words")
def change_quantity_words(callback_query):
    """
    Обрабатывает запрос на изменение количества изучаемых слов.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    user = User.get(User.user_id == callback_query.from_user.id)
    bot.send_message(
        callback_query.from_user.id,
        f"Текущее количество изучаемых слов - {user.word_quantity}.\nНа что хочешь изменить его?",
        reply_markup=quantity_update(user.word_quantity)
    )


def update_word_quantity(callback_query, new_quantity):
    """
    Обновляет количество изучаемых слов.

    :param callback_query: Объект callback-запроса от Telegram API.
    :param new_quantity: Новое количество слов.
    """
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.word_quantity = new_quantity
        user.save()
        bot.send_message(callback_query.from_user.id, f"Количество ваших слов обновлено до {new_quantity}")
    except:
        bot.send_message(callback_query.from_user.id, "Произошла неизвестная ошибка")
    finally:
        bot.send_message(callback_query.from_user.id, "Вернемся в настройки", reply_markup=menu_settings())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "five_up")
def five_up_answer(callback_query):
    update_word_quantity(callback_query, 5)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "ten_up")
def ten_up_answer(callback_query):
    update_word_quantity(callback_query, 10)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "twenty_up")
def twenty_up_answer(callback_query):
    update_word_quantity(callback_query, 20)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "cancel_up")
def cancel_up_answer(callback_query):
    """
    Возвращает пользователя в меню настроек.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    bot.send_message(callback_query.from_user.id, "Вернемся в настройки", reply_markup=menu_settings())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "cancel")
def cancel_answer(callback_query):
    """
    Возвращает пользователя в главное меню.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    bot.send_message(callback_query.from_user.id, "Вернемся в меню", reply_markup=main_menu())
