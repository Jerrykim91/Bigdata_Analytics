# main.py

import numpy as np
from perceptron import perceptron
from time import time
import pickle


def step1_learning():
    # 학습과 테스트를 위해 사용할 데이터 
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

def step2_using():

    with open('./data/perceptron.dat', 'rb') as fp :
        ppn = pickle.load(fp)

    while True : 
        a1 = input("첫번째 2진수를 입력해 주세요 :")
        a2 = input("두번째 2진수를 입력해 주세요 :")

        X = np.array([int(a1),int(a2)])
        # 계산된 결과를 가져온다
        result  = ppn.predict(X)
        if result == 1 :
            print("결과 : 1")
        else :
            print("결과 : 0")




if __name__ == "__main__":
    step1_learning()
    step2_using()