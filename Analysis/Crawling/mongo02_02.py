# mongo02_01.py
import pymongo
import cx_Oracle as oci

conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn_o.cursor()

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db2")
coll = db.get_collection("p20200115")

data1 = coll.find({},{'_id':False}) # id값 빼기
# data1 = coll.find()

for tmp in data1:
    print(tmp)
    sql = """
        INSERT INTO TABLE1(NO, ID, NAME, AGE)
        VALUES(SEQ_TABLE1_NO.nextval, :id, :name, :age)
    """
    cursor.execute(sql, tmp)
    conn_o.commit()

conn_o.close()      # 오라클 연결 끊기
conn.close()        # 몽고DB 연결 끊기