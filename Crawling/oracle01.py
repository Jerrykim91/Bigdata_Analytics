# pip install cx_oracle 모듈 설치

import cx_Oracle as oci

# 접속하기 (암호)
conn = oci.connect('admin/1234@192.168.99.100:32764/xe')
# 커서 생성
cursor = conn.cursor()

# SELCET
sql = "SELECT * FROM MEMBER"  
cursor.execute(sql)
data = cursor.fetchall() #[(),(),()]
print(data)