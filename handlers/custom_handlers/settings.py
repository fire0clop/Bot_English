from telebot.types import Message



from loader import bot
from database.db import User
from keyboards.inline.default_inline_keyb import menu_settings, main_menu, level_update, quantity_update


@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "change_lvl"
    )
)
def change_lvl(callback_query):
    old_user = User.get(User.user_id == callback_query.from_user.id)
    us_lvl = old_user.level
    if us_lvl == 'noob':
        bot.send_message(
            callback_query.from_user.id,
            "Текущий уровень: Начальный \n На что хочешь изменить его",
            reply_markup=level_update(us_lvl),  # Отправляем клавиатуру.
        )
    elif us_lvl == 'middle':
        bot.send_message(
            callback_query.from_user.id,
            "Текущий уровень: Средний \n На что хочешь изменить его",
            reply_markup=level_update(us_lvl),  # Отправляем клавиатуру.
        )
    else:
        bot.send_message(
            callback_query.from_user.id,
            "Текущий уровень: Продвинутый \n На что хочешь изменить его",
            reply_markup=level_update(us_lvl),  # Отправляем клавиатуру.
        )

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "noob_up"
    )
)
def noob_up_answer(callback_query):
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.level = 'noob'
        user.save()
        bot.send_message(
            callback_query.from_user.id,
            "Ваш уровень успешно обновлен на Начальный",
              # Отправляем клавиатуру.
        )
    except:
        bot.send_message(
            callback_query.from_user.id,
            "Произошла неизвестная ошибка",

        )
    finally:
        bot.send_message(
            callback_query.from_user.id,
            "Вернемся в настройки",
            reply_markup=menu_settings(),  # Отправляем клавиатуру.
        )


@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "middle_up"
    )
)
def middle_up_answer(callback_query):
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.level = 'middle'
        user.save()
        bot.send_message(
            callback_query.from_user.id,
            "Ваш уровень успешно обновлен на Средний",
            # Отправляем клавиатуру.
        )
    except:
        bot.send_message(
            callback_query.from_user.id,
            "Произошла неизвестная ошибка",

        )
    finally:
        bot.send_message(
            callback_query.from_user.id,
            "Вернемся в настройки",
            reply_markup=menu_settings(),  # Отправляем клавиатуру.
        )
@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "profi_up"
    )
)
def profi_up_answer(callback_query):
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.level = 'profi'
        user.save()
        bot.send_message(
            callback_query.from_user.id,
            "Ваш уровень успешно обновлен на Продвинутый",
            # Отправляем клавиатуру.
        )
    except:
        bot.send_message(
            callback_query.from_user.id,
            "Произошла неизвестная ошибка",

        )
    finally:
        bot.send_message(
            callback_query.from_user.id,
            "Вернемся в настройки",
            reply_markup=menu_settings(),  # Отправляем клавиатуру.
        )










@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "change_quantity_words"
    )
)
def change_quantity_words(callback_query):
    old_user = User.get(User.user_id == callback_query.from_user.id)
    us_qua = old_user.word_quantity
    if us_qua == 5:
        bot.send_message(
            callback_query.from_user.id,
            "Текущее количество изучаемых слов - 5. \n На что хочешь изменить его",
            reply_markup=quantity_update(us_qua),  # Отправляем клавиатуру.
        )
    elif us_qua == 10:
        bot.send_message(
            callback_query.from_user.id,
            "Текущее количество изучаемых слов - 10. \n На что хочешь изменить его",
            reply_markup=quantity_update(us_qua),  # Отправляем клавиатуру.
        )
    else:
        bot.send_message(
            callback_query.from_user.id,
            "Текущее количество изучаемых слов - 20. \n На что хочешь изменить его",
            reply_markup=quantity_update(us_qua),  # Отправляем клавиатуру.
        )






@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "five_up"
    )
)
def five_up_answer(callback_query):
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.word_quantity = 5
        user.save()
        bot.send_message(
            callback_query.from_user.id,
            "Количество ваших слов обновлено до 5",
              # Отправляем клавиатуру.
        )
    except:
        bot.send_message(
            callback_query.from_user.id,
            "Произошла неизвестная ошибка",

        )
    finally:
        bot.send_message(
            callback_query.from_user.id,
            "Вернемся в настройки",
            reply_markup=menu_settings(),  # Отправляем клавиатуру.
        )


@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "ten_up"
    )
)
def ten_up_answer(callback_query):
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.word_quantity = 10
        user.save()
        bot.send_message(
            callback_query.from_user.id,
            "Количество ваших слов обновлено до 10",
            # Отправляем клавиатуру.
        )
    except:
        bot.send_message(
            callback_query.from_user.id,
            "Произошла неизвестная ошибка",

        )
    finally:
        bot.send_message(
            callback_query.from_user.id,
            "Вернемся в настройки",
            reply_markup=menu_settings(),  # Отправляем клавиатуру.
        )
@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "twenty_up"
    )
)
def twenty_up_answer(callback_query):
    try:
        user = User.get(User.user_id == callback_query.from_user.id)
        user.word_quantity = 20
        user.save()
        bot.send_message(
            callback_query.from_user.id,
            "Количество ваших слов обновлено до 20",
            # Отправляем клавиатуру.
        )
    except:
        bot.send_message(
            callback_query.from_user.id,
            "Произошла неизвестная ошибка",

        )
    finally:
        bot.send_message(
            callback_query.from_user.id,
            "Вернемся в настройки",
            reply_markup=menu_settings(),
        )# Отправляем клавиатуру.








@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "cancel_up"
    )
)
def cancel_up_answer(callback_query):
    bot.send_message(
        callback_query.from_user.id,
        "Вернемся в настройки",
        reply_markup=menu_settings(),  # Отправляем клавиатуру.
    )
@bot.callback_query_handler(
    func=lambda callback_query: (
            callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
            == "cancel"
    )
)
def cancel_answer(callback_query):
    bot.send_message(
        callback_query.from_user.id,
        "Вернемся в меню",
        reply_markup=main_menu(),  # Отправляем клавиатуру.
    )