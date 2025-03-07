import requests

API_KEY = "ab7cojl572571svk6ui28hk7hye21jzfruphyokp27rxxvcb7"
URL = "https://api.wordnik.com/v4/words.json/randomWords"

def get_random_words(count=3):
    """
    Запрашивает случайные английские слова с API Wordnik.

    :param count: Количество слов для запроса (по умолчанию 3).
    :return: Список случайных слов в нижнем регистре или None в случае ошибки.
    """
    try:
        params = {
            "limit": count,
            "api_key": API_KEY
        }
        response = requests.get(URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        return [word_info["word"].strip().lower() for word_info in data]
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к Wordnik API: {e}")
        return None
