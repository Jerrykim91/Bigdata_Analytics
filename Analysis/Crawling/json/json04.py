# 파일 명 : json04.py
# 폴더 생성 : resources
# 몽고디비 이용
# json은 사전형 구조 -> 키로 값을 불러온다 

import requests
import json
import pymongo 

# 접속하기 (서버주소,포트번호,encoding="utf-8"(인코딩))
conn  = pymongo.MongoClient('192.168.99.100',32766)
db    = conn.get_database("db1") # 디비 생성 없으면 생성 있으면 가져오기 
table = db.get_collection("exam4") # collection 생성 
print('--'*40)

url = "http://ihongss.com/json/exam4.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict

# insert_one({})
# insert_many([{},{},{}])

for tmp in data1 : 
    # {'name': 'AAA', 'species': 'cat', 'foods': {'likes': ['tuna', 'catnip'], 'dislikes': ['ham', 'zucchini']}}
    # print(tmp)
    # #AAA ,BBB CCC
    # print(tmp['name']) # { , } 
    # #cat, dog, cat
    # print(tmp['species'])
    # # {'likes': ['tuna', 'catnip'], 'dislikes': ['ham', 'zucchini']}
    # print(tmp['foods']) 
    #likes => 처음꺼 출력 
    # print(tmp['foods']['likes'][0]) 
    # # dislikes => 처음꺼 출력 
    # print(tmp['foods']['dislikes'][0]) 

    dict1 = dict()
    dict1['name']     = tmp['name']
    dict1['species']  = tmp['species']
    dict1['likes']    = tmp['foods']['likes'][0]
    dict1['dislikes'] = tmp['foods']['dislikes'][0]

    table.insert_one(dict1)

# print('--'*40)
# print(type(data1)) 
# print(data1)
# print('--'*40)
