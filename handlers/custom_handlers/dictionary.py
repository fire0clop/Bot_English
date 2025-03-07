from loader import bot
from database.db import User, Word
from keyboards.inline import default_inline_keyb

def send_words_table(callback_query):
    """
    Отправляет пользователю таблицу с его словами.

    :param callback_query: Объект callback-запроса от Telegram API.
    """
    user_id = callback_query.from_user.id
    user = User.get_or_none(user_id=user_id)

    if user:
        words = Word.select().where(Word.user == user)
        words_count = words.count()

        if words_count > 0:
            message_text = (
                f"Слова для пользователя {user.full_name} (Количество слов: {words_count}):\n"
                f"{'№':<2} | {'Ру-слово':<10} | {'Анг-слово':<10} | {'Статус':<10}\n"
                f"{'-' * 35}\n"
            )

            for idx, word in enumerate(words, start=1):
                status = "Выучено" if word.learned else "Обучение"
                message_text += f"{idx:<2} | {word.russian_word:<10} | {word.english_word:<10} | {status:<10}\n"

            bot.send_message(
                chat_id=callback_query.from_user.id,
                text=f"<pre>{message_text}</pre>",
                parse_mode="HTML"
            )
        else:
            bot.send_message(
                chat_id=callback_query.from_user.id,
                text="У вас пока нет связанных слов."
            )
    else:
        bot.send_message(
            chat_id=callback_query.from_user.id,
            text="Пользователь не найден."
        )

    bot.send_message(
        callback_query.from_user.id,
        "Все готово! Дальше дело за тобой :)",
        reply_markup=default_inline_keyb.main_menu()
    )
