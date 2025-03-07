from loader import bot, active_sessions
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from database.db import initialize_db
from database.db import Word, User  # Импортируем модели

def initialize_sessions():
    """Загружает слова всех пользователей в оперативную память при запуске бота."""
    global active_sessions

    # Получаем всех пользователей
    users = User.select()
    for user in users:
        words = (
            Word.select()
            .where((Word.user == user) & (Word.learned == False))
        )
        active_sessions[user.user_id] = [(word.russian_word, word.english_word) for word in words]

    print("Сессии пользователей инициализированы:", active_sessions)

if __name__ == "__main__":
    initialize_db()  # Инициализируем базу данных
    initialize_sessions()  # Загружаем слова пользователей в память
    set_default_commands(bot)
    bot.infinity_polling()
