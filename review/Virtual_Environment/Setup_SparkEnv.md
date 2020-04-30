<br>

# SetUp : 스파크 사용환경 구축

혹시 Visual C++ 런타임 라이브러리여부를 확인하고 없다면 설치하는 것이 좋다.

---
설치: <https://knowledge.autodesk.com/ko/search-result/caas/sfdcarticles/sfdcarticles/KOR/How-to-remove-and-reinstall-Microsoft-Visual-C-Runtime-Libraries.html>   

---

<br>
<br>

## 1. 자바(java) 설치 

커맨드(cmd)창에 다음과 같이 입력했을때 출력이 있어야 한다.


```cmd
$ java -version

출력 >>> java version "1.8.0_144"
    Java(TM) SE Runtime Environment (build 1.8.0_144-b01)
    Java HotSpot(TM) Client VM (build 25.144-b01, mixed mode, sharing)

```

만약 위와 같이 나오지 않는다면 자바가 설치가 안 된 것이므로 아래 링크에서 설치한다.

---
설치경로 1 : <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>

설치경로 2 : <https://www.apache.org/dyn/closer.lua/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz>

---

<!-- --- -->
<br>

### 1.1 자바 환경변수 설정 

시스템 환경변수에서 아래와같이 설정 해주어야한다.

```cmd

# JAVA_HOME 변수를 설정
JAVA_HOME = C:\Program Files\Java\jdk1.8.0_201

# 경로를 환경변수에 추가 
C:\Program Files\Java\jdk1.8.0_201\bin        

```
<!-- --- -->

<br>

### 1.2 자바 환경변수 설정 확인

커맨드(cmd) 창 재시작 후 
- `$where yarn`

Winutils 확인 
- `$ where winutils.exe`



<br>

## 2. SPARK Install

스파크 설치를 진행하기위해 아래의 링크에서 데이터를 다운받는다. 

---
설치 경로 : <http://spark.apache.org/downloads.html>

---

<br>

### 2.1 스파크 환경변수 설정 

시스템 환경변수에서 아래와 같이 설정이 필요하다.

추가)     
복붙시 파일이름은 본인들 파일이름 일 것      
본인들이 다운받은 파일과 동일한 파일 이름일 것 - 아래는 예시 

```cmd

# SPARK_HOME, HADOOP_HOME변수를 설정
SPARK_HOME = C:\spark\spark-2.3.2-bin-hadoop2.7
HADOOP_HOME = C:\spark\hadoop2.7 

# PATH에 아래와 같이 선언 
C:\spark\spark-2.3.2-bin-hadoop2.7\bin        

```

<br>
<br>

## 3. winutils.exe 설치

---
설치 경로: <https://github.com/steveloughran/winutils> 

---

하둡버전과 동일하게 설치를 진행해준다.      
다운받은 winutils.exe를 스파크를 설치해준 bin폴더에 저장한다.      

예) 현재 나의 경로 ->  C:\spark\spark-2.3.2-bin-hadoop2.7

<br>

### 3.1 폴더생성 

`C:\tmp\hive` 와 동일한 경로에 폴더를 생성한다.

<br>

### 3.2 관리자 권한으로 cmd를 실행시키고 두개의 명령어를 실행


```cmd
$ winutils.exe chmod -R 777 C:\tmp\hive
$ winutils.exe ls -F C:\tmp\hive

# 이렇게 실행하면 다음과 유사하게 출력됨
출력 >>> drwxrwxrwx|1|LAPTOP-.....

```


<br>
<br>

## 4. Pyspark 설치 확인 


Pyspark 설치 : `conda install -c conda-forge pyspark`

cmd창에 들어가서 pyspark명령어를 치면     
아래와 같이 뜨면 성공 

```cmd

(base) C:\>pyspark
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.5
      /_/


```

<br>

### 4.1 Pyspark 설치 확인 - 체크 

추가 확인으로 pyspark 실행후 다음과 같은 명령어가 동작하는지 확인 

```cmd

nums = sc.parallelize([1,2,3,4])
nums.map(lambda x:x*x).collect()

```

<br>
<br>

## 5. Pyspark를 쥬피터 노트북에 연결 

anaconda prompt가 설치되어있다는 가정하에 진행한다.

<br>

아래의 명령어를 실행한다. 

```cmd
# findspark 설치 
$ conda install -c conda-forge findspark
```

이후 jupyter notebook을 실행시키고 다음과 같이 컴파일

```py
import findspark 
findspark.init()
findspark.find() 

import pyspark 
findspark.find()

# spark 세션을 생성해주기위해서 다음과 같이 컴파일을 진행해준다.

from pyspark import SparkContext, SparkConf 
from pyspark.sql import SparkSession 

conf = pyspark.SparkConf().setAppName('appName').setMaster('local’) 
sc = pyspark.SparkContext(conf=conf) # sc에 스파크 콘텍스트를 담는다.
spark = SparkSession(sc) # sc를 세션을 할당한다.

# 만약 세션이 끝난다면 다음과같은 코드를 실행한다
sc.stop() # 세션 종료
```
<br>
---
<br>