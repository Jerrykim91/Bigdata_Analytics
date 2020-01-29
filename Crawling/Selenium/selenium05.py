# selenium03.py
# 이미지 크롤링하기

from selenium import webdriver
# from bs4 import BeautifulSoup
import urllib.request



options = webdriver.ChromeOptions()
options.add_argument('headless') # 화면 표시 x

# 옵션 설정
options.add_argument("disable-gpu")   # gpu 사용여부 
options.add_argument("lang=ko_KR")    # 언어 선택 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # 윈도우 환경 

# 드라이버 불러오기 - 드라이버팩 경로 설정 주의 
driver = webdriver.Chrome('../data/chromedriver.exe', options= options)
# url 선언 
url = "https://www.melon.com/album/detail.htm?albumId=10376787"
# url 호출 
driver.get(url)

# copy에서 -> selector를 선택 
img = driver.find_element_by_css_selector('#d_album_org > img')
# 이미지 출력 
print(img)


# 찾는 태그중에서 src의 값만 
file = img.get_attribute("src") 
urllib.request.urlretrieve(file, "../data/melon_solar.png") # 다운로드 위치경로 설정 주의 

# 사진 여러장 오면 여러장 출력 ?? => 나는 솔라진을 원한다 지코아니라 이씨 

driver.close()