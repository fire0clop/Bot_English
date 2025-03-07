import requests

API_KEY = "dict.1.1.20250203T002223Z.72ad9c37a7fa5fa5.3e0290bb5a5dee6a7de40dd7b19ce157400e7249"
BASE_URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"

def translate_word(word):
    """
    Переводит английское слово на русский с помощью Yandex Dictionary API.

    :param word: Английское слово для перевода.
    :return: Перевод слова на русский или None, если перевод не найден.
    """
    try:
        response = requests.get(BASE_URL, params={
            "key": API_KEY,
            "lang": "en-ru",
            "text": word,
            "ui": "ru"
        }, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("def") and data["def"][0].get("tr"):
            return data["def"][0]["tr"][0]["text"]

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к Yandex Dictionary API: {e}")

    return None
