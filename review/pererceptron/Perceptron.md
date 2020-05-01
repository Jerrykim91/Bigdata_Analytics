
# 직접 구현해보자 


```py

import pickle
import numpy as np
from time import time
# from perceptron import perceptron

```

## 1단계 퍼셉트론 생성 

```py

# perceptron 알고리즘 구현

import numpy as np


class Preceptron:
    """
    클래스 멤버 : 주요 알고리즘 
    """
   
    # 생성자 함수 생성 
    def __init__(self, thresholds =0.0, eta=0.01, n_iter=10 ):

        """
        # 생성자의 기본 인자들 
        - thresholds: 임계값(default =0.0)
        - eta = 학습률(default =0.01)
        - n_iter = 학습의 횟수(default =10) 

        """
        self.thresholds = thresholds
        self.eta = eta
        self.n_iter = n_iter


    # 학습함수
    def fit(self, X, y):

        """
        X : 독립변수  - 입력 데이터 (대문자)
        y : 종속 변수 - 결과 데이터 
        """
        self.w_ = np.zeros(1 + X.shape[1])  # 가중치를 넘파이 배열로 정의 
                                            #  X.shape[1] 트레이닝 데이터의 입력값 개수를 의미 
                                            # X 가 5 x 2인 경우 -> x.shape = (5,2)
        
        
        # 예측값과 실제값을 비교 
        self.errors_ = [] # 예측값과 실제 결과값이 다른 오류 회수하고 저장하기 위한 에러박스 
        
        # 지정된 학습 횟수만큼 반복 -> 왜 버려 ?
        """
        self.n_iter 지정한 숫자만큼 반복 
        _ 값은 아무런 ㅡ이미없는 변수 
            -> 단순하게 for문을 특정 횟수 만큼만 반복 하자고 할 때 
        관습적으로 반복하는 변수 

        """
        for _ in range(self.n_iter):
            # 예측값과 실제 값을 담을 변수 
            errors = 0 
            tmp = zip( X, y )     # 입력값과 결과값을 묶어줌
           
            for xi, target in tmp :   # 입력받은 입력값을 묶음을 가지고 반복
                #입력값을 가지고 예측값을 계산
                a1 = self.predict(xi)
        
                if target != a1 :     # 입력값과 예측값이 다르면 가중치를 계산 
                    update = self.eta * (target - a1)
                    self.w_[1:] += update * xi 
                    self.w_[0]  += update

                    # 값이 다른 횟수를 누적
                    errors += int(update != 0.0)

            # 값이 다른 횟수값을 배열에 담음
            self.errors_.append(errors)
            print(self.w_)


    def net_input(self, X):

        """
        - 각 자리의 값과 가중치를 곱한 총합을 구함 
        - 가중치 * 입력값의 총합을 계산 
        - X : 입력값
        """
        a1 = np.dot(X, self.w_[1:]) + self.w_[0]  # al = sum(w_ * X) + b 
        return a1


    # 예측
    def predict(self, X): 
        """
        - 예측된 결과를 가지고 판단
        - X : 입력값 배열 
        """
        # 0 > 1
        # 0 <= -1 
        a2 =  np.where(self.net_input(X) > self.thresholds, 1, -1 )
        return a2 



```
fit 부분인 조금 아리송송하다 

## 2 단계 학습 

```py

def step1_learning():
    # 학습과 테스트를 위해 사용할 데이터를 정의한다. 
    X = np.array([0,0],[0,1],[1,0],[1,1])
    y = np.array([-1,-1,-1,1])
    
    # 퍼셉트론 객체를 생성
    ppn = perceptron(eta=0.1)

    # 학습 
    stime = time()
    ppn.fit( X, y )
    etime = time()
    print("학습에 걸린 시간 : ", (etime - stime))
    print("학습중 오차가 난 개수  : ", ppn.errors_)


    # 학습이 완료된 객체 파일로 저장

    with open('./data/perceptron.dat', 'wb') as fp :
        pickle.dump(ppn, fp)

        print(" 머신러닝 학습 완료 ")

```