/# 퍼셉트론 Perceptron
---

# 퍼셉트론 Perceptron
---
## 인공신경망 
- 인공지능은 우리 사람의 뇌를 흉내내는 인공신경망과 다양한 머신러닝 알고리즘을 통해 구현
- 사람의 뇌는 신경계를 구성하는 주된 세포인 뉴런(neuron)을 약 1000억개 정도 가지고 있음 
- 뉴런들은 시냅스라는 구조를 통해 전기, 화학적 신호를 주고 받음으로써 다양한 정보를 받아들이고 그 정보를 저장하는 기능을 수행

## MCP 뉴런

- 1943년 신경과학자인 Warren S. McCulloch과 논리학자인 Walter Pitts는 하나의 사람 뇌 신경세포를 하나의 이진(Binary) 출력을 가지는 단순 논리게이트로 표현

- MCP 뉴런 : 여러 개의 입력신호가 가지돌기에 도착하면 신경 세포 내에서 이들을 하나의 신호로 통합하고, 통합된 신호 값이 어떤 임계값을 초과하면 하나의 단일 신호가 생성되며, 이 신호가 축삭 돌기를 통해 다른 신경세포로 전달되는 것


## 퍼셉트론 학습규칙

- 1957년 코넬 항공 연구소에 근무하던 Frank Rosenblatt은 MCP 뉴런 모델을 기초로 퍼셉트론(Perceptron) 학습 규칙이라는 개념을 고안
- 하나의 MCP 뉴런이 출력신호를 발생할지 말지를 결정하기 위해 MCP 뉴런으로 들어오는 각 입력값에  곱해지는 가중치 값을 자동적으로 학습하는 알고리즘을 제안
- 이 알고리즘은 머신러닝의 지도학습이나 분류의 맥락에서 볼 때, 하나의 샘플이 어떤 클래스에 속해있는지 예측하는데 사용될 수 있음 


## 퍼셉트론 학습규칙

- x0 ~ xn : 입력되는 값
- w0 ~ wn : x0 ~ xn에 곱해지는 가중치 값
- 순입력 함수 : x0 ~ xn에 가중치 w0 ~ wn을 곱한 값을 모두 더하여 하나의 값으로 만드는 함수
- 활성함수 
    - 순입력 함수의 결과값을 특정 임계값과 비교
    - 순입력 함수 결과값이 이 임계값보다 크면 1, 그렇지 않으면 -1을 출력하는 함수
- 다수의 트레이닝 데이터(입력값과 결과값의 구성)를 이용하여 지도 학습을 수행하는 알고리즘
- 입력되는 특성값 x0 ~ xn에 대한 실제 결과값을 y라고 한다면 y를 활성 함수에 의해-1 또는 1로 변환
    -  이렇게 변환한 값과 퍼셉트론 알고리즘에 의해 예측된 값이 다르면 같아 질때까지 가중치 w0 ~ wn을 업데이트


## 퍼셉트론 학습규칙 2

- 환원 접근법 : MCP 뉴런과 퍼셉트론 모델이 사람 뇌의 단일 뉴런이 작동하는 방법을 흉내내기 위한 방법
    (1)입력되는 특성값에 곱해지는 가중치 w 값들을 모두 0또는 작은 값으로 무작위 할당
    (2)임계값을 정의함(보통 0으로 정의)
    (3)트레이닝 데이터 샘플 x를 순입력 함수를 이용해 가중치와 곱한 뒤 그 총합을 구함
    (4)활성 함수를 이용해 트레이닝 데이터 샘플에 대한 예측 값을 -1 또는 1로 결과가 나오게 함
    (5)트레이닝 데이터 샘플의 실제 결과값에 대한 활성 함수 리턴 값을 예측 값과 비교
- 예측값과 결과가 다르면 모든 가중치 w를 업데이트 하고 (3) 과정부터 다시 시작
[참고](https://snowdeer.github.io/machine-learning/2018/01/02/perceptron/)
- 예측값과 결과값이 동일하면 종료

---
## 논리곱 (AND) 연산에 대한 머신러닝 구현

- 0 AND 0 = 0
- 0 AND 1 = 0
- 1 AND 0 = 0
- 1 AND 1 = 1

### 트레이닝 데이터 
||x0=1|x1|x2|result|
|:----:|:----:|:---:|:---:|:----:|
|가중치|||||
|트레이닝데이터1||0|0|0|
|트레이닝데이터2||0|1|0|
|트레이닝데이터3||1|0|0|
|트레이닝데이터4||1|1|1|


### 논리곱(AND) 연산에 대한 머신러닝 구현

- 가중치는 모두 0으로 설정
- learning rate : 0.1
- 임계값:0

||x0=1|x1|x2|result|활성화함수값|
|:----:|:----:|:---:|:---:|:----:|:----:| 
|초기가중치|W0=0.0|W1=0.0|W2=0.0||    
|트레이닝데이터1||0|0|0|-1|
|트레이닝데이터2||0|1|0|-1|
|트레이닝데이터3||1|0|0|-1|
|트레이닝데이터4||1|1|1|-1|

- 트레이닝 데이터에 대해 순입력 함수 리턴값을 계산
    - w0 X x0 + w1 X x1 + w2 X x2
    - 데이터1 : 0.0 X 1 + 0.0 X 0 + 0.0 X 0 = 0 -> -1
    - 데이터2 : 0.0 X 1 + 0.0 X 0 + 0.0 X 1 = 0 -> -1
    - 데이터3 : 0.0 X 1 + 0.0 X 1 + 0.0 X 0 = 0 -> -1
    - 데이터4 : 0.0 X 1 + 0.0 X 1 + 0.0 X 1 = 0 -> -1

- 활성함수 리턴값 비교
    + -1 : -1
    + -1 : -1
    + -1 : -1
    +  1 : -1

- 데이터 4의 값이 다르므로 가중치 값을 업데이트     
        [수식]

    - w0 = w0 + 0.1(1 – (-1))1 = 0 + 0.2 = 0.2
    - w1 = w1 + 0.1(1 – (-1))1 = 0 + 0.2 = 0.2
    - w2 = w2 + 0.1(1 – (-1))1 = 0 + 0.2 = 0.2
---
## Iris를 데이터를 활용한 퍼셉트론

- 통계학자인 피셔가 소개한 데이터 셋
- 붓꽃 종류 3가지 종(setosa, versicolor, virginica)에 대해 꽃받침(sepal), 꽃잎(petal)의 길이를 정리한 데이터
- 이해하기 쉽고 크기가 작으며 분류에 적합하게 고안된 데이터 셋


|명|의미|데이터타입|
|:----:|:----:|:---:|
|Species|붓꽃의 종. setosa, versicolor, virginica 세 가지 값 중 하나|Factor| 
|Sepal.Width|꽃받침의 너비|Number| 
|Sepal.Length|꽃받침의 길이|Number| 
|Petal.Width|꽃잎의 너비|Number| 
|Petal.Length|꽃잎의 길이|Number| 

--- 
### Iris 실습해보기

- 퍼셉트론 알고리즘을 이용해 꽃 받침 길이와 너비, 꽃 잎의 길이와 너비를 이용해 아이리스 품종을 구분할 수 있는 머신러닝을 수행
- 퍼셉트론은 바이너리 결과를 가지므로 3개의 품종을 동시에 구분할 수 없음
    - 바이너리란  두 가지로 구분되는 것 
- 따라서 Iris-Setosa와 Iris-Versicolor의 2개의 품종을 구분할 수 있도록 학습 시킴 
---