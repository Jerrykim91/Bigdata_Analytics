# selenium02_01.py
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1920x1080')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./data/chromedriver.exe', chrome_options=options)

driver.get("https://music.bugs.co.kr/")

rank2 = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/article/section[3]/div/div[1]/div/table/tbody/tr/th/p/a')
# for i in rank2:
#     print(i.text)

rank3 = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/article/section[3]/div/div[1]/div/table/tbody/tr')
for i in rank3:
    li = i.text.split("\n")
    print(li[0],li[2],li[3])
