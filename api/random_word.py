import requests

API_KEY = "ab7cojl572571svk6ui28hk7hye21jzfruphyokp27rxxvcb7"
URL = "https://api.wordnik.com/v4/words.json/randomWords"


def get_random_words(count=3):
    try:
        params = {
            "limit": count,
            "api_key": API_KEY
        }
        response = requests.get(URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        words = [word_info["word"].strip().lower() for word_info in data]
        return words
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

