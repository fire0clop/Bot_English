from loader import bot
from handlers.custom_handlers.training_v1 import init_training
from keyboards.inline.default_inline_keyb import menu_settings
from handlers.custom_handlers.dictionary import send_words_table
from handlers.custom_handlers.generate_new_word import gen_word
from database.db import User


@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "settings"
    )
)
def settings(callback_query):
    bot.send_message(
        callback_query.from_user.id,
        "Вот твои настроечки",
        reply_markup=menu_settings(),  # Отправляем клавиатуру.
    )
    # Логика для настроек уровня и количества слов

@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "dictionary"
    )
)
def dictionary(callback_query):
    send_words_table(callback_query)
    # Логика для вывода таблицы типа
    # английское слово | перевод на русский | Выучено или нет


@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "lessons"
    )
)
def lessons(callback_query):
    user_id = callback_query.from_user.id
    init_training(user_id)



@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "new_word"
    )
)
def new_word(callback_query):
    user = User.get(User.user_id == callback_query.from_user.id)
    word_id = gen_word(callback_query, user)


