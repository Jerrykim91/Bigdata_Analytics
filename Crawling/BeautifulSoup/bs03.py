# bs03.py
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

# 실습(내가 원하는 사이트에서 데이터 가지고 오기 )
from bs4 import BeautifulSoup
import requests

# 데이트를 얻고자 하는 사이트 
url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str = requests.get(url)
# print(str.text) # 데이터 확인 

soup = BeautifulSoup(str.text, 'html.parser')
#all_div_tit3 = soup.find_all('div',{"class":"tit3"})






for tmp in all_div_tit3:
    # print(tmp)
    print(tmp.find('a').attrs) # 클래스 안에 있는 속성을 출력 

print('===end','='*30)
