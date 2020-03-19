import struct  # 바이너리

# SVM을 위한 클래스 
from sklearn.svm import SVC
# 데이터 표준화
from sklearn.preprocessing import StandardScaler
# Perceptron 머신러닝을 위한 클래스
from sklearn.linear_model import Perceptron
# 로지스트 회귀를 위한 클래스 
from sklearn.linear_model import LogisticRegression
# 의사결정 나무를 위한 클래스 
from sklearn.tree import DecisionTreeClassifier
# 랜덤 포레스트
from sklearn.ensemble import RandomForestClassifier
# 정확도 계산을 위한 함수 
from sklearn.metrics import accuracy_score , classification_report
# 데이터를 학습용과 테스트용으로 나눌수 있는 함수
# from sklearn.model_selection import train_test_split
# from sklearn import svm, model_selection, metrics
# # 알고리즘 
# clf = svm.SVC()



def decode_mnist( dataType='train', dir='./data/mnist', samples=1000 ):
    
    label_name = f'{dir}/{dataType}-labels-idx1-ubyte'  
    image_name = f'{dir}/{dataType}-images-idx3-ubyte'
    print(label_name, '\n', image_name)
    
    label_f = open( label_name, 'rb')
    image_f = open( image_name, 'rb')
    
    csv_f = open( f'{dir}/{dataType}.csv', 'w', encoding='utf-8' )

    LABEL_HEAD_SIZE = 4 + 4
    magic, label_cnt = struct.unpack('>II', label_f.read(LABEL_HEAD_SIZE) )
    print(magic, label_cnt)

    IMAGE_HEAD_SIZE = 4 + 4 + 4 + 4
    magic_img, image_cnt, row, col = struct.unpack('>IIII', image_f.read(IMAGE_HEAD_SIZE) )
    print(magic_img, image_cnt, row, col)
    pixels = row * col
    

    for idx in range(label_cnt):
        if idx >= samples:
            break
    
        label_value = struct.unpack( 'B', label_f.read(1) )    
        label = label_value[0] # (5,) => 0번째만 추출

        binary_data = image_f.read( pixels )
        strPixelData= list( map( lambda x:str(x) , binary_data ) ) 
        csv_f.write( str(label) + ',' )
        csv_f.write( ','.join(strPixelData) + '\n' )
        #break
        if idx == 0: # 1회만 수행
            with open('test.pgm', 'w', encoding='utf-8') as f:
                f.write( 'P2 28 28 255\n' + ' '.join(strPixelData) )


    if label_f:label_f.close()
    if image_f:image_f.close()
    if csv_f:csv_f.close()
        
# decode_mnist()


def load_csv( dataType='train', dir='./data/mnist' ):

    # 0. 데이터를 담는 자료구조
    labels = list()
    images = list()

    # 1. csv 파일 오픈
    with open( f'{dir}/{dataType}.csv', 'r' ) as f:
    # 한줄씩 읽는다
        for line in f:      
            # 분해
            tmp = line.strip().split(',')
            #print(tmp)
            # 정답 데이터 담기 -> 타입은 수치로 변환
            labels.append( int(tmp[0]) )
            # 각 픽셀을 256개(색상의 총수)로 정규화 하여서 리스트로처리
            images.append( list( map( lambda x:int(x)/256, tmp[1:] ) ) )
    return { 'labels':labels   ,'images':images }

# 학습용 
decode_mnist( dataType='train', samples=750)
decode_mnist( dataType='t10k' , samples=250)


# 훈련, 테스트 데이터 준비
train = load_csv()
test  = load_csv( dataType='t10k' )

X_train = train['images']
y_train = train['labels']

X_test = test['images']
y_test = test['labels']

# clf = SVC()
# clf.fit(X_train, y_train)
# predict = clf.predict( X_test )
# accuracy_score(y_test, predict )
# t = classification_report( y_test, predict )

def tmp_train(al_data , t_data, s_data):

#     if t_data == train :
#         dataType='train'
        
#     elif t_data == test:
#         dataType='t10k'
        
    decode_mnist( dataType = t_data , samples = s_data )

    if t_data == 't10k' :
        test = load_csv(dataType = t_data)
    else: 
        test = load_csv()
    
    X_test = test['images'] # X_test
    y_test = test['labels'] # y_test
    

    # 알고리즘
    clf = al_data
    # 학습     
    clf.fit(X_test, y_test)
    # 예측
    predict = clf.predict( X_test )
    # 실제 정답 
    ml_accuracy = accuracy_score(y_test, predict )
#     print(f'accuracy : {ml_accuracy}')
    # 리포트
    t = classification_report( y_test, predict )
    print('='*60)
    # 평가
    ml_score= clf.score( X_test, y_test )
    print(f'Accuracy : {ml_accuracy} || Score : {ml_score}')
    print('='*60)
    
    return print(t)


# dataType='train' # train
# dataType='t10k'  # test 
# clf = SVC()


# tmp_test( SVC(), 't10k', 1000)




# 데이터 준비
train = load_csv()
test  = load_csv( dataType='t10k' )
len(train['labels']), len(test['labels']) # 데이터 준비 완료 

def tmp(al_data , t_data, s_data, mult=1 ):

    data = load_csv()
    X_data = data['images'] # X_test
    y_data = data['labels'] # y_test
    samples_size = int(s_data* mult)
    
    print('='*60)
    print('samples_size',samples_size)
    print('='*60)
    decode_mnist( dataType = t_data , samples = samples_size )
    # 알고리즘
    clf = al_data
    # 학습     
    clf.fit(X_data, y_data)
    # 예측
    predict = clf.predict( X_data )
    # 실제 정답 
    ml_accuracy = accuracy_score(y_data, predict )
#     print(f'accuracy : {ml_accuracy}')
    # 리포트
    t = classification_report( y_data, predict )
    print('='*60)
    # 평가
    ml_score= clf.score( X_data, y_data )
    print(f'Accuracy : {ml_accuracy} || Score : {ml_score}')
    print('='*60)
    
    return print(t)

# tmp( SVC(), 't10k', 1000, 8)


def tmp_scaler():

    pass


if __name__ == "__main__":
    tmp_test() #  디코딩 