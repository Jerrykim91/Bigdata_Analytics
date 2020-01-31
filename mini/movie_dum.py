import urllib.request as ul
# import requests
import json, datetime, time
import pandas as pd 




movieDate = time.strftime('%Y%m%d',time.localtime(time.time()))
print(movieDate)
movieDate = 20200130

url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=66e652e1d2656b42f10d93c91e0295e4&targetDt={movieDate}"
request = ul.Request(url)
print(request)
response = ul.urlopen(request)
print(response)
res = response.getcode()
print(res)

if(res == 200):
    responseData = response.read()

request = ul.Request(url)
print(request)
# ===== 동작 




# 어떤 데이터를 가지고 와서 보여줄지  


pre_result1 = pre_result["dailyBoxOfficeList"]
print(pre_result1)

cine = [{}]
# 날짜, 영화 이름, 누적 관객수 
for i in range(0,len(pre_result1)):
    pre_result1[i]['targetDt'] = movieDate
    cine.append(pre_result1[i])
print(cine)

# 반복 함수 마지막에 날짜를 줄이는 함수를 사용한다 
# str = > date 
datetime_obj = datetime.datetime.strptime(str(movieDate),"%Y%m%d").date()
# 1주일씩 시간을 줄여 간다. 
datetime_obj_tmp.strftime("%Y-%m-%d").split('-')
movieDate = day[0]+day[1]+day[2]
# time.seep(1)
print(movieDate)
# print(cine)

dataFrame=pd.DataFrame(cine)
# 첫행이 비어있음 
dataframe = dataFrame[1:]
print(dataframe.head())
dataframe.to_csv("cine.csv")


# 함수화 
def info():
    movieDate = time.strftime('%Y%m%d',time.localtime(time.time()))
    print(movieDate)
    cine=[{}]
    # whille int(movieDate)//10000 != 2018:
    for i in range(0,30):
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=66e652e1d2656b42f10d93c91e0295e4&targetDt={movieDate}"
        request = ul.Request(url)
        print(request)


