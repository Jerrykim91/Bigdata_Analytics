# csv01.py => 확인 
import pymongo, csv 

conn  = pymongo.MongoClient('192.168.99.100',32766)
db    = conn.get_database("db1") # 디비 생성 없으면 생성 있으면 가져오기 
coll = db.get_collection("exam1") # collection 생성 

f = open('./resources/exam1.csv', 'r', encoding="utf-8")
rdr = csv.reader(f)

next(rdr, None) # 컬럼 skip

for line in rdr :
    print(type(line))
    print(line)
    dict1 = dict()
    dict1[line[0]] = line
    coll.insert_one(dict1)

conn.close()