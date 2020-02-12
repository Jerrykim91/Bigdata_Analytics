# 학습용 데이터
from sklearn import datasets
# 데이터를 학습용과 테스트용으로 나눌수 있는 함수
from sklearn.model_selection import train_test_split
# 데이터 표준화
from sklearn.preprocessing import StandardScaler
# Perceptron 머신러닝을 위한 클래스
from sklearn.linear_model import Perceptron
# 로지스트 회귀를 위한 클래스 
from sklearn.linear_model import LogisticRegression
# SVM을 위한 클래스 
from sklearn.svm import SVC
# 의사결정 나무를 위한 클래스 
from sklearn.tree import DecisionTreeClassifier
# 그리드서치 클래스
from sklearn.model_selection import GridSearchCV
# 교차검증 
# from sklearn.model_selection import KFold
# 정확도 계산을 위한 함수 
from sklearn.metrics import accuracy_score
# 파일 저장
import pickle
import numpy as np


# from mylib.plotdregion import * 

name = None

def step1_get_data():
    
    # 아이리스 데이터 추출
    iris = datasets.load_iris()
    # print(iris) # 딕션너리 형태 안에 아이리스 데이터 가들어있음 !! => 데이터 프레임 
    # print(type(iris))
    # 꽃 정보 데이터 추출 
    X = iris.data[:150, [2,3]]  # 꽃잎 정보 
    y = iris.target[:150]       # 쫓 종류 #

    names = iris.target_names[:3] # 꽃 이름  => target_names 컬럼이름 
    print('='*20,'log point >>> step1_get_data ','='*20)
    # print(X[0])
    # print(y[0])
    # print(names[0])

    return X, y



def step2_learnig():

    # 변수에 담음
    X, y = step1_get_data()
    # 학습 데이터와 테스트 데이터로 나눔 
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.3, random_state = 0 )
    # 표준화 작업 : 데이터들을 표준 정규분포로 변환
    #              적은 학습횟수와 높은 학습 정확도를 갖기 위해 하는 작업 
    sc = StandardScaler()
    # 데이터 표준화 =>  X_train_std
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)

    # 학습 => 알고리즘 변경 ()
    # 알고리즘에 어떤 파라메터가 들어가는지 어떤작용을 하는지 공부할 필요가 있다.  
    # criterion : 불순도 측정 방식, entropy, gini
    # max_depth : 노드 깊이의 최대 값
    machine_learing = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)


    machine_learing.fit(X_train_std, y_train)
    print('학습')

    # 학습 정확도 확인 
    X_test_std = sc.transform(X_test)
    y_pred = machine_learing.predict(X_test_std)
    print("학습 정확도 :", accuracy_score(y_test, y_pred))
    # 학습이 완료된 객체를 지정
    with open('./Machine_Learning_argo/5.Scikit_Tree/ml.dat', 'wb') as fp :
        pickle.dump(sc, fp)
        pickle.dump(machine_learing, fp)

    print('학습완료')

    # 시각화를 위한 작업
    # X_combined_std = np.vstack((X_train_std, X_test_std))
    # y_combined_std = np.hstack((y_train, y_test))
    # plot_decision_region(X=X_combined_std, y=y_combined_std, classifier=ml, test_idx=range(70, 100), title='perceptron')

def step2_learnig2():
    # ? 
    X, y = step1_get_data()
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.3, random_state = 0 )
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    machine_learing = DecisionTreeClassifier()
    parameters = {'max_depth':[1,2,3,4,5,6,7], 'min_samples_split':[2,3]}

    grid_ml = GridSearchCV(machine_learing, param_grid=parameters, cv=3, refit=True)
    grid_ml.fit(X_train_std, y_train)

    # 학습 정확도를 확인해본다.
    print('GridSearchCV 최적 파라미터:', grid_ml.best_params_)
    print('GridSearchCV 최고 정확도: {0:.4f}'.format(grid_ml.best_score_))

    estimator = grid_ml.best_estimator_
    X_test_std = sc.transform(X_test)
    y_pred = estimator.predict(X_test_std)
    print('테스트 데이터 세트 정확도: {0:.4f}'.format(accuracy_score(y_test,y_pred)))

    # 학습이 완료된 객체를 저정한다.
    with open('./Machine_Learning_argo/5.Scikit_Tree/ml.dat', 'wb') as fp :
        pickle.dump(sc, fp)
        pickle.dump(estimator, fp)

    print('학습완료')


def step3_using():

    # 학습 완료된 객체를 복원
    with open('./Machine_Learning_argo/5.Scikit_Tree/ml.dat', 'rb') as fp :
        sc = pickle.load(fp)
        ml = pickle.load(fp)
    
    # print('데이터 확인',ml)


        '''while True:
        input_width  = input("꽃 잎의 너비를 입력해주세요 :")
        input_height = input("꽃 잎의 길이를 입력해주세요 :")

        X = np.array([float(input_width),float(input_height)])
        X_std = sc.transform(X)
        # 데이터를 입력해 결과를 가져옴
        y = ml.predict(X_std) 
        # print(y)

        if y[0] == 0 :
            print('Iris-setosa')
        else :
            print('Iris-versicolor')'''

    X = [
        [1.4, 0.2],[1.3, 0.2],[1.5, 0.2],
        [4.5, 1.5],[4.1, 1.0],[4.5, 1.5],
        [5.2, 2.0],[5.4, 2.3],[5.1, 1.8]
    ]

    X_std = sc.transform(X)
    # 결과 추출 
    y_pred = ml.predict(X_std)

    for value in y_pred :
        if value == 0 :
            print('Iris-setosa')
        elif value == 1 :
            print('Iris-versicolor')
        elif value == 2 :
            print('Iris-virginica')



# 실행         

if __name__ == "__main__":
    # step1_get_data()
    # step2_learnig()
    step2_learnig2()
    step3_using()

