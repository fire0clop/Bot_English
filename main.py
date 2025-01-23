from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from database.db import initialize_db

if __name__ == "__main__":
    initialize_db()  # Инициализируем базу данных
    set_default_commands(bot)
    bot.infinity_polling()
