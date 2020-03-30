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
%matplotlib inline

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
        if self.p > random.random(0) : 
            return 1.0
        else
            return 0.0
    pass

# 랜덤 값의 범위 확인?
print([random.ran() for n in range(10)])

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






# 게임 시뮬레이터 생성 
# 1단계 - 슬롯머신의 팔을 3개 준비한다. 
# 3개의 Arm은 reward(1.0)를 지급하는 확률이 다르다.
arms = [ SlotArm(0.3), SlotArm(0.5), SlotArm(0.9) ]
