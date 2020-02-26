# 코드정리- 1
## 코드+ 주석
---


### Translation_ language detection - 함수화
```py

#  함수화 1
# 1. 파일 리스트 획득
import glob
import os, re

try:
    path = './input/train/*.txt'
    file_list = glob.glob(path)
    print('정상작동',file_list)
except Exception as e :
    print('에러발생', e)

# get_data() 함수 
def get_data(file_path):

    # 2. 언어 코드 확득 file_path
    base_name = os.path.basename(file_path)
    # 정규식 사용 
    p = re.compile('^[a-z]{2}')
    lng_code = p.match(base_name).group()


    # 3. 파일을 열면서 정규화
    try:
        with open( file_path, encoding='utf-8') as f :
            # 두번째 정규식 
            text = f.read().lower() # 소문자로 바꿔서 출력
            p = re.compile('[^a-z]*')
            text = p.sub('', text)
        # 로그
        print('정상작동', f,'\n','='*70 )

    except Exception as e:
        # 로그 
        print('에러발생', e)


    # 4. 알파벳 그릇 만들기 26 개
    counts = [0] * 26
    ASCII_A = ord('a')
    for i in text:
        counts[(ord(i)-ASCII_A)] += 1
    
    # 합치기 
    total_counts = sum(counts)  
    # 5. 람다를 이용해 빈도수 연산하기 
    frequences = list(map(lambda x:x/total_counts, counts)) # 알파벳 갯수 

    # lang_code   :  언어 코드 
    # frequences  :  알파벳 별로 담긴 평균 빈도수  
    #     => 알파벳별 빈도/총 빈도(= 총 알파벳 문자열 개수) 


    # 결과값 리턴
    return lng_code, frequences


# 함수화 2 
# 훈련용 데이터, 테스트용 데이터 로드 
# 중간경로가 train 혹은 test 

# path = 'train'
# load_data()함수
def load_data(path = 'train'):

    # 파일경로 => format으로 할당 
    file_boxs = glob.glob('./input/{}/*txt'.format(path))

    # 리스트 
    labels = list()
    freqs  = list()


    # 하나씩 출력 
    for box in file_boxs:
        # 1개당 정답, 빈도수리스트 리턴 
        lng,freq = get_data(box)
        labels.append( lng )
        freqs.append( freq )

    # 리턴하는데 제이슨 형식으로 배포 
    return {'labels ':labels , 'freqs': freqs } 
    #  #  {'labels':['en','fr'], 'freqs': [[],[]


def try_load( name, option, encoding='utf-8'):
    #  문자열 안나오게 하려했는데 => 변수로 받아들여서 실패 
    # 그외엔 다 정상동작 
    
    file_path = './input/' + '{}.json'.format(name)
    
    try:
        with open( file_path , option) as f:
            if option == 'w' :
                input_data = input('덤프시킬 데이터를 입력하세요')
                json.dump(input_data,f)

            elif option == 'r' :  
                tmp = json.load(f)
                print('\n길이 =', len(tmp)) 

        print('정상동작')

    except Exception as e:
        print('에러발생', e )

    return 

train_data = load_data()
test_data  = load_data('test')
get_data()
try_load('test_data', 'w')


```


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


### Translation_ language detection -1 
```py
# 파일 리스트 획득
import glob

# 파일 목록 보기 =>  파일명 전부 확득  
path = './input/train/*.txt'
# Build_Modeling\Ml 까지 터미널을 열어야지 동작
file_list = glob.glob(path)
print(file_list[:2], len(file_list))

# 오름차순으로 나열 
print(file_list.sort())

# 언어코드 획득 
# 파일에서 파일명 획득 => 언어 코드존재  => 'tr, en'
test = file_list[0].split('/')[-1][:2]
# 언어코드 추출 
print(test)

# 파일명 획득 
import os
# os.path.basename() 
# 입력받은 경로의 기본 이름(base name)을 반환
name = os.path.basename(file_list[0])
print(name)

# 첫번째 정규식으로 언어 코드 획득 
import re  

p = re.compile('^[a-z]{2}')
lng_code = p.match(name).group() # 그룹화 하는 이유는 뭐지 ? 
print(lng_code)

# 파일 열기
with open(file_list[0],encoding='utf-8')as f:
    # 파일 읽기 + 소문자라 다바꿔서 읽기
    text = f.read().lower()

    # 2번째 정규식 =>내용을 알파벳만 남겨라 
    p = re.compile('[^a-z]*')
    text = p.sub('', text) # 일치하는 값만 제거 

    pass 

# 하나의 이름으로 26의 정보를 담는 그릇
counts = [0 for i in range(26)]
# print(counts)
# counts = [0]*26 

# 쉽고 간단하게 자동화하기위해서 아스키코드를 이용
# ord() 함수사용
print(ord('a'), ord('z'), (ord('z')-ord('a'))) # 아스키 넘버를 확인가능 

# 각 그릇에 정보담기 => 빈도수 담기 
counts = [0]*26
# 기준데이터가 필요  => 아스키값과 기준데이터를 연산해 다른 알파벳을 알수있음
ASCII_A = ord('a')  # a를 기준 데이터 (97이라는 레이블이라고보면 됨)

# text를 돌려 각자의 방이 나오면 1씩 카운트 
for i in text : 
    # counts[(97-97)] += 1 =>  counts[0] += 1 
    counts[(ord(i)-ASCII_A)] += 1
    # break
print(counts,'\n',len(counts))


# 람다함수 
# x: 멤버 하나 하나 
def check_norm(x):
    # print(x)  # 함수 호출 값을 확인 
    # 알파벳별 빈도/총 빈도(= 총 알파벳 문자열 개수)
    return x / len(text)       # x / 총빈도 

# 한 줄짜리 한번 사용할 함수는 => 람다를 이용 => 일회성 
frequences = list(map( lambda x:x/len(text), counts))
print(frequences, len(frequences))

# lng_code   :  언어 코드 
# frequences  :  알파벳 별로 담긴 평균 빈도수  
#     => 알파벳별 빈도/총 빈도(= 총 알파벳 문자열 개수) 




#  함수화 1
# 1. 파일 리스트 획득
import glob
import os, re


try:
    path = './input/train/*.txt'
    file_list = glob.glob(path)
    print('정상작동',file_list)
except Exception as e :
    print('에러발생', e)

# get_data() 함수 
def get_data(file_path):

    # 2. 언어 코드 확득 file_path
    base_name = os.path.basename(file_path)
    # 정규식 사용 
    p = re.compile('^[a-z]{2}')
    lng_code = p.match(base_name).group()


    # 3. 파일을 열면서 정규화
    try:
        with open( file_path, encoding='utf-8') as f :
            # 두번째 정규식 
            text = f.read().lower() # 소문자로 바꿔서 출력
            p = re.compile('[^a-z]*')
            text = p.sub('', text)
        # 로그
        print('정상작동', f,'\n','='*70 )

    except Exception as e:
        # 로그 
        print('에러발생', e)


    # 4. 알파벳 그릇 만들기 26 개
    counts = [0] * 26
    ASCII_A = ord('a')
    for i in text:
        counts[(ord(i)-ASCII_A)] += 1
    
    # 합치기 
    total_counts = sum(counts)  
    # 5. 람다를 이용해 빈도수 연산하기 
    frequences = list(map(lambda x:x/total_counts, counts)) # 알파벳 갯수 
    


    # lang_code   :  언어 코드 
    # frequences  :  알파벳 별로 담긴 평균 빈도수  
    #     => 알파벳별 빈도/총 빈도(= 총 알파벳 문자열 개수) 


    # 결과값 리턴
    return lng_code, frequences


# 함수화 2 
# 훈련용 데이터, 테스트용 데이터 로드 
# 중간경로가 train 혹은 test 

# path = 'train'
# load_data()함수
def load_data(path = 'train'):

    # 파일경로 => format으로 할당 
    file_boxs = glob.glob('./input/{}/*txt'.format(path))

    # 리스트 
    labels = list()
    freqs  = list()


    # 하나씩 출력 
    for box in file_boxs:
        # 1개당 정답, 빈도수리스트 리턴 
        lng,freq = get_data(box)
        labels.append( lng )
        freqs.append( freq )

    # 리턴하는데 제이슨 형식으로 배포 
    return {'labels ':labels , 'freqs': freqs } 
    #  #  {'labels':['en','fr'], 'freqs': [[],[]

train_data = load_data()
test_data  = load_data('test')
get_data()




def try_load( name, option, encoding='utf-8'):
    #  문자열 안나오게 하려했는데 => 변수로 받아들여서 실패 
    # 그외엔 다 정상동작 
    
    file_path = './input/' + '{}.json'.format(name)
    
    try:
        with open( file_path , option) as f:
            if option == 'w' :
                input_data = input('덤프시킬 데이터를 입력하세요')
                json.dump(input_data,f)

            elif option == 'r' :  
                tmp = json.load(f)
                print('\n길이 =', len(tmp)) 

        print('정상동작')

    except Exception as e:
        print('에러발생', e )

    return 





# 현재 만들어둔 파일을 저장 
# json 형태의 파일로 저장 
import json

file_path = './input/'
full_path = file_path + 'labels_freqs_data'

try: 
    with open('{}.json'.format(full_path),'w', encoding='utf-8') as f: 
        # json 구조로 저장  => [train_data, test_data], f
        json.dump([train_data, test_data],f)
        print('정상동작')
except Exception as e:
    print('에러발생', e)






# import
import pandas as pd
import numpy as np


# 데이터로드 
# 위에서 생성한 json 파일을 불러옴
try:
    with open('{}.json'.format(full_path),'r', encoding='utf-8') as f:
        # json 불러오기
        tmp = json.load(f)
    print('정상출력','\n길이 =', len(tmp)) # 0:train, 1:test
    # 길이가 2면 정상
    
except Exception as e :
    print('에러발생', e)

# 훈련 데이터 크기확인 => 20 개
print(len(tmp[0]['labels']),len(tmp[0]['freqs']))
# 테스트 데이터 크기확인  => 8 개 
print(len(tmp[1]['labels']),len(tmp[1]['freqs']))

# 훈련(train)데이터의 빈도데이터만 로드 
# df_freqs 변수에 데이터 프레임 형태의 tmp[0]['freqs'] 데이터를 할당
df_freqs = pd.DataFrame(tmp[0]['freqs']) # 0 => train_data
# 데이터 확인 
print(df_freqs.head(3)) # 값이다름

# 훈련 데이터의 정답 데이터만 로드
# df_labels 변수에 데이터 프레임 형태의 tmp[0]['labels'] 데이터를 할당
df_labels = pd.DataFrame(tmp[0]['labels']) # 0 => train_data
# 데이터 확인 
print(df_labels.head(3)) # 값이다름

# df_freqs 컬럼이름을 a부터 z까지 변경 
from string import ascii_lowercase
# 소문자만 
print(ascii_lowercase)

# 컬럼명 변경
df_freqs.columns = list(ascii_lowercase)
print(df_freqs.head(2))

# concat 사용 
df_concat = pd.concat([df_freqs, df_labels],axis=1)
print(df_concat)

# 중복값의 핵심만 추출  
print(df_concat['label'].unique())


# 인덱스와 컬럼이 2개 이상이라서 피벗 이용불가 => 피봇테이블을 이용해 재구성
# 레이블이 index 일떄 
df_pv =  df_concat.pivot_table(index = df_concat.label) 

# 결과물 
print(df_pv.head(2), df_pv.shape)

# 그래프 패키지 
import matplotlib.pyplot as plt 
%matplotlib inline

# 그래프 그리기 => 바차트 이용해서 한눈에 보기 
# 플로팅 패키지 => ggplot
# style.available
plt.style.use('ggplot')
# 플로팅, y축의 값을 특정 구간으로 제한  =>  ylim=(0,0.25)


# 한그래프에 담기 
df_pv.plot(kind='bar',figsize=(16,8), ylim=(0,0.3))

# 저장
num = 1
file_path = './img/na_per_freqs{}.png'.format(num)
print('저장경로',file_path)
plt.savefig(file_path)


# 각나라별로 그래프를 그리므로서 나라별로 알파벳의 빈도수를 한눈에 확인가능
df_pv.plot(kind='bar',subplots=True,figsize=(16,8), ylim=(0,0.25))

# 저장
# num = 2
# file_path = './img/na_per_freqs{}.png'.format(num)
# print('저장경로',file_path)
# plt.savefig(file_path)

# 보이기
#plt.show()

# 그래프 - 2 
alphabet = ascii_lowercase
all_nara = df_concat.label.unique()
# 1. 나라부터 

# 3. 데이터 출력 

for alpa in alphabet:
#     print(alpa)
    # 2. 중복 제외 나라 픽 
    for nara in all_nara:
#         print(nara)
        # 3. 데이터 출력
        test = df_concat[ df_concat.label == '{}'.format(nara)]
#         print(test)
        test = test['{}'.format(alpa)]
        # 4. 그래프 출력해보기
        test.plot( kind='hist', alpha=0.4, label=nara )
    
    #  5. for문이 끝나기전에 사진 저장 
    # 주의 ) 들려쓰기 조심 => 포문 밖을 나가면 안됨  => 여러개 출력 불가능 
    plt.legend()                    # 각나라표기(범례)
    plt.suptitle('%s freqs' % alpa) # 제목
   
    # 저장하기 
    # 경로를 변수에 담아 저장위치와 함꼐 출력 
    file_path = './img/%s_freqs.png'% alpa
    plt.savefig(file_path)
    print('저장경로',file_path)
    plt.show()
    
#     break

# 그래프 - 3
# 피벗으로 한 자료를 선형차드로 다시 확인 
# 빈도수를 확연하게 확인가능 
df_pv.plot( kind='line', figsize=(16,6), ylim=(0,0.25) )



```


