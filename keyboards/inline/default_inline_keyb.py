from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def level_checking(lvl_now='no_user'):
    """
    Генерирует инлайн-клавиатуру для выбора уровня знаний пользователя.

    :param lvl_now: Текущий уровень пользователя ('noob', 'middle', 'profi', 'no_user').
    :return: Объект InlineKeyboardMarkup.
    """
    button_1 = InlineKeyboardButton(text="Начальный", callback_data="noob")
    button_2 = InlineKeyboardButton(text="Средний", callback_data="middle")
    button_3 = InlineKeyboardButton(text="Продвинутый", callback_data="profi")
    button_4 = InlineKeyboardButton(text="Не хочу менять", callback_data="cancel")

    keyboard = InlineKeyboardMarkup()
    if lvl_now == 'noob':
        keyboard.add(button_2, button_3, button_4)
    elif lvl_now == 'middle':
        keyboard.add(button_1, button_3, button_4)
    elif lvl_now == 'profi':
        keyboard.add(button_1, button_2, button_4)
    else:
        keyboard.add(button_1, button_2, button_3)

    return keyboard


def word_quantity():
    """
    Генерирует инлайн-клавиатуру для выбора количества изучаемых слов за раз.

    :return: Объект InlineKeyboardMarkup.
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="5", callback_data="five"),
        InlineKeyboardButton(text="10", callback_data="ten"),
        InlineKeyboardButton(text="20", callback_data="twenty")
    )
    return keyboard


def level_update(lvl_now):
    """
    Генерирует инлайн-клавиатуру для обновления уровня пользователя.

    :param lvl_now: Текущий уровень ('noob', 'middle', 'profi').
    :return: Объект InlineKeyboardMarkup.
    """
    button_1 = InlineKeyboardButton(text="Начальный", callback_data="noob_up")
    button_2 = InlineKeyboardButton(text="Средний", callback_data="middle_up")
    button_3 = InlineKeyboardButton(text="Продвинутый", callback_data="profi_up")
    button_4 = InlineKeyboardButton(text="В настройки", callback_data="cancel_up")

    keyboard = InlineKeyboardMarkup()
    if lvl_now == 'noob':
        keyboard.add(button_2, button_3, button_4)
    elif lvl_now == 'middle':
        keyboard.add(button_1, button_3, button_4)
    elif lvl_now == 'profi':
        keyboard.add(button_1, button_2, button_4)
    else:
        keyboard.add(button_1, button_2, button_3)

    return keyboard


def quantity_update(qua_now):
    """
    Генерирует инлайн-клавиатуру для изменения количества изучаемых слов.

    :param qua_now: Текущее количество слов ('5', '10', '20').
    :return: Объект InlineKeyboardMarkup.
    """
    button_1 = InlineKeyboardButton(text="5", callback_data="five_up")
    button_2 = InlineKeyboardButton(text="10", callback_data="ten_up")
    button_3 = InlineKeyboardButton(text="20", callback_data="twenty_up")
    button_4 = InlineKeyboardButton(text="В настройки", callback_data="cancel_up")

    keyboard = InlineKeyboardMarkup()
    if qua_now == '5':
        keyboard.add(button_2, button_3, button_4)
    elif qua_now == '10':
        keyboard.add(button_1, button_3, button_4)
    elif qua_now == '20':
        keyboard.add(button_1, button_2, button_4)
    else:
        keyboard.add(button_1, button_2, button_3)

    return keyboard


def main_menu():
    """
    Генерирует инлайн-клавиатуру главного меню.

    :return: Объект InlineKeyboardMarkup.
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Настройки ️", callback_data="settings"),
        InlineKeyboardButton(text="Словарь", callback_data="dictionary"),
        InlineKeyboardButton(text="Уроки 🛠️", callback_data="lessons"),
        InlineKeyboardButton(text="Добавить слова", callback_data="new_word")
    )
    return keyboard


def menu_settings():
    """
    Генерирует инлайн-клавиатуру для меню настроек.

    :return: Объект InlineKeyboardMarkup.
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Изменить уровень", callback_data="change_lvl"),
        InlineKeyboardButton(text="Изменить количество слов", callback_data="change_quantity_words"),
        InlineKeyboardButton(text="В меню", callback_data="cancel")
    )
    return keyboard


def ask_learn(word_id):
    """
    Генерирует инлайн-клавиатуру для выбора изученного слова.

    :param word_id: ID слова в базе данных.
    :return: Объект InlineKeyboardMarkup.
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Знаю", callback_data=f"know_{word_id}"),
        InlineKeyboardButton(text="Не знаю", callback_data=f"not_know_{word_id}")
    )
    return keyboard


def generate_options_keyboard(options, correct_word):
    """
    Генерирует инлайн-клавиатуру с 4 вариантами ответа.

    :param options: список из 4 слов (3 случайных + 1 правильное).
    :param correct_word: правильный ответ.
    :return: Объект InlineKeyboardMarkup.
    """
    keyboard = InlineKeyboardMarkup()

    for option in options:
        keyboard.add(InlineKeyboardButton(option, callback_data=f"answer:{correct_word}:{option}"))

    return keyboard
