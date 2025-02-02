import requests
API_KEY = 'dict.1.1.20250127T010434Z.3f513700d5a50e4a.b05539ec97a8b856de1ebb3f30443b593485da94'
def translate_word(word):
    base_url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?'

    response = requests.get(f'{base_url}/lookup', params = {
        'key': API_KEY,
        'lang': 'en-ru',
        'text': word,
        'ui' : 'ru'

    })
    data = response.json()

    # Проверяем, есть ли переводы в ответе
    if 'def' in data and data['def']:
        if 'tr' in data['def'][0] and data['def'][0]['tr']:
            return data['def'][0]['tr'][0]['text']

    return None  # Если перевод не найден
