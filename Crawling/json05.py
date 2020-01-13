# 파일 명 : json05.py => exam 10(실습 )
# 폴더 생성 : resources - 몽고디비 이용

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
table = db.get_collection("exam10") 

print('-'*20,'start point','-'*20)

# url 불러오기 = json 경로 변수에 담기  
url = "http://ihongss.com/json/exam10.json"
# 텍스트 형의 json을 sty1에 담는다 
str1 =rq.get(url).text
# 타입 변경(str -> dict)
data = json.loads(str1)
data1 = json.loads(str1)['data']

# 타입 출력 해보기 
# print(data1)
# print(type(data1)) # dict로 바뀐거 확인 

# print('-'*20,'Checkpoint1','-'*20)
# print(data1['data'])
# print('-'*20,'Checkpoint1','-'*20)
# print(data1['ret'])
# print('-'*20,'Checkpoint','-'*20)

# data = data1['data']
# print(data)
# print('-'*20,'Checkpoint','-'*20)

# 일단 for문 돌려보자 
for tmp in data1:
    # print('-'*20,'Checkpoint1','-'*20)
    # print(tmp)
    # print(tmp['id'])
    # print(type(tmp['id']))
    # print(tmp['name'])
    # print(tmp['age'])
    # print(tmp['score'])
    # print('-'*20,'Checkpoint2','-'*20)
    # print(tmp['score']['math'])
    # print('-'*20,'Checkpoint2','-'*20)

    dict1 = dict()
    dict1['id']   = tmp['id']
    dict1['name'] = tmp['name']
    dict1['math'] = tmp['score']['math']
    dict1['eng']  = tmp['score']['eng']
    dict1['kor']  = tmp['score']['kor']

    table.insert_one(dict1)

print('done')

    # soc = tmp['score']
    # print(soc)


