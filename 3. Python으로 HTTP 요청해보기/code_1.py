import requests

response = requests.post(
    'https://controlc.com/index.php',
    params={
        'act': 'submit',
    },
    data={
        'subdomain': '',
        'antispam': '1',
        'website': '',
        'paste_title': '제목',
        'input_text': '내용',
        'timestamp': '3b990af196ec6a638a8ca3e7d3eb62c6',
        'paste_password': '',
        'code': '0',
    },
    headers={
        'referer': 'https://controlc.com/',
    },
)

with open('./results/result_3-1.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
