from peewee import *
from datetime import datetime
db = SqliteDatabase('users.db')

# Определение модели
class User(Model):
    """Класс пользователя для базы данных,
    содержит имя пользователя,
    айди пользователя,
    username,
    уровень владения языком выбранный пользователем,
    количество слов которое пользователь изучает за раз,
    а также дату создания объекта"""
    id = AutoField()  # Уникальный автоинкрементный ID записи в таблице
    user_id = IntegerField(unique=True)  # ID пользователя Telegram
    full_name = CharField(null=True)  # Полное имя пользователя
    username = CharField(null=True)  # Юзернейм (может быть null)
    level = CharField()
    word_quantity = IntegerField(default=0)
    created_at = DateTimeField(default=datetime.now)  # Время добавления

    class Meta:
        database = db  # Указание базы данных
        table_name = 'user'  # Имя таблицы в базе данных



class Word(Model):
    """класс """
    id = AutoField()  # Уникальный автоинкрементный ID записи в таблице
    user = ForeignKeyField(User, backref='word', on_delete='CASCADE')  # Связь с пользователем
    russian_word = CharField()  # Слово на русском
    english_word = CharField()  # Перевод слова на английский
    learned = BooleanField(default=False)  # Флаг, изучено слово или нет
    added_at = DateTimeField(default=datetime.now)  # Время добавления слова в словарь

    class Meta:
        database = db  # Указание базы данных
        table_name = 'word'  # Имя таблицы в базе данных
# Создание таблицы
def initialize_db():
    db.connect()
    db.create_tables([User, Word], safe=True)  # Создаём таблицы, если их ещё нет
    print("Таблицы успешно созданы или уже существуют.")