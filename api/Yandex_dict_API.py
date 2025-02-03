import requests
API_KEY = 'dict.1.1.20250203T002223Z.72ad9c37a7fa5fa5.3e0290bb5a5dee6a7de40dd7b19ce157400e7249'
def translate_word(word):
    base_url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'

    response = requests.get(f'{base_url}', params = {
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
