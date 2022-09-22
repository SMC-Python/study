import requests

title = input('제목을 입력하세요: ')
content = input('내용을 입력하세요: ')

response = requests.post(
    'https://controlc.com/index.php',
    params={
        'act': 'submit',
    },
    data={
        'subdomain': '',
        'antispam': '1',
        'website': '',
        'paste_title': title,
        'input_text': content,
        'timestamp': '3b990af196ec6a638a8ca3e7d3eb62c6',
        'paste_password': '',
        'code': '0',
    },
    headers={
        'referer': 'https://controlc.com/',
    },
)

with open('./results/result_3-2.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
