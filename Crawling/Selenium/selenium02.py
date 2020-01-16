# selenium02.py
# 스크립트 페이지에서 크롤링하기

from selenium import webdriver
from bs4 import BeautifulSoup
import time



options = webdriver.ChromeOptions()
options.add_argument('headless') 


options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36') 


driver = webdriver.Chrome('./data/chromedriver.exe', options= options)
driver.get("http://digital.kyobobook.co.kr/digital/ebook/ebookMain.ink")


# 5초 스크립트 정보가져오도록 기다리기
time.sleep(5) 
tag = driver.find_element_by_class_name('list') \
    .find_elements_by_tag_name("div")

for tmp in tag:
    print(tmp.text.split("\n")) 