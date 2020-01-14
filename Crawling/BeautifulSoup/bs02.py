# bs01.py

from bs4 import BeautifulSoup
import requests

# 데이트를 얻고자 하는 사이트 
url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
# 긁어오기 
str = requests.get(url)
# print(str.text) # 데이터 확인 

soup = BeautifulSoup(str.text, 'html.parser')
all_div_tit3 = soup.find_all('div',{"class":"tit3"})



for tmp in all_div_tit3:
    # print(tmp) #=> 출력하면 아래 div의 class가 tit3인 아이를 전부 출력 
    # <div class="tit3">
    # <a href="/movie/bi/mi/basic.nhn?code=122527" title="캡틴 아메리카: 시빌 워">캡틴 아메리카: 시빌 워</a>
    # </div>

    # print(tmp.find('a').text) # 클래스 안에 있는 text를 출력 
    print(tmp.find('a').attrs) # 클래스 안에 있는 속성을 출력 
    # {'href': '/movie/bi/mi/basic.nhn?code=85579', 'title': '신과함께'}

print('===end','='*30)

txt = """
soup = BeautifulSoup(str.text, 'html.parser')
all_div_tit3 = soup.find_all('div')

이렇게 출력하면 문자열에 'a'가 포함된 아이들은 전부 출력 
for tmp in all_div_tit3:
    print(tmp.find('a').text)
"""
print(txt)