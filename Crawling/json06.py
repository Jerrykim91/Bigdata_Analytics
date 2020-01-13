# 파일 명 : json06.py => exam 21(실습 )
# 폴더 생성 : resources - 몽고디비 이용
# 날짜 이름 개봉일 

# import 
# 뭐뭐 인포트 해야하나 
import requests as rq
import pymongo 
import json

# 몽고디비에 접속 
conn = pymongo.MongoClient('192.168.99.100',32766)
# 디비 생성
db = conn.get_database("db1") 
# 테이블 생성 => 컬렉션 생성 
table = db.get_collection("exam21") 

txt = """
0. showRange,
dailyBoxOfficeList{
    1. rankOldAndNew,
    2. movieNm,
    3. salesShare,
    4. salesAcc,
    5. scrnCnt,
    6. showCnt
    }
출력 !! 
"""

print('-'*40)
print(txt)
print('-'*40)

# url 불러오기 
url = "http://ihongss.com/json/exam21.json"
str1 =rq.get(url).text
# 타입 변경(str -> dict)
data = json.loads(str1)
# ['boxOfficeResult']['dailyBoxOfficeList']
data1 = json.loads(str1)['boxOfficeResult']['dailyBoxOfficeList']  


# 타입 출력 해보기 
# print(data)
print(type(data)) # dict로 바뀐거 확인 
print('-'*20,'Checkpoint2','-'*20)


# 일단 for 문 돌려보자 
for tmp in data['boxOfficeResult'] :
    # print(tmp['showRange'])
    # print(tmp['dailyBoxOfficeList'])
    print(tmp[boxofficeType])
    # print(tmp[])
    # print(tmp[])
