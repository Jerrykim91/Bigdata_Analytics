# 파일 명 : json01.py
# 폴더 생성 : resources

import json
import cx_Oracle as oci

# 접속하기 (계정/비밀번호@서버주소:포트번호/SID,encoding="utf-8"(인코딩) )
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
# 커서 생성
cursor = conn.cursor()

# 파일 읽기 => 읽을 때도 한글은 인코딩을 해줘야 한다. 
file1 = open('./resources/exam02.json',encoding="utf-8")
# str to dict로 변경 
data1 = json.load(file1)
# {"ID", "aaa", "PW":"34"}

sql = """
INSERT INTO MEMBER(ID, PW, NAME, AGE, JOINDATE)
VALUES(:ID, :PW , :NAME, :AGE, SYSDATE)
"""
# 데이터에 담겨 있는것을 대채하라는 의미 VALUES(:ID, :PW , :NAME, :AGE, SYSDATE)

cursor.execute(sql, data1)
conn.commit()
# json은 사전형 구조 -> 키로 값을 불러온다 

#{'str': 'hello', 'number': 34, 'array': [1, 2, 3, 4, 5], 'object': {'name': 'a', 'age': 23}, 'bool': True}
print(data1)
# <class 'dict'>
print(type(data1))



# https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?utm_source=chrome-ntp-icon