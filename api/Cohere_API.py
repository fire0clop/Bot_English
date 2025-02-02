import cohere
from database.db import *
from api.Yandex_dict_API import translate_word
import requests
import json

# # Ваш API-ключ Cohere
# api_key = "xDrJe7QbwSiIzSw3Tsgi8VzXNFAJiVJaVMIvZkww"
# co = cohere.Client(api_key)
#
# # Список для хранения уже сгенерированных слов
#
# def generate_word_for_beginer(callback_query, words_base):
#     user = User.get(User.user_id == callback_query.from_user.id)
#     # Преобразуем список в строку для запроса
#     excluded_words = ", ".join(words_base) if words_base else "none"
#
#     # Создаем запрос с учетом исключений
#     prompt = (
#         f"Generate an English word from beginner vocabulary, for English level A0-A2. The word must be a noun, verb, adjective, or adverb. Do not use any of these words: {excluded_words}."
#     )
#
#     # Запрос к Cohere API
#     response = co.generate(
#         model="command",
#         prompt=prompt,
#         max_tokens=1,
#         temperature=0.9,  # Добавляем случайности
#         k=0,
#         p=0.9
#     )
#
#     # Получаем результат
#     if response.generations:
#         word = response.generations[0].text.strip()
#         if word and word not in words_base:
#             ru_word = translate_word(word)
#             Word.create(
#                 user=user,  # Связываем слово с текущим пользователем
#                 russian_word=ru_word,  # Русское слово
#                 english_word=word,  # Перевод на английский
#                 learned=False,  # Флаг изученности
#                 added_at=datetime.now()  # Время добавления
#             )
#             return word
#         else:
#             return generate_word_for_beginer(callback_query, words_base)  # Если слово повторяется, пробуем снова
#     else:
#         return None
#
#
#
#
#
#
# def generate_word_for_middle(callback_query, words_base):
#     user = User.get(User.user_id == callback_query.from_user.id)
#     # Преобразуем список в строку для запроса
#     excluded_words = ", ".join(words_base) if words_base else "none"
#
#     # Создаем запрос с учетом исключений
#     prompt = (
#         f"Generate an English word from middle vocabulary, for English level B1-B2. The word must be a noun, verb, adjective, or adverb. Do not use any of these words: {excluded_words}."
#     )
#
#     # Запрос к Cohere API
#     response = co.generate(
#         model="command",
#         prompt=prompt,
#         max_tokens=1,
#         temperature=0.9,  # Добавляем случайности
#         k=0,
#         p=0.9
#     )
#
#     # Получаем результат
#     if response.generations:
#         word = response.generations[0].text.strip()
#         if word and word not in words_base:  # Убеждаемся, что слово уникальное
#             ru_word = translate_word(word)
#             Word.create(
#                 user=user,  # Связываем слово с текущим пользователем
#                 russian_word=ru_word,  # Русское слово
#                 english_word=word,  # Перевод на английский
#                 learned=False,  # Флаг изученности
#                 added_at=datetime.now()  # Время добавления
#             )
#             return word
#         else:
#             return generate_word_for_middle(callback_query, words_base)  # Если слово повторяется, пробуем снова
#     else:
#         return None
#
#
#
#
#
#
#
#
# def generate_word_for_professional(callback_query, words_base):
#     user = User.get(User.user_id == callback_query.from_user.id)
#     # Преобразуем список в строку для запроса
#     excluded_words = ", ".join(words_base) if words_base else "none"
#
#     # Создаем запрос с учетом исключений
#     prompt = (
#         f"Generate an English word from professional vocabulary, for English level C1-C2. The word must be a noun, verb, adjective, or adverb. Do not use any of these words: {excluded_words}."
#     )
#
#     # Запрос к Cohere API
#     response = co.generate(
#         model="command",
#         prompt=prompt,
#         max_tokens=1,
#         temperature=0.9,  # Добавляем случайности
#         k=0,
#         p=0.9
#     )
#
#     # Получаем результат
#     if response.generations:
#         word = response.generations[0].text.strip()
#         if word and word not in words_base:  # Убеждаемся, что слово уникальное
#             ru_word = translate_word(word)
#             Word.create(
#                 user=user,  # Связываем слово с текущим пользователем
#                 russian_word=ru_word,  # Русское слово
#                 english_word=word,  # Перевод на английский
#                 learned=False,  # Флаг изученности
#                 added_at=datetime.now()  # Время добавления
#             )
    #         return word
    #     else:
    #         return generate_word_for_professional(callback_query, words_base)  # Если слово повторяется, пробуем снова
    # else:
    #     return None




API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"
def generate_word(callback_query, words_base, level="A1-A2"):
    user = User.get(User.user_id == callback_query.from_user.id)
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
        word = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip().lower()

        # Если слово уже есть в списке (на случай ошибки модели), повторяем вызов
        if word in words_base:
            return generate_word(words_base, level)

        ru_word = translate_word(word)
        Word.create(
            user=user,
            russian_word=ru_word,
            english_word=word,
            learned=False,
            added_at=datetime.now()
        )

        return word

    except requests.exceptions.Timeout:
        return "Error: Request timeout"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
