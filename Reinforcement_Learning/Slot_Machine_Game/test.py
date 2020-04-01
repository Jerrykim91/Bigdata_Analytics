# 구조 
'''
- SlotMachineGame
  L SlotArm Class
  L GameEngine Class
    L EpsilonGreedyEngine Class
    L UCB1Engine Class
  L GameSimulator Class or function
'''

# 필요 패키지 
import numpy as np
import pandas as pd
import random
import math

import matplotlib.pyplot as plt
# %matplotlib inline
# %% %matplotlib inline


# class SlotArm()
class SlotArm():

    # __init__() -> 생성자 함수 생성 -> 초기화
    def __init__(self, p): # p : 객체를 만들 때 주어지는 확률값
        self.p = p 
        
    # draw - 얘가 보상을 지급 
    def draw(self):  # 보상? # 세팅 값은 어딨는데 ? 
        # 뭔가 그리는데 거기값이 0 아니면 1 -> 랜덤 값
        # 랜덤 값 : 0 ~ 1 
        if self.p > random.random() : 
            return 1.0
        else:
            return 0.0
    pass # ??

# 랜덤 값의 범위 확인
print([ random.random() for n in range(10)]) 


"""
# GameEngine Class
    - 알고리즘 2개에 대한 표준 인터페이스 제공 

"""
# 멤버 변수의 파라미터들은 구현하면서 설정
# 알고리즘 검토 후 필요 변수 확인 후 조정 


# class GameEngine() - 일단 틀 생성 
class GameEngine():
    # 초기화 = 생성자 
    # 알고리즘에 필요한 값을 초기화 
    def initialize(self):
        pass

    # arm을 선택
    def select_arm(self):
        pass

    # 액션 마다의 정책(policy-룰)조정
    # 파라미터를 조정
    def policyUpdate(self): 
        pass

    # 알고리즘 이름을 출력 
    def getName(self):
        pass 

    pass


"""
# ε-greedy 알고리즘

- 확률 ε(0~1)으로 랜덤하게 행동을 선택한다.
    - arm을 선택하는 행위
- 확률 1-ε는 현재 가치가 가장 높은 팔을 선택한다.
- 이런 확률값 중 가장 좋은 성능을 내는 값 0.1인 경우가 많다.

"""
# from IPython.display import Image
# Image( '../data/ε-greedy.jpeg' ) # ε-greedy.jpeg
# 현재 행동후 현재의 가치=
# (처음부터 이전 시도까지의 수행양)* 이전번 가치 + (1/전체 시도 횟수)*현재 받은 보상


# class EpsilonGreedyEngine() -> 상속 받은건가 ?
class EpsilonGreedyEngine(GameEngine):

    def __init__(self, epsilon):
        self.epsilon = epsilon  # 탐색하는 확률 
        pass
    
    # initialize()
    def initialize(self, n_arms):
    # n_arms:arm의 개수 - 경험을 들고 있어야 하므로, 시도, 가치(보상)-> 배열에 저장 

        self.n = np.zeros(n_arms) # 각 팔의 시행 횟수 -> [0,0,0]
        self.v = np.zeros(n_arms) # 각 팔의 가치      -> [0,0,0]
        pass 
  

    # select_arm() -> 랜덤하게 arm을 선택 -> 정책에 가까움 
    def select_arm(self):
        if self.epsilon > random.random():  # 0.1 보다 난수 값이 적으면 
            # 랜덤하게 팔을 선택 
            # 0<= ~ < len(self.n) => 0 <= x < 3 => 0, 1, 2중에 하나
            return np.random.randint(0, len(self.n))
        else: # 이용
            # 가치가 높은 팔의 인덱스를 구해서 리턴-> 팔번호 : 0, 1, 2 중에 하나
            return np.argmax(self.v) # 가장 큰 값의 인덱스번호를 리턴 # 1)argmax *
        pass  


    # valueUpdate()
    def valueUpdate(self, choice_arm, reward ): # 턴 당 한번 

        # 1. arm의 수행 횟수를 증가
        self.n[ choice_arm ] += 1

        # 수식 (n-1)/n*Vt-1 + (1/n)*Rt  -> arm의 가치를 증가
        n = self.n[ choice_arm ]
        # 직전의 가치
        v = self.v[ choice_arm ] # vt

        self.v[ choice_arm ] = (n-1)/n*v-1 + (1/n)*reward
        pass

    # getName()
    def getName(self):
        # 리턴 값 -> ε-greedy 알고리즘 이용한 값
        return 'ε-greedy 알고리즘 이용'


# UCB1 알고리즘 추가 
class UCB1Engine(GameEngine):
    # 왜 인잇함수는 없을까 ?
    # 각 타입 확인 할 것 
    # 왜 거기 들어가는지 확인할 것 
    def initialize(self):
        # 경험을 keep
        # 시행 횟수 
        # 팔의 가치 
        # 성공 횟수
        pass

    def select_arm(self, parameter_list): 
        # 모든 암을 한번씩 선택
        # 그중 값이 큰 암을 선택 -> argmax
        pass
    
    def valueUpdate(self, parameter_list):  # self, choice_arm, reward
        # 선택한 암의 시행횟수(행동 횟수) + 1 -> 시도에 대한 횟수 증가 

        # 만약 보상을 받았다면, 성공 횟수를 증가 => 총 보상 + 1

        # 시행 횟수가 0인 팔이 존재할 경우 -> 갱신하지 않는다. 

        # UCB1의 수식에 의해 모든 팔에 대한 가치 갱신
            # 성공률       = (개별팔의성공수)/(개별팔의시행횟수)
            # 바이어스     = ( (2*math.log(모든시행횟수))/(개별팔의시행횟수) )**0.5
            # 개별팔의가치 = 성공률 + 편향(바이어스)
        # 
        pass
    
    def getName(self):
        return 'UCB1 알고리즘'
    pass


# 게임 시뮬레이터 생성 



# 머신 준비 ---------------------------
arms = [ SlotArm(0.3), SlotArm(0.5), SlotArm(0.9) ] # 슬롯머신의 팔을 3개 준비 
# 3개의 Arm은 reward(1.0)를 지급하는 확률이 다르다.

# 알고리즘 
algos = [EpsilonGreedyEngine(0.1)] # 2개의 알고리즘 필요 













"""
argmax : 'https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221164668953&proxyReferer=https%3A%2F%2Fwww.google.com%2F'
"""



# %%
