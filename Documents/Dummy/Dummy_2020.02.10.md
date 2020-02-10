# 2020.02.10
---
# 대용량 데이터분석 및 처리를 위한 Hadoop

    - 데이터 처리
    - 데이터 저장 

- 여러 서버와 스토리지 보유 
- 구축은 리눅스 서버에서 구축하는 것을 권장 

## 하둡과 스파크
    - 빠른 스파크 => 꼭 속도가 필요한 것은 아님 
    - 두가지의 역활은 다르나  하둡과 아파치 스파크는 상호 독립적
        - 스파크를 사용하면 하둡을 같이 사용하게 된다. 

## 다운로드 
---
하둡 홈페이지에서 다운로드 => 
https://hadoop.apache.org/releases.html

버전 3.1.2	=> binary (checksum signature) 클릭 
    => 자동으로 다운 안될 때 눌러서 다운  http://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz 

- 자바 버전 확인 
    - java -version
    - jdk 버전 

    - 없으면 자바 설치하고 
        - 환경변수 (고급시스템에서 환경변수)
            - 1. 자바 홈 설정 
                - JAVA_HOME 
                    => C:\Program Files\Java\jdk1.8.0_211
                - path 
                    새로만들기 => C:\Program Files\Java\jdk1.8.0_211\bin  
                    - %JAVA_HOME%\bin 
                
        ```bash
        C:\>where java # 이렇게 쳤을 때
        #>>> 아래와 같이 출력 되면 Good
        C:\Program Files\Java\jdk1.8.0_211\bin\java.exe
        C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe

        ```
- hadoop-3.1.2.tar 압축 풀기 
    - C:\Bigdata 새 폴더를 만든다 
    - 반디집을 관리자 권한으로 열어서 C:\Bigdata위치에 압축을 품 

- hadoop-3.1.2_winutils 설치 
    - 압축을 풀면 bin 이라는 폴더 생김 
    - hadoop-3.1.2.tar 압축을 풀어 생긴 hadoop-3.1.2 열고 bin 폴더에 들어가 hadoop-3.1.2_winutils(bin)을 빈을 열어 hadoop-3.1.2(bin)에 덮어 쓴다 . 


---

### 하둡 설정 파일 

|하둡 설정파일|설명|
|---------|---|
|conf/masters|세컨더리 네임노드가 동작하는 노드를 명시|
|conf/slaves|데이터노드와 태스크 트래커가 동작하는 노드를 명시|
|conf/hadoop-env.sh|하둡이 실행하는 모든 프로세스에 적용되는 시스템 환경 관련 스크립트|
|conf/core-site.xml|하둡 분산 파일 시스템과 하둡 맵리듀스 모두에 적용할 수 있는 스크립트|
|conf/hdfs-site.xml|하둡 분산 파일 시스템 설정 스크립트|
|conf/mapred-site.xml|하둡 맵리듀스 설정 스크립트|
---

---

```py 

# 
```
---



# 판다스 
``` py

판다스는 
- 구조화된 데이터나 표 형식의 데이터를 빠르고 쉽고(고성능) 표현적으로 다루도록 설계
    - 구조화 
    - 고성능 array계산 

    - 인덱싱, 연산용함수, 전처리 함수, 
    - 인덱싱 연산용

    - 시리즈 
    - 데이터프레임

열을 시리즈 
열과 행을 데이터 프레임 테이블 전체
시리즈 구조 (인덱스 데이터 데이터 타입)
데이터 프레임 생성 문법 기억
딕셔너리 타입으로 선언 
판다스로 지정해주기
describe
정렬 => sort_values
판다스 상관계수 확인하는 함수
corr

drop 세로로 지우는 방법과
가로로 지우는 방법을 지우기 axis=0 / 1
apply 함수 데이터 프레임 전체 컬럼에 함수를 적용

데이터 타입이 시리즈 일때 쓴느 것 map
=> 사용자 정의 함수를 적용해서 원소에 적용

데이터 합치기
concat => 같은 데이터를 붙이는 연산 작업
데이터 프레임 연결 시 사용 axis 적용가능

날짜 데이터로 바꿔주는 함수
to_datetime 함수

groupby 된거에는 apply 대신에
aggregation => 그룹함수 
transformation
filter 특정조건에 맞는 애만 걸러줌

seaborn
matpotlib이 있어야 파이썬에서 대표적인 시각화 라이브러리
어떻게 임포트 하는지 기억

sns.barplot
boxplot
중간 중앙 최소 최대 신뢰구간 안에 있는 작은값
folium 기본 설정을 해주는 기능folium.Map

```
---
### 데이터 엔지니어링 
### 데이터 분석거
### 데이터 사이언티스트
### 데이터 아키덱쳐 
---

