# 파일 명 : json03.py
# 폴더 생성 : resources
# json은 사전형 구조 -> 키로 값을 불러온다 

import requests
import json
import cx_Oracle as oci

# 접속하기 (계정/비밀번호@서버주소:포트번호/SID,encoding="utf-8"(인코딩) )
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
# 커서 생성
cursor = conn.cursor()
print('--'*40)

url = "http://ihongss.com/json/exam3.json"
# ret 안에 딕셔너리 

str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict

# data1 = {ret:[{},{},{}], ret1:[{},{},{}]}
ret = data1['ret'] # ret:[{},{},{}] => [a,b,c]

for tmp in ret : 
    print(tmp) # {} => 3번 수행 
    # sql = """
    # INSERT INTO MEMBER(ID, PW, NAME, AGE, JOINDATE)
    # VALUES(:ID,'1234', :NAME, :AGE, SYSDATE)
    # """
    # cursor.execute(sql, tmp)

print('--'*40)
print(type(ret)) 
print(ret)
print('--'*40)
