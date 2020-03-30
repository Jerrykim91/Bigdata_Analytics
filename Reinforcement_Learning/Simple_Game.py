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
        if 조건식 : 
            return 1.0
        else
            return 0.0
    pass

# 랜덤 값의 범위 확인?
print([random.ran() for n in range(10)])

# 게임 시뮬레이터 생성 
# 1단계 
