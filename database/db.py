from peewee import *
from datetime import datetime

db = SqliteDatabase('users.db')

class User(Model):
    """
    Модель пользователя.

    Атрибуты:
    - id: Уникальный автоинкрементный идентификатор.
    - user_id: ID пользователя в Telegram.
    - full_name: Полное имя пользователя.
    - username: Имя пользователя (может быть null).
    - level: Уровень владения языком.
    - word_quantity: Количество слов, изучаемых за раз.
    - created_at: Дата и время создания записи.
    """
    id = AutoField()
    user_id = IntegerField(unique=True)
    full_name = CharField(null=True)
    username = CharField(null=True)
    level = CharField()
    word_quantity = IntegerField(default=0)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'user'


class Word(Model):
    """
    Модель слова пользователя.

    Атрибуты:
    - id: Уникальный автоинкрементный идентификатор.
    - user: Связь с пользователем (ForeignKey).
    - russian_word: Русское слово.
    - english_word: Английский перевод.
    - learned: Флаг изученного слова (по умолчанию False).
    - score: Баллы за изучение слова (0 по умолчанию).
    - added_at: Дата и время добавления слова.
    """
    id = AutoField()
    user = ForeignKeyField(User, backref='words', on_delete='CASCADE')
    russian_word = CharField()
    english_word = CharField()
    learned = BooleanField(default=False)
    score = IntegerField(default=0)
    added_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'word'


def initialize_db():
    """
    Инициализирует базу данных, создавая таблицы, если они ещё не существуют.
    """
    db.connect()
    db.create_tables([User, Word], safe=True)
    print("Таблицы успешно созданы или уже существуют.")
