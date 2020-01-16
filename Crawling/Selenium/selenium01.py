# selenium01.py
# 드라이버 팩 다운로드 경로 
# https://chromedriver.chromium.org/downloads

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080') # ?? 
# options.add_argument('headless')            # 창이 없는, 화면에 출력 안됨 

# 드라이버 가지고 오기 
driver = webdriver.Chrome('./data/chromedriver.exe', chrome_options= options)
# 드라이버에 진입할 경로 전달
driver.get("http://ihongss.com/webboard")

# 드라이버로 아이디와 비밀번호 전달 => 아이디, 패스워드 입력 
driver.find_element_by_name("email").send_keys('20191216')
driver.find_element_by_name("pw").send_keys('20191216')
# 진입 
driver.find_element_by_css_selector('#form1 > div:nth-child(4)> input').click()

# driver.find_element_by_xpath('//*[@id="form1"]/div[3]/input')

# 작업 완료후 다음 메인 출력 
driver.get("http://daum.net") # 로그인 이후의 페이지
html = driver.page_source
soup = BeautifulSoup(html,'html_parser')