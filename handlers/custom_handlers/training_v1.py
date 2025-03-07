from loader import active_sessions, bot
from database.db import User, Word
from api.random_word import get_random_words
from keyboards.inline.default_inline_keyb import generate_options_keyboard, main_menu
import random
from peewee import fn

def init_training(user_id):
    """
    Инициализирует тренировку пользователя. Загружает слова из БД и запускает первый вопрос.

    :param user_id: ID пользователя в Telegram.
    """
    if user_id in active_sessions and active_sessions[user_id]:
        print(f"Продолжаем сессию для пользователя {user_id}")
    else:
        try:
            user = User.get(User.user_id == user_id)
            words = Word.select().where((Word.user == user) & (Word.learned == False))
            active_sessions[user_id] = [(word.russian_word, word.english_word) for word in words]
        except User.DoesNotExist:
            print(f"Пользователь {user_id} не найден в БД")
            return

    print(f"Список слов для пользователя {user_id}: {active_sessions[user_id]}")
    ask_question(user_id)

def ask_question(user_id):
    """
    Отправляет пользователю вопрос о переводе слова с вариантами ответа.

    :param user_id: ID пользователя в Telegram.
    """
    if not active_sessions[user_id]:
        bot.send_message(user_id, "Тренировка пройдена! Можешь начать заново", reply_markup=main_menu())
        return

    russian_word, correct_english_word = active_sessions[user_id].pop(0)

    random_words = get_random_words(3)
    while correct_english_word in random_words:
        random_words = get_random_words(3)

    options = random_words + [correct_english_word]
    random.shuffle(options)

    question_text = f"Как переводится слово - **{russian_word}**?"
    bot.send_message(
        user_id,
        question_text,
        parse_mode="Markdown",
        reply_markup=generate_options_keyboard(options, correct_english_word)
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("answer:"))
def check_answer(call):
    """
    Проверяет ответ пользователя и обновляет его прогресс.

    :param call: Объект callback-запроса от Telegram API.
    """
    _, correct_word, selected_word = call.data.split(":")
    user_id = call.from_user.id

    correct_word = correct_word.strip().lower()
    selected_word = selected_word.strip().lower()

    print(f"✅ DEBUG: correct_word='{correct_word}', selected_word='{selected_word}'")

    user = User.get_or_none(User.user_id == user_id)
    if not user:
        bot.send_message(user_id, "⚠ Ошибка: пользователь не найден в БД.")
        return

    word = Word.get_or_none((Word.user == user) & (fn.LOWER(Word.english_word) == correct_word))
    if not word:
        bot.send_message(user_id, "⚠ Ошибка: слово не найдено в БД.")
        return

    if correct_word == selected_word:
        word.score = min(word.score + 1, 20)
        response_text = "✅ Поздравляю, правильный ответ!"
    else:
        word.score = max(word.score - 1, 0)
        response_text = f"❌ Неверно! Правильный ответ: {word.english_word}"

    if word.score >= 7:
        word.learned = True
        response_text += "\n🎉 Слово изучено! Оно больше не будет появляться в тренировках."

    word.save()
    bot.send_message(user_id, response_text)
    ask_question(user_id)
