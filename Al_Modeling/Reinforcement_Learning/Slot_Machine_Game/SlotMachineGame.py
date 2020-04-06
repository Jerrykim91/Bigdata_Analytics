# 구조 
'''
- SlotMachineGame # 슬롯머신 
  L SlotArm Class
  L GameEngine Class
    L EpsilonGreedyEngine Class # 알고리즘 - 엡실론 그리디
    L UCB1Engine Class # 알고리즘 - UCB1
  L GameSimulator Class or function

https://github.com/bgalbraith/bandits

'''
# 필요 패키지 
import numpy as np
import pandas as pd
import random
import math

import matplotlib.pyplot as plt
# %% %matplotlib inline

# 머신 겉
class SlotArm():
  # 슬롯이 하는일 
  # 팔을 당긴다 -> 엔진에 
  # 동작과 동시에 확률을 가진다. -> 자기자신 ,확률
  # 보상이 주어진다.



  # 생성자 

  # 보상 지급
  pass


