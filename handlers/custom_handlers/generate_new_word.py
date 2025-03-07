from loader import bot
from database.db import User, Word
from api.Deepseek_API import generate_word
from handlers.custom_handlers.dictionary import send_words_table
from keyboards.inline.default_inline_keyb import ask_learn

def gen_word(callback_query, user):
    list_words = []
    words = user.words  # Исправлено: user.word -> user.words
    for w in words:
        list_words.append(w.english_word)

    bot.send_message(
        callback_query.from_user.id,
        "Подождите, генерируем слово..."
    )

    if user.level == 'noob':
        en_word, user_id = generate_word(callback_query, words_base=list_words, level='A1-A2')
    elif user.level == 'middle':
        en_word, user_id = generate_word(callback_query, words_base=list_words, level='B1-B2')
    elif user.level == 'profi':
        en_word, user_id = generate_word(callback_query, words_base=list_words, level='C1-C2')
    else:
        print('error')

    bot.send_message(
        callback_query.from_user.id,
        f"Новое слово - {en_word.capitalize()} успешно добавлено в словарь. Вот ваш словарь."
    )

    print(user_id)
    word_obj = Word.get(Word.english_word == en_word, Word.user == user_id)
    word_id = word_obj.id
    print(word_id)

    bot.send_message(
        callback_query.from_user.id,
        f"Знаешь ли ты это слово - {word_obj.english_word}?",
        reply_markup=ask_learn(word_id),  # Отправляем клавиатуру.
    )


@bot.callback_query_handler(
    func=lambda callback_query:
    callback_query.data.startswith("know_")
)
def know(callback_query):
    word_id = int(callback_query.data.split("_")[1])  # Извлекаем ID слова
    word_obj = Word.get(Word.id == word_id)  # Получаем объект Word
    word_obj.learned = True
    word_obj.save()
    print(f"Пользователь знает слово: {word_obj.english_word}")
    send_words_table(callback_query)

@bot.callback_query_handler(
    func=lambda callback_query:
    callback_query.data.startswith("not_know_")
)
def not_know(callback_query):
    word_id = int(callback_query.data.split("not_know_")[1])  # Извлекаем ID слова
    word_obj = Word.get(Word.id == word_id)  # Получаем объект Word
    word_obj.learned = False
    word_obj.save()
    print(f"Пользователь не знает слово: {word_obj.english_word}")
    send_words_table(callback_query)