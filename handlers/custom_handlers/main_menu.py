from telebot.types import Message

from loader import bot
from keyboards.inline.default_inline_keyb import menu_settings
from handlers.custom_handlers.dictionary import send_words_table
from api.Cohere_API import *
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
    pass
    # Логика для отправки к тренировке слов

@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "new_word"
    )
)
def new_word(callback_query):
    list_words = []
    user = User.get(User.user_id == callback_query.from_user.id)
    words = user.word
    for w in words:
        list_words.append(w.english_word)

    bot.send_message(
        callback_query.from_user.id,
        "Подождите, генерируем слово..."
    )
    if user.level == 'noob':
        print('вызываем апи для нубов')
        word_new = generate_word(callback_query, words_base = list_words, level = 'A1-A2')
    elif user.level == 'middle':
        print('вызываем апи для среднечков')
        word_new = generate_word(callback_query, words_base = list_words, level = 'B1-B2')
    elif user.level == 'profi':
        print('вызываем апи для профи')
        word_new = generate_word(callback_query, words_base = list_words, level = 'C1-C2')
    else:
        print('error')

    bot.send_message(
        callback_query.from_user.id,
        f"Новое слово - {word_new} успешно добавлено в словарь. Вот ваш словарь"
    )
    send_words_table(callback_query)
