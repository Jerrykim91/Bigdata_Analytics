
# pyspark란 ? 

병렬 및 분산엔진인 스파크를 이용하기 위한 파이썬 api이다. 

RDD(Resilient Distributed Dataset)을 지원하는 아키텍쳐 
RDD는 read-only를 목적으로 다양한 머신에 데이터셋으 멀티셋(중복을 허용)을 분산해두고 특정한 머신에 문제가 생기더라도 문제없이 읽을 수 있도록 지원한다. 

설치 관련은 SparkSetup.md 을 참조!  

Spark를 많이 쓰는 이유는 속도가 빨라서 
실제로 디비나, 리스트 처럼 데이터가 묶음으로 있을때 이를 병렬로 처리해서 속도를 빨리처리 
매트릭스 연산과 비슷하다고 해도 무방할정도로 




# < 참조 >
https://www.samsungsds.com/global/ko/support/insights/Spark-Cluster-job-server.html
스파크 이해하기: <https://12bme.tistory.com/305>