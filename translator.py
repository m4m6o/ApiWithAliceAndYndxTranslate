import requests

def translate_word(word):
    try:
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        api_key = 'trnsl.1.1.20190424T103559Z.9f2d465a6cd6fbc9.4b01888932093a717a28c85cd5085f727142bd90'
        params = {
            'key': api_key,
            'text': word,
            'lang': 'ru-en',
            'format': 'plain'
        }
        response = requests.get(url, params)
        json = response.json()
        return json['text'][0]
    except Exception as e:
        return e
    