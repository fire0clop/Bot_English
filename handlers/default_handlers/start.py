from telebot.types import Message
from keyboards.inline import default_inline_keyb
from loader import bot
from database.db import User
from handlers.custom_handlers.word_quantity import level_ask_quantity

@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    """
    Обрабатывает команду /start. Приветствует пользователя и проверяет его в базе данных.

    :param message: Объект сообщения от Telegram API.
    """
    bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")

    try:
        old_user = User.get(User.user_id == message.from_user.id)
        bot.send_message(
            message.from_user.id,
            "Рад твоему возвращению :)",
            reply_markup=default_inline_keyb.main_menu()
        )
    except:
        bot.send_message(
            message.chat.id,
            "Меня зовут Potato Bot. Моя задача — помочь вам в изучении английских слов."
        )
        bot.send_message(
            message.from_user.id,
            "Какой у тебя текущий уровень знаний?",
            reply_markup=default_inline_keyb.level_checking()
        )

def register_user(callback_query, level, message):
    """
    Регистрирует нового пользователя в базе данных и запрашивает количество изучаемых слов.

    :param callback_query: Объект callback-запроса от Telegram API.
    :param level: Уровень владения языком ('noob', 'middle', 'profi').
    :param message: Приветственное сообщение для пользователя.
    """
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    bot.send_message(callback_query.from_user.id, message)

    new_user = User.create(
        user_id=callback_query.from_user.id,
        full_name=callback_query.from_user.full_name,
        username=callback_query.from_user.username,
        level=level
    )
    print(f"Пользователь добавлен с ID {new_user.id}")

    level_ask_quantity(callback_query)

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "noob")
def noob_answer(callback_query):
    """
    Обрабатывает выбор начального уровня ('noob').

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    register_user(callback_query, "noob", "Отлично! Тогда начнем сначала.")

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "middle")
def middle_answer(callback_query):
    """
    Обрабатывает выбор среднего уровня ('middle').

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    register_user(callback_query, "middle", "Отлично! Продолжим совершенствоваться.")

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "profi")
def profi_answer(callback_query):
    """
    Обрабатывает выбор продвинутого уровня ('profi').

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    register_user(callback_query, "profi", "ОГО! Даже не знаю, смогу ли я тебя чему-нибудь научить, но я постараюсь.")
