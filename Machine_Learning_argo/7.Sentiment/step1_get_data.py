# step1_get_data.py

import pandas as pd
import numpy as np
import os, codecs





# step1_get_data
def step1_get_data():
    # 데이터 파일들이 들어 있는 결로 
    path  = './Machine_Learning_argo/data/aclImdb/'
    # 긍정 또는 부정을 의미하는 값
    labels = {'pos' : 1, 'neg' : 0}
    # csv에 저장할 값을 관리할 객체 => 데이터 프레임 
    df = pd.DataFrame()

    # 각 데이터를 합치기 
    # 디렉토리의 개수만큼 반복
    for s in ('test','train'):
        print('>>>>done 1st for -1')

        for name in ('pos','neg'):
            # 읽어올 파일들이 들어 있는 디렉토리명 생성 
            subpath = '%s/%s' % (s, name)
            dirpath = path + subpath
            print('>>>>done 2ed for-1')
            # print(dirpath)

            # 현재 디렉토리안에 있는 파일 목록 
            file_list = os.listdir(dirpath)
            # print(file_list)


            # 파일 목록을 순회하면서 정보를 가져옴
            for file in file_list:
                fileName = os.path.join(dirpath, file)
                print('>>>done 1st for-2')
                with codecs.open(fileName,'r','utf-8') as fp :
                    txt = fp.read()
                    # print(labels[name], ":", txt)
                    print('>>>done 2nd for-2')

                # 데이터프레임 객체에 저장 
                df = df.append([[txt, labels[name]]], ignore_index=True)
                # print(fileName)
    print('>>>>>done make df_object')



    # 컬럼 설정 
    df.columns = ['review', 'sentiment']
    # 순서를 섞는다.
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))

    # 저장
    df.to_csv('./Machine_Learning_argo/data/movie_review.csv', index=False)

# step1_get_data()
