# selenium03.py
# 이미지 크롤링하기

from selenium import webdriver
# from bs4 import BeautifulSoup
import urllib.request
import time
import os
from selenium.webdriver.common.keys import Keys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = os.path.join(BASE_DIR, 'data')
# print(os.path.join(BASE_DIR, 'data'))
# print(os.path.join(BASE_DIR,'파일 이름'))


options = webdriver.ChromeOptions()
# options.add_argument('headless') # 화면 표시 x

# 옵션 설정
options.add_argument("disable-gpu")   # gpu 사용여부 
options.add_argument("lang=ko_KR")    # 언어 선택 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # 윈도우 환경 

# 드라이버 불러오기 - 드라이버팩 경로 설정 주의 
driver = webdriver.Chrome(os.path.join(BASE_DIR, 'data','chromedriver.exe'), options= options)
# url 선언 => 원하는 url 긁어 오기 
url = "https://www.google.com/"
# url 호출 
driver.get(url)

# 네이버 검색창에 검색어 입력 
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('강아지')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# 이미지 창 클릭 
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()
img = driver.find_element_by_xpath('//*[@id="GdjdK7ot_diCBM:"]')

print(img)



# link = [] 
# for i in range(1,5,1) :
#     try : 
#         img = driver.find_element_by_xpath('//*[@id="irc-ss"]/div[2]/div[1]/div['+ str(i)+']/a[1]/img')
#     except:
#         img =  driver.find_element_by_xpath('//*[@id="irc-ss"]/div[2]/div[2]/div['+ str(i)+']/a[1]/img')
#     print(img)   

    #link.append(img. get_attribute("src"))




# //*[@id="GdjdK7ot_diCBM:"]
# //*[@id="G8QTWFTxAUNcLM:"]
# //*[@id="HghtUB4eNpBa1M:"]
# //*[@id="SRH01WubjDRbaM:"]

# #파일명 n0.jpg  n1.jpg, n2.jpg, n3.jpg, n4.jpg
# for idx , tmp in enumerate(link):
#     urllib.request.urlretrieve( tmp, './data/'+'n'+ str(idx)+'.jpg')

# 테스트용 
# time.sleep(2) 

# 종료
driver.close()