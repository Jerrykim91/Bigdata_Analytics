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
# %%

# Slot Machine Arm class
class SlotArm():
    # 초기화 -> 확률값 초기화(외부에서 주입)
    # 생성자 함수 생성 ㄴ
    def __init__(self,p):
        # 맴버 변수 self.p가 만들어지고, 외부에서 입력된 p로 인해 값이 초기화 
        self.p = p 
        
    # 팔 선택시 보상 지급 처리 -> 세팅된 확률보다 랜덤값이 적으면 -> 1.0
    # 아니면 0.0  
    def draw(self):
        # 랜덤 값 : 0 ~ 1 
        if self.p > random.random(0) : 
            return 1.0
        else:
            return 0.0
    pass

# 랜덤 값의 범위 확인?
print([ random.random() for n in range(10)])


"""
# GameEngine Class
    - 알고리즘 2개에 대한 표준 인터페이스 제공 
"""

class GameEngine():
    # 초기화 = 생성자 
    # 알고리즘에 필요한 값을 초기화 
    def initialize(self):
        pass

    # 팔(arm)선택
    def select_arm(self):
        pass

    # 원 액션이 완료된 후 정책(policy)을 조정 -> 파라 미터를 조정한다.  
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

# 클레스로 구현
class EpsilonGreedyEngine(GameEngine):
# 해당 알고리즘에서 팔을 선택시 랜덤 or 이미 선택해 본 것중 선택
# 경험해본 팔중에 가치가 높은 팔을 선택할 것이니 그것을 
# 결정하는 기준값, 통상 0.1이 가장 좋은 성능을 냈다.
    def __init__(self, epsilon):
        self.epsilon = epsilon  # 탐색하는 확률 
        pass

    def initialize(self, n_arms):
        self.n = np.zeros[n_arms] # 각 팔의 시행 횟수 -> [0,0,0]
        self.v = np.zeros[n_arms] # 각 팔의 가치      s-> [0,0,0]
        pass 
  
    # 랜덤하게 팔을 선택 
    def select_arm(self):
        if self.epsilon > random.random():  # 0.1 보다 난수 값이 적으면 
            # 랜덤하게 팔을 선택 
            # 0<= ~ < len(self.n) => 0<= x < 3 => 0, 1, 2중에 하나
            return np.random.randint(0, len(self.n))
            pass
        else:
            # 가치가 높은 팔에서 선택
            pass
        pass  

    def policyUpdate(self):
        pass

    def getName(self):
        pass


from IPython.display import Image
Image( '../data/ε-greedy.jpeg' ) # ε-greedy.jpeg
# 현재 행동후 현재의 가치=(처음부터이전시도까지의수행양)*이전번가치 
#                         + (1/전체시도횟수)*



# 게임 시뮬레이터 생성 
# 1단계 - 슬롯머신의 팔을 3개 준비한다. 
# 3개의 Arm은 reward(1.0)를 지급하는 확률이 다르다.
arms = [ SlotArm(0.3), SlotArm(0.5), SlotArm(0.9) ]

# 2개의 알고리즘 필요 
algos = [EpsilonGreedyEngine(0.1)]



# %%
