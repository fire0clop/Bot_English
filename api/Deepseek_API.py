
from database.db import *
from api.Yandex_dict_API import translate_word
import requests
import json

API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"
def generate_word(callback_query, words_base, level="A1-A2"):
    user = User.get(User.user_id == callback_query.from_user.id)
    user_id = user.id
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    excluded_words = ", ".join(words_base)

    data = {
        "model": "deepseek/deepseek-r1",
        "messages": [
            {
                "role": "user",
                "content": f"Give 1 {level} word (noun/verb/adj/adv) NOT in: {excluded_words}. Send only the word."
            }
        ],
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=5)
        response.raise_for_status()

        result = response.json()
        en_word = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip().lower()
        if en_word is None or en_word == " ":
            return generate_word(callback_query, words_base, level)

        # Если слово уже есть в списке (на случай ошибки модели), повторяем вызов
        if en_word in words_base:
            return generate_word(callback_query, words_base, level)

        ru_word = translate_word(en_word)
        if ru_word is None:  # Если перевода нет, генерируем другое слово
            print(f"Не удалось найти перевод для {en_word}, повторяем запрос...")
            print(ru_word)
            return generate_word(callback_query, words_base, level)
        Word.create(
            user=user,
            russian_word=ru_word,
            english_word=en_word,
            learned=False,
            added_at=datetime.now()
        )

        return en_word, user_id


    except (requests.exceptions.Timeout, requests.exceptions.RequestException):
        return generate_word(callback_query, words_base, level)