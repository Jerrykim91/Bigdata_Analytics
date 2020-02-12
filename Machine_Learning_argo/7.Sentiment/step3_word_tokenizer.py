# step3_word_tokenizer.py

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk

# stopword 단어 사전을 다운로드 
nltk.download('stopwords')
# stopword 데이터 가져 옮
stop = stopwords.words('english')
# 단어 줄기를 하기 위한 객체 
porter = PorterStemmer()



# 함수 생성 - 공백으로 단어 분리 
def tokenizer(text):
    print('>>>done_tokenizer')
    return text.split()

def tokenizer_porter(text):

    # 띄어쓰기를 기준으로 분리
    word_list = text.split()
    # 단어 줄기 처리 => 리스트 내포를 이용해서 작업  
    word_list_re = [porter.stem(word) for word in word_list]  
    print('>>>done_tokenizer_porter')

    return word_list_re




# 단어 줄기 
def step3_word_tokenizer():
    text = 'runners like running and thus they run'

    a1 = tokenizer(text)
    a2 = tokenizer_porter(text)
    print('a1 :', a1)
    print('a2 :', a2)

    print('>>done_step3')


step3_word_tokenizer()