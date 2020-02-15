# step2_preprocessing.py
import pandas as pd 
from time import time
# 정규식 
import re



# 전처리 작업을 위해 호출될 함수 => preprocessor
# preprocessor
def preprocessor(text) :
    # 문자열의 내의 html 태그를 삭제
    text = re.sub('<[^>*>]', '', text)
    # 문자열에서 이모티콘을 찾아냄
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)|\^.?\^', text)

    # 문장에서 특수문자를 제거하고 문자열을 소문자로 바꿈
    # 추출한 이모티콘을 붙여줌

    text = re.sub('[\W]+', ' ', text.lower() + ' '.join(emoticons).replace('-', ''))
    # print(text)
    print('>>>> done preprocessor')
    return text






# step2_preprocessing 
def step2_preprocessing():

    # csv 데이터를 읽어 옮
    df = pd.read_csv('./Machine_Learning_argo/data/movie_review.csv')

    # 전처리 작업 
    stime = time()
    print('>>> 전처리 시작')
    # 사용자가 만든함수를 불러와서 사용할때 ! => apply 사용 
    df['review'] = df['review'].apply(preprocessor)
    print('전처리 완료')
    print('소요시간: %d' % (time()-stime))

    # 전처리된 데이터를 저장 
    df.to_csv('./Machine_Learning_argo/data/refined_movie_review.csv',index=False)
    print('done_step2_all ')


# step2_preprocessing()