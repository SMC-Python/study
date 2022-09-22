import requests

response = requests.get('https://www.naver.com')

with open('./results/result_2-1.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
