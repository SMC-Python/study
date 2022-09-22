import requests

response = requests.get(
    'https://dict.naver.com/search.dict',
    params={
        'dicQuery': '한글',
        'query': '한글',
        'target': 'dic',
        'ie': 'utf8',
        'query_utf': '',
        'isOnlyViewEE': '',
    }
)

with open('./results/result_2-2.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
