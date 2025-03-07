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

        # Удаляем LaTeX-обертки, если они есть
        en_word = re.sub(r"\\boxed\{(.*?)\}", r"\1", en_word)

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