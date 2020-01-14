# 파일 명 : json02.py
# 폴더 생성 : resources
# json은 사전형 구조 -> 키로 값을 불러온다 

import requests
import json

# json 경로 변수에 담기  
url = "http://ihongss.com/json/exam2.json"

# requests.get(url).text
str1 = requests.get(url).text

print(type(str1)) # <class 'str'>
print(str1)


# 타입 변경 
# 파일에서 가져오는거 load, 여기서는 loads
data1 = json.loads(str1) # str -> dict
print(type(data1)) # <class 'str'>
print(data1)

ret = data1['ret']
#ret1 = data1['ret1']

print(type(ret)) # <class 'dict'>
print(ret)

