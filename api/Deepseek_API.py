from database.db import *
from api.Yandex_dict_API import translate_word
import requests
import re
from openai import OpenAI
from datetime import datetime

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)


def generate_word(callback_query, words_base, level="A1-A2"):
    """
    Генерирует новое английское слово, исключая уже известные пользователю.

    :param callback_query: объект запроса от Telegram API
    :param words_base: список слов, которые уже известны пользователю
    :param level: уровень сложности (по умолчанию A1-A2)
    :return: сгенерированное слово на английском и ID пользователя
    """
    user = User.get(User.user_id == callback_query.from_user.id)
    user_id = user.id
    excluded_words = ", ".join(words_base)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",
         "content": f"Give 1 {level} word (noun/verb/adj/adv) NOT in: {excluded_words}. Send only the word."}
    ]

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-zero:free",
            messages=messages,
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            extra_body={}
        )

        en_word = response.choices[0].message.content.strip().lower()
        en_word = re.sub(r"\\boxed\{(.*?)\}", r"\1", en_word)  # Удаляем LaTeX-обертки

        if not en_word or en_word in words_base:
            return generate_word(callback_query, words_base, level)

        ru_word = translate_word(en_word)
        if ru_word is None:
            print(f"Не удалось найти перевод для {en_word}, повторяем запрос...")
            return generate_word(callback_query, words_base, level)

        Word.create(
            user=user,
            russian_word=ru_word,
            english_word=en_word,
            learned=False,
            added_at=datetime.now()
        )

        return en_word, user_id

    except Exception as e:
        print(f"Ошибка запроса: {e}")
        return generate_word(callback_query, words_base, level)
