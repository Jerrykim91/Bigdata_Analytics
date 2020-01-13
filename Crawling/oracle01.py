# pip install cx_oracle 모듈 설치

import cx_Oracle as oci

# 접속하기 (계정/비밀번호@서버주소:포트번호/SID,encoding="utf-8"(인코딩) )
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
# 커서 생성
cursor = conn.cursor()

# SELCET
sql = "SELECT * FROM MEMBER"  
cursor.execute(sql)
data = cursor.fetchall() #[(),(),()]
print(data)


sql = """
INSERT INTO MEMBER(ID, PW, NAME, AGE, JOINDATE)
VALUES(:1, :2 , :3, :4, SYSDATE)
"""

arr = ['a1', 'a1', '홍길동', 33] 
cursor.execute(sql, arr)
conn.commit()