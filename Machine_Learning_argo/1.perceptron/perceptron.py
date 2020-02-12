# perceptron.py
# perceptron 알고리즘을 구현하는 파일 
# 단층 퍼셉트론

import numpy as np


class perceptron:
    # 생성자 함수 생성
    # thresholds: 임계값 , 계산된 
    # eta = 학습률 
    # n_iter = 학습 횟수 
    def __init__(self, thresholds =0.0, eta=0.01, n_iter=10 ):
        self.thresholds = thresholds
        self.eta = eta
        self.n_iter = n_iter


    # 학습함수
    # X: 독립변수 - 입력데이터 , y: 종속 변수 - 결과 데이터 
    def fit(self, X, y):
        # 가중치를 담을 행렬을 생성 
        self.w_ = np.zeros(1 + X.shape[1])
        # 예측값과 실제값을 비교 
        # 다른 예측값의 개수를 담을 리스트 
        self.errors_ = [] 


        # 지정된 학습 횟수만큼 반복 
        for _ in range(self.n_iter):
            # 예측값과 실제 값을 담을 변수 
            errors = 0
            # 입력값과 결과값을 묶어줌
            tmp = zip(X,y)
            # 입력받은 입력값을 묶음을 가지고 반복
            for xi, target in tmp :
                #입력값을 가지고 예측값을 계산
                a1 = self.predict(xi)
                # 입력값과 예측값이 다르면
                # 가중치를 계산 
                if target != a1 :
                    update =self.eta * (target - a1)
                    self.w_[1:] += update * xi 
                    self.w_[0]  += update

                    # 값이 다른 횟수를 누적
                    errors += int(update != 0.0)

            # 값이 다른 횟수값을 배열에 담음
            self.errors_.append(errors)
            print(self.w_)



    # 가중치 * 입력값의 총합을 계산 
    # X : 입력값 
    def net_input(self, X):
        # 각 자리의 값과 가중치를 곱한 총합을 구함 
        a1 = np.dot(X, self.w_[1:]) + self.w_[0]
        return a1



    # 예측된 결과를 가지고 판단 
    # X: 입력값 배열 
    def predict(self, X): 
        # 0 > 1
        # 0 <= -1 
        a2 =  np.where(self.net_input(X) > self.thresholds, 1, -1 )
        return a2 
