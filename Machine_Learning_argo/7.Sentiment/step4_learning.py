# step4_learning.py
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from step3_word_tokenizer import tokenizer, tokenizer_porter
from time import time
import pandas as pd
import pickle


def step4_learning():

    # csv 파일에서 데이터를 읽어옴
    df = pd.read_csv('./Machine_Learning_argo/data/refined_movie_review.csv')
    # 데이터를 테스트, 학습데이터로 나눔
    X_train = df.loc[:35000 - 1, 'review'].values
    y_train = df.loc[:35000 - 1, 'sentiment'].values

    X_test = df.loc[35000:50000, 'review'].values
    y_test = df.loc[35000:50000, 'sentiment'].values

    # print(y_test)
    print(len(X_train),len(X_test))

    # 단어장을 만들어주는 객체 생성 
    # TF_IDF : TF * IDF => 단어의 빈도와 문서의 빈도를 곱한 값 
    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer_porter)
    # 데이터를 학습하기 위한 객체
    logistic = LogisticRegression(C=10.0, penalty='l2', random_state=0)
    # 파이프 라인 설정 
    pipeline = Pipeline([('vect',tfidf),('clf',logistic)])

    # 학습 
    stime = time()
    pipeline.fit(X_train, y_train)
    print('학습 종료')
    print('총 학습시간 : %d' % (time() - stime))

    # 테스트
    y_pred = pipeline.predict(X_test)
    print("정확도 : %.3f" % accuracy_score(y_test, y_pred))

    # 학습이 완료된 객체를 저장한다.
    with open('./Machine_Learning_argo/7.Sentiment/pipe.dat', 'wb') as fp :
        pickle.dump(pipeline, fp)

    print('저장완료')

    