# 스파크 

스파크 2.4.5 Download Mirror : <https://www.apache.org/dyn/closer.lua/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz>

Visual C++ 런타임 라이브러리 제거 + 설치
: <https://knowledge.autodesk.com/ko/search-result/caas/sfdcarticles/sfdcarticles/KOR/How-to-remove-and-reinstall-Microsoft-Visual-C-Runtime-Libraries.html> 

# 자바 설치 

jdk 
jre

$ java -version 확인 

# 환경 변수설정 

JAVA_HOME : 설치 위치
HADOOP_HOME : 설치 위치
SPARK_HOME : 설치 위치
path (확인 or 추가)

```bash
C:\bigdata\hadoop-3.1.2\bin
C:\bigdata\hadoop-3.1.2\sbin
C:\bigdata\spark-2.4.5-bin-hadoop2.7\bin
C:\bigdata\spark-2.4.5-bin-hadoop2.7\sbin
```
# 환경 변수 적용 확인

- CMD 창 재시작 후 > where yarn
- Winutils 확인 > where winutils.exe

```bash
# pySpark 설치
$ conda install -c conda-forge pyspark
# findspark 설치
$ conda install -c conda-forge findspark 
```

```py
# findspark
import findspark

findspark.init()
findspark.find() # 홈 경로를 출력 

# spark 세션을 생성해주기 위해서 다음과 같이 컴파일을 진행 
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

conf = pyspark.SparkConf()\
    .setAppName('appName').setMaster('local[2]')# 'local[숫자]' 숫자를 주면 스레드 형태로 생성 

sc = pyspark.SparkContext(conf=conf)
spark = SparkSession(sc)

# 만약 세션인 끝난다면 다음과 같은 코드를 실행 
sc.stop()

```