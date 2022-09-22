from bs4 import BeautifulSoup

with open('./4. 응답결과에서 원하는 정보 추출하기/4-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

content_list = soup.select('#content-box > ul > li')

for content in content_list:
    print('내용: ', content.get_text())
