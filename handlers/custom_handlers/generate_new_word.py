from loader import bot
from database.db import User, Word
from api.Deepseek_API import generate_word
from handlers.custom_handlers.dictionary import send_words_table
from keyboards.inline.default_inline_keyb import ask_learn

def gen_word(callback_query, user):
    """
    Генерирует новое слово для пользователя, исключая уже изученные.

    :param callback_query: Объект callback-запроса от Telegram API.
    :param user: Объект пользователя из базы данных.
    """
    list_words = [w.english_word for w in user.words]

    bot.send_message(
        callback_query.from_user.id,
        "Подождите, генерируем слово..."
    )

    level_mapping = {
        'noob': 'A1-A2',
        'middle': 'B1-B2',
        'profi': 'C1-C2'
    }

    level = level_mapping.get(user.level)
    if not level:
        print("Ошибка: некорректный уровень пользователя")
        return

    en_word, user_id = generate_word(callback_query, words_base=list_words, level=level)

    bot.send_message(
        callback_query.from_user.id,
        f"Новое слово - {en_word.capitalize()} успешно добавлено в словарь. Вот ваш словарь."
    )

    word_obj = Word.get(Word.english_word == en_word, Word.user == user_id)
    word_id = word_obj.id

    bot.send_message(
        callback_query.from_user.id,
        f"Знаешь ли ты это слово - {word_obj.english_word}?",
        reply_markup=ask_learn(word_id)
    )


@bot.callback_query_handler(func=lambda callback_query: callback_query.data.startswith("know_"))
def know(callback_query):
    """
    Отмечает слово как изученное.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    word_id = int(callback_query.data.split("_")[1])
    word_obj = Word.get(Word.id == word_id)
    word_obj.learned = True
    word_obj.save()
    print(f"Пользователь знает слово: {word_obj.english_word}")
    send_words_table(callback_query)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data.startswith("not_know_"))
def not_know(callback_query):
    """
    Отмечает слово как не изученное.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    word_id = int(callback_query.data.split("not_know_")[1])
    word_obj = Word.get(Word.id == word_id)
    word_obj.learned = False
    word_obj.save()
    print(f"Пользователь не знает слово: {word_obj.english_word}")
    send_words_table(callback_query)