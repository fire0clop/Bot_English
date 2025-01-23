from loader import bot
from database.db import User, Word
from keyboards.inline import default_inline_keyb


def send_words_table(callback_query):
    # Проверяем, есть ли пользователь с указанным ID
    user_id = callback_query.from_user.id
    user = User.get_or_none(user_id=user_id)

    if user:
        # Получаем все слова, связанные с этим пользователем
        words = Word.select().where(Word.user == user)
        words_count = words.count()  # Подсчитываем количество слов

        if words_count > 0:
            # Формируем шапку таблицы
            message_text = f"Слова для пользователя {user.full_name} (Количество слов: {words_count}):\n"
            message_text += f"{'№':<5} | {'Русское слово':<15} | {'Английское слово':<15} | {'Статус':<10}\n"
            message_text += "-" * 55 + "\n"

            # Добавляем строки с данными
            for idx, word in enumerate(words, start=1):  # Нумерация начинается с 1
                status = "Выучено" if word.learned else "Обучение"
                message_text += f"{idx:<5} | {word.russian_word:<15} | {word.english_word:<15} | {status:<10}\n"

            # Отправляем сообщение пользователю
            bot.send_message(chat_id=callback_query.from_user.id, text=f"<pre>{message_text}</pre>", parse_mode="HTML")
        else:
            # Сообщение, если слов нет
            bot.send_message(chat_id=callback_query.from_user.id, text=f"У вас пока нет связанных слов.")
    else:
        # Сообщение, если пользователь не найден
        bot.send_message(chat_id=callback_query.from_user.id, text=f"Пользователь не найден.")
    bot.send_message(
        callback_query.from_user.id,
        "Все готово! Дальше дело за тобой :)",
        reply_markup=default_inline_keyb.main_menu(),  # Отправляем клавиатуру.
    )

