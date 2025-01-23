from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
def level_checking(lvl_now = 'no_user'):
    """ инлайн клавиатура проверяющая уровень значний пользователя
    ps реализовать систему перехода с одного уровня на другой, при этом в варианте выбора при переходе не должно быть текущего уровеня"""
    # Создаемкнопки с вариантами ответа
    button_1 = InlineKeyboardButton(text="Начальный", callback_data="noob")
    button_2 = InlineKeyboardButton(text="Средний", callback_data="middle")
    button_3 = InlineKeyboardButton(text="Продвинутый", callback_data="profi")
    button_4 = InlineKeyboardButton(text="Не хочу менять", callback_data="cancel")
    # Создаём объект клавиатуры, добавляя в него кнопки
    keyboard = InlineKeyboardMarkup()
    if lvl_now == 'noob':
        keyboard.add(button_2, button_3, button_4)
    elif lvl_now == 'middle':
        keyboard.add(button_1, button_3, button_4)
    elif lvl_now == 'profi':
        keyboard.add(button_1, button_2, button_4)
    else:
        keyboard.add(button_1,button_2, button_3)
    return keyboard


def word_quantity():
    """ Инлайн клавиатура для задачи количества слов изучаемой за раз"""
    button_1 = InlineKeyboardButton(text="5", callback_data="five")
    button_2 = InlineKeyboardButton(text="10", callback_data="ten")
    button_3 = InlineKeyboardButton(text="20", callback_data="twenty")
    # Создаём объект клавиатуры, добавляя в него кнопки
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1,button_2, button_3)
    return keyboard


def level_update(lvl_now):
    """ инлайн клавиатура проверяющая уровень значний пользователя
    ps реализовать систему перехода с одного уровня на другой, при этом в варианте выбора при переходе не должно быть текущего уровеня"""
    # Создаемкнопки с вариантами ответа
    button_1 = InlineKeyboardButton(text="Начальный", callback_data="noob_up")
    button_2 = InlineKeyboardButton(text="Средний", callback_data="middle_up")
    button_3 = InlineKeyboardButton(text="Продвинутый", callback_data="profi_up")
    button_4 = InlineKeyboardButton(text="Не хочу менять", callback_data="cancel_up")
    # Создаём объект клавиатуры, добавляя в него кнопки
    keyboard = InlineKeyboardMarkup()
    if lvl_now == 'noob':
        keyboard.add(button_2, button_3, button_4)
    elif lvl_now == 'middle':
        keyboard.add(button_1, button_3, button_4)
    elif lvl_now == 'profi':
        keyboard.add(button_1, button_2, button_4)
    else:
        keyboard.add(button_1,button_2, button_3)
    return keyboard

def quantity_update(qua_now):
    """ инлайн клавиатура проверяющая уровень значний пользователя
    ps реализовать систему перехода с одного уровня на другой, при этом в варианте выбора при переходе не должно быть текущего уровня"""
    # Создаемкнопки с вариантами ответа
    button_1 = InlineKeyboardButton(text="5", callback_data="five_up")
    button_2 = InlineKeyboardButton(text="10", callback_data="ten_up")
    button_3 = InlineKeyboardButton(text="20", callback_data="twenty_up")
    button_4 = InlineKeyboardButton(text="Не хочу менять", callback_data="cancel_up")
    # Создаём объект клавиатуры, добавляя в него кнопки
    keyboard = InlineKeyboardMarkup()
    if qua_now == '5':
        keyboard.add(button_2, button_3, button_4)
    elif qua_now == '10':
        keyboard.add(button_1, button_3, button_4)
    elif qua_now == '20':
        keyboard.add(button_1, button_2, button_4)
    else:
        keyboard.add(button_1,button_2, button_3)
    return keyboard


def main_menu():
    """ Инлайн клавиатура главного меню"""
    button_1 = InlineKeyboardButton(text="К настройкам ️", callback_data="settings")
    button_2 = InlineKeyboardButton(text="К словарю", callback_data="dictionary")
    button_3 = InlineKeyboardButton(text="К урокам 🛠️", callback_data="lessons")
    button_4 = InlineKeyboardButton(text="Добавить слова 🛠️", callback_data="new_word")
    # Создаём объект клавиатуры, добавляя в него кнопки
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard

def menu_settings():
    """Инлайн клавиатура для меню настроек"""
    button_1 = InlineKeyboardButton(text="Изменить уровень", callback_data="change_lvl")
    button_2 = InlineKeyboardButton(text="Изменить количество слов", callback_data="change_quantity_words")
    button_3 = InlineKeyboardButton(text="Не хочу менять", callback_data="cancel")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3)
    return keyboard