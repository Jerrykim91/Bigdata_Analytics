# 코드 작성전 어떤 그림이 그려질지 상상하자 
# 그리고 의사코드를 작성 =>  다시 역설계 한다.


'''
의사 코드 작성
목표 : 

step01
1. 파일 목록화 
    - 파일에서 파일을 목록화 
    - 파일명을 전부 얻는다
2. text 파일 한개 확인  
    - file_list의 개수만큼 반복
    - 20번 반복(list의 갯수)
3. 언어코드 획득 및 추출
    - 파일에서 파일명 확득 
    - 정규식을 이용해 특정 포인트만 추출 

step02
1. 전처리를 통해 영어만 남김 
    - 파일을 불러옴
    - 읽을때 소문자만 읽어옴
2. 알파벳만 남김(소문자만) 
    - 정규식을 이용 
3. 알파벳 별로 할당할 각각의 공간을 만듬 
    - a-z 까지 26개의 공간이 필요 
step03 
1. 텍스트 파일만 읽어서 알파벳 
step01 
step01 

'''



# import
import os, re , glob, json

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt 
%matplotlib inline

from string import ascii_lowercase



try:
    path = './input/train/*.txt'
    file_list = glob.glob(path)
    print('정상작동',file_list)
    
except Exception as e :
    print('에러발생', e)



# get_data() 함수 
def get_data(file_path):

    base_name = os.path.basename(file_path)
    p = re.compile('^[a-z]{2}')
    lng_code = p.match(base_name).group()

    try:
        with open( file_path, encoding='utf-8') as f :
            text = f.read().lower() 
            p = re.compile('[^a-z]*')
            text = p.sub('', text)

        print('정상작동', f,'\n','='*70 )

    except Exception as e:

        print('에러발생', e)


    counts = [0] * 26
    ASCII_A = ord('a')
    for i in text:
        counts[(ord(i)-ASCII_A)] += 1
    
    total_counts = sum(counts)  
    frequences = list(map(lambda x:x/total_counts, counts)) 

    return lng_code, frequences


# get_data()


# 함수화 2 
# load_data()함수
def load_data(path = 'train'):
    file_boxs = glob.glob('./input/{}/*txt'.format(path))
    labels = list()
    freqs  = list()

    for box in file_boxs:
        lng,freq = get_data(box)
        labels.append( lng )
        freqs.append( freq )

    return {'labels ':labels , 'freqs': freqs } 


train_data = load_data()
test_data  = load_data('test')



file_path = './input/'
full_path = file_path + 'labels_freqs_data'

try: 
    with open('{}.json'.format(full_path),'w', encoding='utf-8') as f: 
        
        json.dump([train_data, test_data],f)
        print('정상동작')
except Exception as e:
    print('에러발생', e)



try:
    with open('{}.json'.format(full_path),'r', encoding='utf-8') as f:
        tmp = json.load(f)
    print('정상출력','\n길이 =', len(tmp)) 
    
except Exception as e :
    print('에러발생', e)

file_path = './input/' + path
full_path = file_path + 'labels_freqs_data'


def try_load(name, option, encoding='utf-8'):
    name = str(name)
    option = str(option)
    file_path = './input/' + '{}.json'.format(name)
    try:
        with open( path, option) as f:
            if option == 'w' :
                input_data = input('덤프시킬 데이터를 입력하세요')
                json.dump(input_data,f)

            elif option == 'r' :  
                json.load(f)
                print('\n길이 =', len(tmp)) 

        print('정상동작')

    except Exception as e:
        print('에러발생', e )

    return 


print(len(tmp[0]['labels']),len(tmp[0]['freqs']))
print(len(tmp[1]['labels']),len(tmp[1]['freqs']))


df_freqs = pd.DataFrame(tmp[0]['freqs'])
df_labels = pd.DataFrame(tmp[0]['labels']) 
df_freqs.columns = list(ascii_lowercase)
df_concat = pd.concat([df_freqs, df_labels],axis=1)

print(df_concat['label'].unique())
df_pv = df_concat.pivot_table(index = df_concat.label) 



plt.style.use('ggplot')
df_pv.plot(kind='bar',figsize=(16,8), ylim=(0,0.3))
num = 1
file_path = './img/na_per_freqs{}.png'.format(num)
print('저장경로',file_path)
plt.savefig(file_path)
plt.show()


df_pv.plot(kind='bar',subplots=True,figsize=(16,8), ylim=(0,0.25))
num = 2
file_path = './img/na_per_freqs{}.png'.format(num)
print('저장경로',file_path)
plt.savefig(file_path)
plt.show()


alphabet = ascii_lowercase
all_nara = df_concat.label.unique()
for alpa in alphabet:
    for nara in all_nara:

        test = df_concat[ df_concat.label == '{}'.format(nara)]
        test = test['{}'.format(alpa)]
        test.plot( kind='hist', alpha=0.4, label=nara )
    
    plt.legend()                   
    plt.suptitle('%s freqs' % alpa) 
   
    file_path = './img/%s_freqs.png'% alpa
    plt.savefig(file_path)
    print('저장경로',file_path)
    plt.show()
    