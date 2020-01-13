# 파일 명 : json02.py
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

"""
{
    'ret' : {'id': "a", 'name': "123", 'age': 34},
    'ret1': {'id': "a", 'name': "123", 'age': 36}
}
"""

# json 경로 변수에 담기  
url = "http://ihongss.com/json/exam2.json"
# ret 안에 딕셔너리 

# requests.get(url).text
str1 = requests.get(url).text
print(str1)
print(type(str1)) #<class 'str'>
print('--'*40)


# 타입 변경 -> dict
# 파일에서 가져오는거 load, 여기서는 loads
data1 = json.loads(str1) # str -> dict
print(data1)
print('data1', type(data1)) #<class 'dict'>

ret = data1['ret']
ret1 = data1['ret1']

print(ret)
#print(type(box)) #<class 'dict'>
print('--'*40)


# 타입 변경 완료 
# {'ret': {'id': 'a386', 'name': '123', 'age': 34}, 'ret1': {'id': 'a383', 'name': '123', 'age': 36}}
# <class 'dict'>


for tmp in data1 :
    print(tmp)
    print(type(tmp))

    sql = """
    INSERT INTO MEMBER(ID, PW, NAME, AGE, JOINDATE)
    VALUES(:ID,'1234', :NAME, :AGE, SYSDATE)
    """
    cursor.execute(sql,tmp)    
    
#conn.commit()

# print(type(ret)) # <class 'dict'>
# print(ret)

# 수집하는 디비는 기본키를 사용하면 안된다 
# => 예) id 값이 동일해서 충돌이 일어난다. 