# selenium01_01.py

# 드라이버 팩 다운로드 경로 
# https://chromedriver.chromium.org/downloads

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# ChromeOptions()를 만들어 add_argument를 통해 Headless모드인 것과, 크롬 창의 크기, 
# 그리고 gpu를 사용하지 않는 옵션 설정 
options = webdriver.ChromeOptions()
# options.add_argument('headless') # 중요!! 크롬이 Headless모드로 동작하도록 만들어주는 키워드
# 크롬 창의 크기를 직접 지정해 준 이유
# => 일반적으로 노트북,데스크탑에서 사용하는 해상도가 1920x1080이기 때문
options.add_argument('window-size=1920x1080')



# 드라이버 가지고 오기 
driver = webdriver.Chrome('./data/chromedriver.exe', chrome_options= options)

# 드라이버에 진입할 경로 전달
driver.get("http://ihongss.com/webboard")
# 원하는 페이지 개발자 모드에서 위치를 검색 
# name이 email인것을 찾아서 다음값을 넣는 스크립트



# driver.find_element_by_name("email").send_keys('20191216') 
driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
# by_name("html의 name값").send_keys(원하는값)
driver.find_element_by_name("pw").send_keys('20191216')
# by_css_selector('#포함!! copy selector한값').click() 
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click() 



# pop창 띄우기 
time.sleep(3)
driver.execute_script('alert("hello")')


# driver.get("http://daum.net") # 로그인 이후의 페이지
# html    = driver.page_source
# soup    = BeautifulSoup(html, 'html_parser')
# driver.close()


# driver.find_element_by_xpath('//*[@id="form1"]/div[3]/input')
