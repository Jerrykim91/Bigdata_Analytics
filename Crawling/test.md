# test

---

```py

# <a href="#", id="aaa">가나다</a>
# <span abc ="1">가나다></span>

print(tmp.find('span').text)  # 클래스 안에 있는 text를 출력 
print(tmp.find('span').attrs) # 클래스 안에 있는 속성을 출력 

```

---

```py

# json 경로 변수에 담기  
url = "http://ihongss.com/json/exam2.json"
# requests.get(url).text
str1 = requests.get(url).text
# 타입 변경 
# 파일에서 가져오는거 load, 여기서는 loads
data1 = json.loads(str1) # str -> dict

```
---

```py
# html 문서 검색

# 여러개의 해당 태그찾기 
soup.find_all()
# 첫번재 태그찾기 
soup.find()
# 여러개의 해당 태그검색 
soup.select()

```
---

```py
# 자바스크립트를 수행시키는 명령어 
driver.execute_script()
find_element_by_id().click()

# s의 여부 중요 
find_element_by_  # 한개 요소
find_elements_by_ # 여러개 요소 

# 스크립트 제어 
# 키보드, 마우스, 화면 제어 가능 
# 내용을 지우는 것, 제거하는것은 안됨 

# a = {"ret": {"bbb" : [13,45]}}
# a["ret"]["bbb"][0] => 13 출력 

# a = [{ "ret": 0 }, { "ret" : 1 },{ "ret": 3 }}]
# a[2]["ret"] => 1 출력 
```

---

```sql
-- DML 
-- 데이터 
insert , update, delete, select

```
---

```xml
<!-- xml -->
<!-- 파싱할때 속성  -->
xml  : attrib 
html : attrs

```

```py
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

```