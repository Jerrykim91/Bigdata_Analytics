<br>

# SparkEnv_Outline

우리는 pyspark를 이용해 스파크를 간접적(?)으로 다루게 된다.      
그러기 위해서는 간단하게라도 pyspark가 무엇인지 spark란 무엇인지를 알아야한다.      

<br>

# 1. Spark란 ?


아파치 스파크(**Spark**)는Apache에서 관리되고 있는 오픈소스 프로젝트이며 
빅데이터 처리를 위한 분산 클러스터컴퓨터 프레임워크이다. 
스파크는 복수의 컴포넌트로 구성되며, 스파크 코어는 데이터소스로 HDFS(Hadoop Distributed File System) 뿐만 아니라 Hive, HBase, PostgreSQL, MySQL, CSV 파일 등도 처리가 가능하다. 
 

인메모리를 기반으로 한 대용량 데이터를 처리할 수 있는 데이터 고속 처리 엔진을 가지고있다.
그렇기때문에 대량의 데이터를 고속 병렬분산처리한다. 
스파크는 하둡보다 100배정도 빠른속도를 가지고 있다.   


스파크는 데이터셋으로부터 데이터를 읽어 들인 뒤 스토리지 I/O와 네트워크 I/O를 최소화하도록 처리한다. 따라서 스파크는 동일한 데이터에 대한 변환처리가 연속으로 이루어지는 경우와 머신러닝처럼 결과셋을 여러 번 반복해 처리하는 경우에 적합하다. 지연이 작게 동작하는 특성을 이용해 스트림처리를 할 수도 있다. 


스파크에서 가장 기본적인 개념은 데이터셋이라고 불리는 분산 컬렉션이다. 
Dataset은 Hadoop InputFormat(HDFS파일)으로 부터 만들어지거나 다른 데이터셋을 변경하여 만들어진다.    
동적으로 타입 검사를 수행하는 파이썬의 특성 때문에 파이썬에서는 데이터셋의 타입의 체크는 필요하지 않다.      
Python에서 사용하는 모든 Dataset은 DataSet[Row]의 형태인데 이것은 우리가 주로 사용하는 DataFrame의 DataFrame과 동일한 개념이다.      


<br>

# 2. pyspark란 ? 

병렬 및 분산엔진인 스파크를 이용하기 위한 파이썬 api이다. 

RDD(Resilient Distributed Dataset)을 지원하는 아키텍쳐 
RDD는 read-only를 목적으로 다양한 머신에 데이터셋으 멀티셋(중복을 허용)을 분산해두고 특정한 머신에 문제가 생기더라도 문제없이 읽을 수 있도록 지원한다. 

설치 관련은 SparkSetup.md 을 참조!  

Spark를 많이 쓰는 이유는 속도가 빨라서 
실제로 디비나, 리스트 처럼 데이터가 묶음으로 있을때 이를 병렬로 처리해서 속도를 빨리처리 
매트릭스 연산과 비슷하다고 해도 무방할정도로 


**-ing** 

<br>

---

< 참조 >
​

1. 스파크 공식홈페이지 -> [이동](https://spark-korea.github.io/docs/index.html)

2. 아파치 스파크란? ->
[이동](https://12bme.tistory.com/433)

3. 스파크 이해하기 -> [이동](https://12bme.tistory.com/305) 

4. 클러스터 리소스 최적화를 위한 Spark 아키텍처 -> [이동](https://www.samsungsds.com/global/ko/support/insights/Spark-Cluster-job-server.html)

---
<br>