# 파일 명 : json06.py => exam 21(실습 )
# 폴더 생성 : resources - 몽고디비 이용
# 날짜 이름 개봉일 

# import 
# 뭐뭐 인포트 해야하나 
import requests, pymongo, json


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
str1 = requests.get(url).text
# 타입 변경(str -> dict)
data = json.loads(str1)
# ['boxOfficeResult']['dailyBoxOfficeList']
# 내가 원하는 데이터는 showRange 데이터 값을 출력 
# dailyBoxOfficeList 안의 데이터를 출력 
data1 = json.loads(str1)['boxOfficeResult']['dailyBoxOfficeList']  
data2 = json.loads(str1)['boxOfficeResult']
data3 = json.loads(str1)['boxOfficeResult']['showRange']

# 타입 출력 해보기 
# print(type(data2)) # dict로 바뀐거 확인 



# 일단 for 문 돌려보자 
for tmp in data2['dailyBoxOfficeList'] :
    # print(tmp['showRange'])
    # print(tmp['dailyBoxOfficeList'])
    # print(tmp['boxofficeType'])
    print('-'*20,'Checkpoint3','-'*20)

#     print(tmp)
#     print(tmp['rankOldAndNew'])
#     print(tmp['movieNm'])
#     print(tmp['salesShare'])
#     print(tmp['salesAcc'])
#     print(tmp['scrnCnt'])
#     print(tmp['showCnt'])

# print('finish')    
# print(data2['showRange'])

    dict1 = dict()
    dict1['showRange'] =  data2['showRange']
    dict1['rankOldAndNew'] = tmp['rankOldAndNew']
    dict1['movieNm'] = tmp['movieNm']
    dict1['salesShare'] = tmp['salesShare']
    dict1['salesAcc'] = tmp['salesAcc']
    dict1['scrnCnt'] = tmp['scrnCnt']
    dict1['showCnt'] = tmp['showCnt']

    table.insert_one(dict1)
    # 1. rankOldAndNew,
    # 2. movieNm,
    # 3. salesShare,
    # 4. salesAcc,
    # 5. scrnCnt,
    # 6. showCnt