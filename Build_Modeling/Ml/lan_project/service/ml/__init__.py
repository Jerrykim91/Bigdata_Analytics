from sklearn.externals import joblib
from sklearn import svm, metrics
import json

# 언어 감지 예측 모델기능으로 학습된 알고리즘을 로드
# 요청이 들어 올 때마다 예측하고 결과를 던져준다.

# 경로  
folder_path = 'Build_Modeling/Ml/lan_project/service/ml/' 
# folder_path = 'service/ml/' 
model_path = folder_path + 'clf_modle_202003101113.model'
label_path = folder_path + 'clf_labels.json'


# 분류기(알고리즘) 로드 
clf = joblib.load(model_path) 

# 레이블(정답) 로드 
with open(label_path, 'r') as f:
  clf_label = json.load(f)

def detect_lang( oriTxt ):
    # 주피터를 참고해서 작성 
    # 1. 데이터 가공 
    clf = svm.SVC( gamma='auto' )
    clf.fit( clf_label[0]['freqs'], clf_label[0]['labels'] )
    # 2. 예측 
    predict = clf.predict( clf_label[1]['freqs'] )
    # 3. 출력결과 구성 
    print( metrics.classification_report( clf_label[1]['labels'],
                              predict ) )
    return 'en', '영어'

