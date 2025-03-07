from loader import bot
from handlers.custom_handlers.training_v1 import init_training
from keyboards.inline.default_inline_keyb import menu_settings
from handlers.custom_handlers.dictionary import send_words_table
from handlers.custom_handlers.generate_new_word import gen_word
from database.db import User

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "settings")
def settings(callback_query):
    """
    Отправляет пользователю меню настроек.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    bot.send_message(
        callback_query.from_user.id,
        "Вот твои настроечки",
        reply_markup=menu_settings()
    )

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "dictionary")
def dictionary(callback_query):
    """
    Отправляет пользователю список его слов.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    send_words_table(callback_query)

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "lessons")
def lessons(callback_query):
    """
    Запускает тренировку слов для пользователя.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    user_id = callback_query.from_user.id
    init_training(user_id)

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "new_word")
def new_word(callback_query):
    """
    Генерирует новое слово для пользователя.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    user = User.get(User.user_id == callback_query.from_user.id)
    gen_word(callback_query, user)
