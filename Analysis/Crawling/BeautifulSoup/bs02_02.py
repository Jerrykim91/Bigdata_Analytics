# bs02_02.py
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

# 실습(내가 원하는 사이트에서 데이터 가지고 오기 - 환률)
from bs4 import BeautifulSoup
import requests

# 데이트를 얻고자 하는 사이트 
url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

str = requests.get(url)
# print(str.text) # 데이터 확인 

soup = BeautifulSoup(str.text, 'html.parser')
# 순서대로 하자 
# 1. 사위 부터 전부 출력 
all_h3 = soup.find_all("h3")
# 변수 
h3_class = ("h3",{"class":"h_lst"})
all_h3_class = soup.find_all(h3_class)


for tmp in all_h3_class:
    print(tmp.text)
    #print(tmp)

print('===end','='*30)
