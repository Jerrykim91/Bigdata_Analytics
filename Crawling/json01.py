# 파일 명 : json01.py
# 폴더 생성 : resources

import json

file1 = open('./resources/exam01.json')
# str to dict로 변경 
data1 = json.load(file1)


#{'str': 'hello', 'number': 34, 'array': [1, 2, 3, 4, 5], 'object': {'name': 'a', 'age': 23}, 'bool': True}
print(data1)
# <class 'dict'>
print(type(data1))
