# 스파크 스피드 체크 

import time
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

from pyspark import SparkContext

# spark context는 한 번에 여러 개를 돌리면 세팅에 몇개를 추가해야한다. 
# 또한 스파크 컨텍스트를 제대로 구현하고자 하면 손대야할것이 많지만 지금은 테스트 용이라서 생략 


#  이미 스파크가 살아 있으면  죽였다가 다시  그게아니면 그냥 생성 
if sc is None:
    sc = SparkContext(master='local', appName='1st app')
else:
    sc.stop()
    sc = SparkContext(master='local', appName='1st app')

# 주석 확인 

# performance check
spark_time_list = list()
python_time_list = list()
python_np_time_list = list()

n_list = [20000*i for i in range(0,10)]

for n in n_list:
    # 무슨 함수 
    def each_ck(k):
        return 1/(16**k)*( 4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
    
    ## with spark 
    start_time = time.time()
    pi_approximated = sc.parallelize(range(0,n)).map(each_ck).sum()
    spark_time_list.append(time.time()-start_time)
    
    ## pure python
    start_time = time.time()
    pi_approximated = sum((each_ck(k) for k in range(0, n)))
    python_time_list.append(time.time()-start_time)

    # with numpy
    start_time = time.time()
    pi_approximated = np.apply_along_axis(arr=np.array(range(0,10)), func1d=each_ck, axis=0).sum()
    python_np_time_list.append(time.time() - start_time)

## plotting

df = pd.DataFrame({
    'spark':spark_time_list.copy(),
    'pure python': python_time_list.copy(),
    'python with numpy': python_np_time_list.copy()
}, index=[2000*i for i in range(0,10)])
plt.figure(figsize=(12,6))
plt.plot(df['spark'], 'ro-'), plt.plot(df['pure python'],'bo-'), plt.plot(df['python with numpy'],'go-')
plt.legend(fontsize=25)
plt.xticks([20000*i for i in range(0, 10)], [20000*i for i in range(0, 10)])
# plt.savefig('./grp.svg')
plt.show()