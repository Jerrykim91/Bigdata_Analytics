# import
import urllib.request 
import requests
import json, datetime, time
import pandas as pd 


movieDate = time.strftime('%Y%m%d',time.localtime(time.time()))
# print(movieDate)
# 날짜 지정 
movieDate = 20200130

url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=66e652e1d2656b42f10d93c91e0295e4&targetDt={movieDate}"

request = urllib.request.Request(url)
# print(request)
response = urllib.request.urlopen(request)
# print(response)
res = response.getcode()
# print(res)

# 접속 확인 
if(res == 200):
    responseData = response.read()
    # data = json.load(responseData)
else: 
    print('접속 불가',responseData)

# 
# str = requests.get(url).text
# data = json.loads(str)
# print(data)

# json 불러오기 
result = json.loads(responseData)
pre_result = result["boxOfficeResult"]
# print(pre_result)

# 주요 데이터 
movie_Data = pre_result['dailyBoxOfficeList']
# print(movie_Data)
# print(len(movie_Data)) # 10
# <class 'list'>

print('='*100)

# 데이터 뽑아 내기 
cine = [{}]
#print(range(0,len(movie_Data)))# >>> range(0, 10)

# 날짜, 영화 이름, 누적 관객수 
for i in range(0, len(movie_Data)):
    # 요청인터페이스(targetDt) => 조회하고자 하는 날짜를 yyyymmdd 형식으로 입력
    movie_Data[i]['targetDt'] = movieDate    
    cine.append((movie_Data[i]))
# print(cine)

# df = pd.DataFrame(cine)
# df = df[1:]
# print(df)

# 반복 함수 마지막에 날짜를 줄이는 함수를 사용한다. 
# str -> date 
datetime_obj = datetime.datetime.strptime(str(movieDate), "%Y%m%d")
# print(datetime_obj) # >>> 2020-01-30 00:00:00
# 1주일 씩 시간을 줄여간다.
# timedelta 객체는 두 날짜나 시간의 차이인 기간을 나타냅니다.
datetime_obj_tmp = datetime_obj - datetime.timedelta(days=1)
# datetime_obj_tmp = datetime_obj - datetime.timedelta(weeks=1)


# date -> str 변경 
day = datetime_obj_tmp.strftime("%Y-%m-%d").split('-')
movieDate = day[0]+day[1]+day[2]
print(movieDate)

df = pd.DataFrame(cine)
df = df[1:]
print(type(df))
# print(df[1:])
print(df)
df.to_csv("cine.csv", index=False)