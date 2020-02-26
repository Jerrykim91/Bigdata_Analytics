# 코드정리- 1
## 코드+ 주석
---

### Review_before_coding
```py
# Review_before_coding - 돌아보기 

# 데이터 수집 
# 위키피디아를이용 => 스크래핑 수준이면 처리가 가능


sample = '''
https://ko.wikipedia.org/wiki/방탄소년단
https://en.wikipedia.org/wiki/BTS_(band)
https://fr.wikipedia.org/wiki/BTS_(groupe)

'''
# print(sample)

# 위 3가지 방법을 이용해서 검색이가능하다 
# 겹치않는 코드만 확인해 보자면 일단은 국가코드와 검색 내용
# 그외의 내용은 모두 겹친다 => 'https://'국가코드'.wikipedia.org/wiki/'내용'

# 일단 하나의 사이트에서 처리루틴을 정의해보자 (미국위키를 전제로)

target_url = 'https://en.wikipedia.org/wiki/BTS_(band)'
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 참고 
# 고용량 파서인 html5lib 사용 

# 웹 스크래핑 관련 모듈 
# 통신담당 : reguest
# 파싱담당 : BS4, html5lib parser 사용
# (파서 선정이유 속도가 중요한게 아니라, 정확한 처리*가 중요)

import urllib.request as rq 
from bs4 import BeautifulSoup

# 요청 
res = rq.urlopen(target_url)
# 파싱 
soup = BeautifulSoup(res,'html5lib')

# print(type(soup), soup)

# 대상 태그를 모은다 
ps = soup.select('#mw-content-text p')
print(len(ps),type(ps))

# 뽑아 내기 
tmp = [ p.text.strip() for p in ps]

print(len(tmp))

# 리스트에 존재하는 문자열들을 한개의 문자열로 통합 => join을 이용 
src_text = ' '.join(tmp)
# src_text
print(len(src_text),src_text[:])


# 정규식 
import re

# p = re.compile('')
# p.sub('', src_text)
# tmp[:10]


# 알파벳만 남겨라 
# ^ :이외에
p = re.compile('[a-zA-Z ]*') 
tmp = p.sub( '' ,  src_text )
tmp.lower()[:100]


```

---


### Translation_ language detection
```py
# 파일 리스트 획득
import glob

# 파일 목록 보기 =>  파일명 전부 확득  
path = './input/train/*.txt'
file_list = glob.glob(path)
print(file_list[:2], len(file_list))

# 오름차순으로 나열 
print(file_list.sort())

```