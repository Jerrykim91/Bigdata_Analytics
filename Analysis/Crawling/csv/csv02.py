# csv01.py => 확인 
import pymongo, csv 
#  판다스 
import pandas as pd

#csv는 구분자 , \t
# delimiter 구분 문자 
df = pd.read_csv('./resources/exam1.csv', 'r', delimiter=",")
print(df)
print('='*40)

# NaN 제거 : 결측치 제거 
df = df.dropna() 
print(df)

print('='*40)
# DF -> list 변경 
list1 = df.values.tolist() 
print(list1)

print('='*40)
# DF -> dict로 변경 
dict1 = df.to_dict() 
print(dict1)
print('='*40)