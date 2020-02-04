# bs02_03.py
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

# 실습(내가 원하는 사이트에서 데이터 가지고 오기 - 빌보드)
from bs4 import BeautifulSoup
import requests

# 데이트를 얻고자 하는 사이트 
url = "https://www.billboard.com/charts/hot-100"

str = requests.get(url)
# print(str.text) # 데이터 확인 

soup = BeautifulSoup(str.text, 'html.parser')
# 순서대로 하자 
# 1. 상위부터 전부 출력 
all_h3 = soup.find_all("h3")
# 변수 
chart_name = ("button",{"class":"chart-highlights__item__artist display--block font--semi-bold text--"})
all_chart_name = soup.find_all(chart_name)


for tmp in all_chart_name:
    print('='*30)
    print(tmp.text)
    #print(tmp)

print('===end','='*30)


"""
99
New


Slow Dance In A Parking Lot
Jordan Davis

-
- Last Week
99 Peak Rank
1 Weeks on Chart



-
99
1

"""
