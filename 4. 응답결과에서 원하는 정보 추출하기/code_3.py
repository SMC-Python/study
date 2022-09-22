from bs4 import BeautifulSoup

with open('./4. 응답결과에서 원하는 정보 추출하기/4-3.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

url = soup.select_one('#wrapper > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > form > input')
print('내용: ', url.attrs['value'])
