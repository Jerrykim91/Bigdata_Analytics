# bs02_01.py
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

# 실습(내가 원하는 사이트에서 데이터 가지고 오기 - 국내증시)
from bs4 import BeautifulSoup
import requests

# 데이트를 얻고자 하는 사이트 
url = "https://finance.naver.com/sise/sise_quant.nhn"

str = requests.get(url)
# print(str.text) # 데이터 확인 

soup = BeautifulSoup(str.text, 'html.parser')
#all_spen1 = soup.find_all('td',{"class":"title"})
all_a = soup.find_all("a",{"class":"tltle"})


for tmp in all_a:
    print(tmp.text)
    #print(tmp)

print('===end','='*30)
