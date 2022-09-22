from bs4 import BeautifulSoup

with open('./4. 응답결과에서 원하는 정보 추출하기/4-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print('제목: ', soup.select_one('#title').get_text())
print('부제목: ', soup.select_one('#sub-title').get_text())
print('첫번째 내용: ', soup.select_one('#content').get_text())
print('두번째 내용: ', soup.select_one('#content-box > p:nth-child(2)').get_text())
