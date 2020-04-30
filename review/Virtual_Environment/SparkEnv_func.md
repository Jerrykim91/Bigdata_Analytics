<br>

# SparkEnv_func


## 패키지 불러오기 
```py
import pyspark    # pyspark

import findspark  # findspark
# findspark 패키지를 통해서 스파크를 찾아내고      
# pyspark.SparkContext 명령어로 스파크 접속지 점을 특정
```



<br>

# RDD

RDD는 외부데이터를 읽어서 처리하거나 자체적으로 컬렉션 데이터를 생성하여 처리할 수 있다. 

또한 데이터 처리는 파티션 단위로 분리해서 작업을 처리한다. 


RDD 타입 
- 트랜스포메이션(transformation)
    - 필터링 같은 작업으로 RDD에서 새로운 RDD를 반환 
- 액션(action) 
    - RDD로 작업을 처리하여 결과를 반환
    - 실행될 때마다 새로운 연산을 처리 
        - 만약 작업의 처리 결과를 재사용하고 싶으면 persist() 메소드를 사용하여 결과를 메모리에 유지할 수 있다. 
            
            
RDD는 SparkContext객체를 이용하여 생성이 가능하다. 
- SparkContext
    - SparkConf 객체를 이용해서 파라메터값을 설정 혹은 생성한다. 
    - 초기화도 가능하다. 

<br>

## RDD 데이터 이용

1. 내부 데이터를 이용하는 방법(Parallelized Collections)
    - parallelize() 메소드를 이용
        - 연산 : map(), reduce(), filter() 등의 RDD 연산을 이용해서 처리한다. 


2. 외부데이터 이용 
    - textFile() 메소드를 이용

<br>

## spark 세션을 생성해주기위해서 다음과 같이 컴파일을 진행해준다.  

```py
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

conf = pyspark.SparkConf().setAppName('appName').setMaster('local[2]')
# sc = SparkContext(master='local[2]', appName='appName')
sc = pyspark.SparkContext(conf=conf)
spark = SparkSession(sc)
# sc.stop()

```
### 만약 세션이 끝나면 코드를 실행한다. 

```py

# 리스트에서 RDD 생성 
data = list(range(1,6))

# inputdata의 새로운 집합을 생성하기위함 
rdd = sc.parallelize(data, 4) # data를 메모리에 저장될때 4조각으로 쪼개서 메모리에 저장 

sc.defaultParallelism
rdd1 = rdd.map(lambda x: x * 2)
# map() : 데이터를 가공한다. 반환타입이 같지 않아도 된다.

# collect()는 액션이며 실제로 collect()가 호출되면 RDD가 메모리에 올려져 계산이 이루어진다. 
# 각 테스크의 엔트리들을 수집한후 그결과를 다시 SparkContext전송한다.
rdd1.collect()

rdd2 = rdd.filter(lambda x: x % 2 == 0)
# filter() : 함수의 결과가 참인경우에만 요소들을 통과시키는 함수이다. 결과로 새로운 RDD를 생성한다 
# 액션은 아니다. 

rdd2.collect()

```
<br>

## Test_1 - code( filter를 테스트 해보자 ) 

``` py
def ten(val):
    if(val<10):
        return True
    else:
        return False
    

Filter_test = rdd1.filter(ten)
Filter_test.collect()

# 주어진 조건에 해당하는 데이터만 선별해 오는 것을 알 수 있다.
```

<br>

### Action

- reduce(func)  
- take(n)  
- collect()  
- takeOrdered(n, key=func) 

<br>

```py
rdd3 = sc.parallelize([1, 4, 2, 2, 3])
rdd3.distinct().collect()
# distinct() : 중복을 제거한 RDD를 반환한다. 

rdd4 = sc.parallelize([1, 2, 3])
rdd4.map(lambda x: [x, x+5]).collect()

rdd4.flatMap(lambda x: [x, x+5]).collect()
# 차원 변경 ?
# iterator 안에 포함된 값으로 RDD를 구성하기 원할 경우에 flatmap()을 사용

rdd = sc.parallelize([1,2,3])
rdd.reduce(lambda a, b : a * b)

# reduce(func): 계산된 값을 하나로 합쳐준다. 
# reduce은 파티션 레벨 단위로 적용된다.

rdd.take(2)
# take(): RDD에서 해당 개수만큼 데이터를 가져온다. 

rdd5 = sc.parallelize([5, 3, 1, 2])
rdd5.takeOrdered(3, lambda s: -1 * s)
# takeOrdered() : 해당 개수만큼 데이터를 가져오는데 정렬해서 가져온다.(오름차순, 내림차순)

```


## Test_2 - code( 데이터 세트를 넘겨주고 RDD를 생성 ) 

``` py

# 리스트를 생성
tmp_data = range(1,10001)

# 담자 
plc_RDD = sc.parallelize(data,10) # 파티션은 제한이 없는것인가? 
print('type of plc_RDD: {0}'.format(type(plc_RDD)))

# 해당 RDD의 파티션 숫자를 확인
plc_RDD.getNumPartitions()  

print(plc_RDD.toDebugString())  
 >> b'(10) ParallelCollectionRDD[2] at parallelize at PythonRDD.scala:195 []'

print('plc_RDD id: {0}'.format(plc_RDD.id())) # RDD id 확인 
 >>> plc_RDD id: 2

```

<br>

<참조><br>
빅데이터 - 스칼라(scala), 스파크(spark)로 시작하기: <https://wikidocs.net/28387>     
\[SPARK\]Tutorial(pyspark) : <https://yujuwon.tistory.com/entry/spark-tutorial>

<br>