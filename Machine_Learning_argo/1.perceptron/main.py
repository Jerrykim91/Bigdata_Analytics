# main.py

import numpy as np
from perceptron import perceptron
from time import time
import pickle
import pandas as pd

def step1_get_data():
    # iris.data 파일에서 데이터를 읽어 옴 
    df = pd.read_csv('what\data\iris.data', header=None)
    # print(df)

    X = df.iloc[0:100, [2,3]].values
    # print(X)
    # 꽃 종류 데이터 추출 
    y = df.iloc[0:100, 4].values

    # 퍼셉트론 객체를 생성
    ppn = perceptron(eta=0.1)

    # 학습 
    stime = time()
    ppn.fit( X, y )
    etime = time()
    print("학습에 걸린 시간 : ", (etime - stime))
    print("학습중 오차 개수 : ", ppn.errors_)

    return X, y



def step2_learning():
    ppn  = perceptron(eta = 0.1)
    data = step1_get_data()

    X = data[0]
    y = data[1]

    # 학습 
    pnn.fit(X,y)
    print(ppn.errors_)
    print(ppn.w_)
    # 학습된 객체를 지정한다. 

    # 학습이 완료된 객체 파일로 저장
    with open('./data/3.Iris/perceptron.dat', 'wb') as fp :
        pickle.dump(ppn, fp)

        print(" 머신러닝 학습 완료 ")




def step3_using():
    # 복원 
    with open('./data/3.Iris/perceptron.dat', 'rb') as fp :
        ppn = pickle.load(fp)

    while True : 
        a1 = input("너비 입력 :")
        a2 = input("길이 입력 :")

        X = np.array([float(a1),float(a2)])

        # 계산된 결과를 가져온다
        result  = ppn.predict(X)
        if result == 1 :
            print("결과 : 세토사")
        else :
            print("결과 : 벌시컬러")




if __name__ == "__main__":
    step1_get_data()
    step2_learning()
    step3_using()