# selenium01_00.py
# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("http://ihongss.com/webboard")

driver.get("http://daum.net") # 로그인 이후의 페이지
html = driver.page_source
soup = BeautifulSoup(html, 'html_parser')
