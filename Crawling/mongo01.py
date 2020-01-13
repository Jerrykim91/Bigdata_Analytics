# mongo01.py
# pip install pymongo
import pymongo 

conn  = pymongo.MongoClient('192.168.99.100',32766)
db    = conn.get_database("db1") # 디비 생성 없으면 생성 있으면 가져오기 

table = db.get_collection("table1") # collection 생성 
dict1 = {"id":"a","age":35}


#table.insert_one(dict1) # 추가하기

data1 = table.find()
for tmp in data1 :
    print(tmp)
    print(type(tmp))
conn.close()
# print(conn)

# 수행할때 마다 테이블이 생성되는 이유는 몽고디비에서 자동으로 기본키를 생성 