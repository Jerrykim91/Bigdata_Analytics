# Dummy_02.04 to 02.07 
---
### 02. 05
- 기록 방법
  - 블로그
  - [notion](https://www.notion.so/)
  - onenote...
  - [github_io](https://pages.github.com/) 

- 쥬피터 노트북 특수명령어
  - !
  - %
  - ? : 도움말 보기

- 제플린.. 알아보기(쥬피터 노트북 비슷)

- df.sample() : 랜덤하게 가져오기

- 연도, 월별 컬럼명 합쳐주는 반복문!
  - eda0205.md, 후반부에서 호가인
```py
# 컬럼을 새로 만들어 주기 위해 0번째와 1번째 행을 합쳐준다.
for i, y in enumerate(year):
    if i > 2 and i < 15:
        year[i] = ' '.join(['2014년', month[i]])
    elif i >= 15:
        year[i] = ' '.join(['2015년', month[i]])
    elif i == 2 :
        year[i] = ' '.join([year[i], month[i]])
    elif i == 1:
        year[i] = '시군구'
```

- 내일 시험 본다. 오전에 복습, 오전 공부 오후 시험


- pandas는 numpy 기반으로 한다.
- numpy 속도는 python 보다 빠름.


- ADsP
- p-value :  유의수준  0.05 이하면 유의하다.
- 귀무가설 : 귀무가설은 기각되야 좋다.
- R-squared 결정계수 :

    - 전진선택
    - 후진소거
    - 단계선택


- 정상성 이해하기


- 데이터 마이닝
  - 지도학습
  - 비지도학습 알기


- 성과분석 별표 다섯개!

---

## 시험 복습
1. pip install <패키지명>

2. 패키지들의 alias 별명
   1. pandas as pd
   2. numpy as np
   3. plt
   4. etc...

3. pandas 특징
   1. 구조화된 데이터 처리를 지원하는 python 라이브러리
   2. 고성능 array 계산 라이브러리인 numpy와 통합하여, 강력한 "스프레드시트"처리 기능을 제공
   3. 인덱스, 연산용 함수, 전처리 함수 등을 제공

4. pandas 구성
   1. 데이터 프레임 : Data table 전체를 포함하는 object
   2. 시리즈 : 한 칼럼을 읽는 object

5. 시리즈의 구조
   1. Index
   2. data
   3. Data Type

6. 데이터 프레임 생성
   1. pd.DataFrame( raw_data(시리즈데이터, 딕셔너리), columns=[컬럼명 지정, , ,])

- T : transpose, values : 값 출력, to_csv() : 값 변환
7. 기술할 떄 = df.describe() : 수치형
    - df.describe(include=np.object) : object형
    - 
8. 정렬할 때 쓰는 함수 sort_values()

9. 판다스에서 상관계수를 구하는 함수 : np.corrcoef(), df.corr()
   1.  공분산 cov()

10. Data Drop에서 축을 기준으로 행 또는 열 삭제 (축에 대한 개념)
    1.  axis=0 : index, row
    2.  aixs=1 : columns

11. Lambda 함수
    1.  - 코딩할 줄 몰라도 읽을준 알아야한다.
    2.  lambda argument : expression
    3.  `f = lambda x,y : x + y`    `f(1,4)`    `5`
      ```py
      def f(x, y):
          return x+y
      ```

12. apply 함수 for dataframe
    - 보통 람다 함수 넣어서 잘 사용함.
    ```py
    df.apply(사용자함수)
    ```

13. 시리즈일 때 apply처럼 사용하는 것. map()
    1.  `series.map(lambda x: x**2)`

14. 같은 형태의 데이터를 붙이는 연산 작업 Concat
    1.  pandas.concat(obj, )

15. 날짜 데이터로 바꿔주는 것 to_datetime()
    1.  pandas.to_datetime(obj, )

16. groupby
    1.  aggregation - agg()
    2.  transformation - transform()
    3.  filter - filter()

17. 판다스 대표적 시각화 라이브러리 matplotlib 
    1. import 하는 방법.
    2. `import matplotlib.pyplot as plt`

18. seaborn 시각화 차트 라이브러리
    1.  히트맵 사용 `sns.heatmap()`

19. 차트 중에 읽을 수 있어야 하는 것 box plot
    1. 신뢰구간 안에서 최소값 최대값

20. folium에서 지도를 그리는 것
    1.  folium.Map()


### 썰
- 라즈베리파이, 아두이노kit
- KPI 핵심성과지표

------

# 2020. 2. 7. 필기

- ch01_빅데이터 개념과 처리 과정.pptx에 정리 있음.

## 1. 빅데이터의 개념과 처리 과정

- 디지털 데이터 단위
  - 1TeraByte = 1024GB
  - 1PetaByte = 1024TB
  - 1ExaByte = 1024PB
  - 1ZetaByte = 1024EB
  - 1YottaByte = 1024ZB
- 빅데이터의 기준은 무엇일까?
  - 데이터가 많다고?
  - 내가 할 수 있는 범위를 넘어서는...
- 데이터
  - 예전에는 log 데이터 등.. 쌓이는 데이터를 다 버렸다. -> AI 발전 저조
  - 데이터를 많이 쌓이면서 다양한 케이스들이 생겨서 AI가 발전하게 됨.
  - Full Stack 개발자? ... 나타나기 시작했다.

- 큐.. 엠큐..

| 구분     | 정보화시대  | 스마트시대                    |
| -------- | ----------- | ----------------------------- |
| 자료구조 | 큐          | 엔큐?                         |
| 저장     | 정형 데이터 | 비정형데이터, 클라우드 서비스 |
| 관리     | KMS         | 플랫폼, 소셜 네트워크         |
| 분석     | ERP, CRM    | 빅데이터 분석                 |

- 속성
  - 규모
  - 다양성
  - 속도 : 대용량 데이터.. (단일은 기본 서버가 빠르지만.. 대용량은 분산 서버가 빠르다.)
  - 정확성
  - 가치

- 정의
  - 데이터
  - 데이터 처리, 축적, 분석 기술
  - 인재, 조직

- 종류
  - 비정형
  - 반정형
  - 정형

- 전통적 데이터 vs 빅데이터

  - 표

- 처리 특징

  - 의사결정 속도, 처리 복잡도, 데이터 규모, 데이터 구조, 분석 유연성, 처리량

- 처리 과정

  - 데이터 소스 > 수집 > 저장 > 처리 > 분석 > 표현

    - | 과정 | 영역                    |
      | ---- | ----------------------- |
      | 생성 | 내부데이터, 외부 데이터 |
      | 수집 | 크롤링, ETL             |
      | 저장 | NoSQL, 스토리지, 서버   |
      | 처리 | 맵리듀스, 프로세싱      |
      | 분석 | NLP, 기계학습, 직렬화   |
      | 표현 | 가시화, 호기득          |

- 새로운 용어 많이 배움...

  - 알아보기 : ETL, kafka(분산구조 로그 수집기), Thread(쓰레드), spark
  - 저장 
    -  분산파일 시스템
      -  GFS(Google File System), HDFS(Haddop Distributed File System)
    - NoSQL
  - 빅데이터 분석 기술
    
    - 
  - |용어|
    |:--|
    |텍스트 마이닝|
    |웹 마이닝|
    |오피니언 마이닝|
    |리얼리티 마이닝|
    |소셜 네트워크 분석|
    |분류 Classfication|
  |군집화 Clustering|
    |Machine Learning|
    |감성 분석 Sentiment Anaysis|
    
  
  

## 데이터 분석 프로젝트 관리 방법론

데이터 분석 프로젝트 관리 방법론.pptx



- KDD

  - Selection
  - Preprocessing
  - Transformation
  - Dataming
  - Interpration / Evaluation

- SEMMA (Smapling Exploration Modification Modeling Assessment)

  - Sample
  - Exploration
  - Modification
  - Modeling
  - Assessment

- CRISP-DM(CRoss-Industry Standard Process for DataMining)

  - Business understanding
  - Data understanding
  - Data preparation
  - Modeling
  - Evaluation
  - Deployment

  - 선생님 평 : 얘가 현실적인 편이다.

![img](https://k.kakaocdn.net/dn/bgGzs3/btqt0a0xEOK/TKRgf6YaKqL09xsvWOrkkk/img.png)

- CRISP-DM Task

![phases and generic tasks of CRISP-DM. ](https://www.researchgate.net/profile/David_Corrales2/publication/283430974/figure/fig1/AS:614004070309903@1523401386613/phases-and-generic-tasks-of-CRISP-DM.png)



 - | 시계열 데이터     | 예측 |
   | ----------------- | ---- |
   | 카테고리성 데이터 | 분류 |

### 프로젝트 관리 방법론

- 애자일 방법론 [[Agile\] 애자일이란 - Heee's Development Blog](https://gmlwjd9405.github.io/2018/05/26/what-is-agile.html)
  - 플랜 할 때는 플랜에 집중
  - 회의 시 카드 게임 :해야될거를 주욱 쓰고... 1,3,5 카드를 들고 몇시간 몇시간 카드 내기
  - 일의 순서 조정하기 : 목표일에 맞게 일을 조정하기

- 간트 차트

- WBS (간트 차트 + .... )

- PM - Project Manager - [3.1.](https://namu.wiki/w/프로젝트 관리#toc)

- ITIL 기반 서비스 관리  - [01(651-659) CPL17-10.hwp - 01.pdf](http://kiise.or.kr/e_journal/2017/12/KTCP/pdf/01.pdf)

- 보여주고자 하는 화면 하나에 집중하는 것도 한가지 방법이다.

- KPI 인사평가할 때 기본..(Key Performance Indicators)

  - 기준을 세우는 것..

- 위험 관리 (Issue 관리)

  - 아무도 안 해 봤는데.. 될지 안될지 몰라.. 해봐야 아는 것.

  ​        [![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MjFfMjUx/MDAxNTM0ODQxNjY2ODYz.7QLw1UkfkC3ZulGNaa7poB01-dWVsld0OvLJvCO00m4g.fyF9cZo6RJ8v-VxW5VTgwWvGlt-QDvxeZB_wS0RRQ8Ig.PNG.jdhpuppy/image.png?type=w800)](https://m.blog.naver.com/PostView.nhn?blogId=jdhpuppy&logNo=221343689820&proxyReferer=https%3A%2F%2Fwww.google.com%2F#) 

  - 데이터 준비 단계

  -  데이터 정의 : 무슨 데이터가 어디에 있는데 어떠한 형태로 어떻게 가지고 올거냐.

  - 

  - 프로젝트 관리에 수반되는 활동

    - 기획 +
      위험(risk) 측정 +
      이용가능한 자원의 산정
      작업 분류 체계(Work Breakdown Structure;WBS)의 작성 +
      필요한 인적, 물적 자원 확보
      비용 산정(인력)
      팀원에의 작업 할당
      진척 관리 +
      목적에 따른 결과가 도출되게끔 작업의 방향성을 유지
      달성한 결과를 분석
    - 피드백만 잘해줘도.

  - WBS

    - Trello
    - JIRA
    - Redmine

  - 애자일 방법론

    - 산출물 없이 하자? 필요한건 있어야한다. (최소 요구사항 기획서)
    - 개발 표준에 대한 것은 처음에 반드시 정해야 한다. (이중작업 방지)
    - WBS와 개발표준을 만드는 것이 중요하다 (반나절이 걸려도)

  - slack - 대화채널, 개발도구랑 연동이 자로딤

  - jira - 팀원 5명 이내는 무료

    

---

# 20. 02. 08.

## Hadoop
- hadoop common
- HDFS
- Hadoop MapReduce



- 구성



- Hadoop과 Spark는 한 쌍처럼 따라다닌다.
  - Hadoop은 빅데이터 분산처리
  - Spark는 빠르게 읽어오기 (MapReduce는 사장되는 추세라고 한다. -대체-)
  
- 하둡 다운로드

  - https://www.apache.org/
  - Download > 3.1.2 > binary download

  

  - 환경변수 설정하기

    - `내 PC > 우클릭 > 설정 > 고급 시스템 설정 > 환경변수` 또는 `Win + Q > 환경 변수`

    - 시스템 환경변수

      - 변수 이름 : JAVA_HOME 

        - 변수 값 : jdk가 설치된 디렉토리 ex) C:\Program Files\Java\jdk1.8.0_211

      - Path > 편집 > 새로만들기

        - %JAVA_HOME%\bin 또는
    - 디렉토리풀네임\bin  ex) C:\Program Files\Java\jdk1.8.0_211\bin
        - 위로 이동으로 우선순위를 올린다.
        - cmd 창을 새로 열고, `where java `로 경로 확인
    
        ```
    C:\Users\admin>where java
        C:\Program Files\Java\jdk1.8.0_211\bin\java.exe
        ```
        
    
  - 하둡을 설치할 폴더를 만든다. `c:\bigdata\`

  - 다운받은 파일 압축을 푼다.

    -  (에러 날 경우 반디집 관리자 권한으로 압축풀기)

  - 윈도우에서 사용할 경우 winutils 의 bin폴더를 덮어쓰기 한다. `hadoop-3.1.2_winutils`



- 하둡 벤더 배포판
  - [기고 | 하둡 배포판 3종의 현재와 미래 - CIO Korea](http://www.ciokorea.com/news/21480)
  - 클라우데라(Cloudera), 맵알(MapR), 호트웍스(Hortonworks)



## ref

[Code Dragon :: Hadoop - install for windows (설치 및 설정하기)](https://codedragon.tistory.com/9582)



### Hadoop 설정 파일 수정
- hadoop-env.sh
  - `\etc\hadoop` 에 있음.
  - windows에서는 hadoop-env.sh 대신 hadoop-env.cmd 설정 수정

- hadoop-env.cmd
  - `@rem`은 주석
  - 윈도우는 폴더명에 길거나 빈 문자 등이 들어가면 제대로 인식하지 못한다.
  - cmd에서 `dir /x`로 확인하여 짧은 폴더명 확인 ex> `PROGRA~1`
  - 인식이 안될 경우
    - `set JAVA_HOME=C:\PROGRA~1\Java\JDK18~1.0_2` 이런 식으로 대체

  - JAVA_HOME 경로 설정
  - HADOOP_IDENT_STRING 설정
    - 맨 끝에 있음
    - %USERNAME%은 cmd에서 `set`으로 확인.
  - 하단에 추가
```cmd
set HADOOP_PREFIX=C:\bigdata\hadoop-3.1.2
set HADOOP_CONF_DIR=%HADOOP_PREFIX%\etc\hadoop
set YARN_CONF_DIR=%HADOOP_CONF_DIR%
set PATH=%PATH%;%HADOOP_PREFIX%\bin;%HADOOP_PREFIX%\sbin
```

- core-site.xml
  - 하단에 추가
  - 임시저장 폴더를 설정하고 해당 위치에 폴더를 만들어준다.
```xml
<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://0.0.0.0:9000</value>
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/c:/bigdata/hadoop-3.1.2/tmp</value>
  </property>
</configuration>
```



- hdfs-site.xml
  - 하단에 추가
  - 네임노드 위치, 데이터노드 위치를 설정하고 해당 위치에 폴더를 만들어준다.
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.permissions</name>
        <value>false</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/C:/bigdata/hadoop-3.1.2/data/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/C:/bigdata/hadoop-3.1.2/data/datanode</value>
    </property>
</configuration>
```

- mapred-site.xml
  - 하단에 추가
```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>mapred.job.tracker</name>
    <value>0.0.0.0:9001</value>
  </property>
</configuration>
```

- yarn-site.xml
  - 하단에 추가
```xml
<configuration>
    <!-- Site specific YARN configuration properties -->
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
    <property>
        <name>yarn.log-aggregation-enable</name>
        <value>true</value>
    </property>
    <property>
        <name>yarn.nodemanager.pmem-check-enabled</name>
        <value>false</value>
    </property>
    <property>
        <name>yarn.nodemanager.vmem-check-enabled</name>
        <value>false</value>
    </property>
</configuration>
```

- workers 파일
  - 가분산 모드에서는 `localhost` 하나만 있음.
  - 완전 분산 모드에서는 호스트 파일의 사용리스트 이름을 목록으로 추가

- 호스트 파일 위치
  - windows : `C:\Windows\System32\drivers\etc`
  - linux : `/etc/`

- 잘 동작하는지 확인
  - cmd 관리자 권한으로 실행
  - `hdfs namenode -format`
  - `'네임노드 디렉토리' has been successfully formatted.`가 뜨는지 확인
  - `start-dfs.cmd` 실행 (sbin 폴더 안에 있는 명령어)
    - cmd 창 2개 생성 (닫지 않고 그대로 둔다.)
  - `start-yarn.cmd` 실행
    - cmd 창 2개 생성 (닫지 않고 그대로 둔다.)
  - `jps` 실행
    ```cmd
    10416 NameNode
    11792 ResourceManager
    11920 DataNode
    1360 Jps
    7672 NodeManager
    ```
    - 5줄이 나오면 제대로 동작

- 종료 할 때는 꼭 아래 명령어를 사용
    - `stop-dfs.cmd`
    - `stop-yarn.cmd`


  - 브라우저에서 확인
    - http://localhost:9870 Namenode information
    - (하둡 2.x 버전에서는) http://localhost:50070 


- [항공 관련 공개 데이터](http://www.rdatasciencecases.org/Data/Airline/)
  - 예제에서 2008년도 데이터를 사용한다.

### 하둡 명령어
- 하둡 폴더 만들기
  - `hdfs dfs -mkdir /airline/`
- 하둡 목록 보기
  - `hdfs dfs -ls /`
- 파일 넣기
  - `hdfs dfs -put 2008.csv /airline/`


#### 예제 실습
- [6.통계기반데이터분석기법 on PNU20191216 | Trello](https://trello.com/c/nZqOuDK3/13-6통계기반데이터분석기법)에서
  - WordCount.jar 다운로드
  - speech.tar.gz 다운로드

- 다운로드 받은 것 풀고,
- 파일 하둡에 넣고
  -  `hdfs dfs -put ./speech /speech`
- 워드카운트 실행
  - `hadoop jar WordCount.jar /speech/ /output/word_count`
- 확인
  - `hdfs dfs -ls /output/word_count`
- 글자 수 확인
  - `hdfs dfs -head /output/word_count/part-r-00000`

### 자주 쓰는 명령어
- 참고 : [Hdfs dfs 명령어 정리 및 설명(ls, cat, du, count, copyFromLocal 등)](https://blog.voidmainvoid.net/175)
  - ls : 목록 보기
    -  `hdfs dfs -ls /<디렉토리>`
  - 파일 내용 보기 : cat, text
  - mkdir [-p] : 디렉토리 생성
  - put, get : 파일복사(로컬<->HDFS)
  - cp, mv : 이동, 저장
  - rm [-R] [-skipTrash] : 파일삭제, 디렉토리 삭제, 완전삭제
  - chmod, chown, chgrp : 권한, 소유주, 그룹 변경
- 라이브러리
  - pyhadoop

### 조 편성
- 조 6개 : 4 4 3 3 3 3
- 조장 : 최병철, 김이환, 김민섭, 정용희 + 서연주, 오창석
  - 최병철, 성훈, 재경
  - 김이환, 소현, 장원
  - 정용희, 효원, 준호
  - 서연주, 영재, 지윤, 준형
  - 김민섭, 홍근, 아인, 환희
  - 오창석, 선우, 석원