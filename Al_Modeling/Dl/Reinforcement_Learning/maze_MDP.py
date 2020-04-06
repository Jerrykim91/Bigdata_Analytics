# MDP
"""
# 마르코프 결정 과정 (Markov Decision Process:MDP)

- 벨만 방정식이 성립하기 위해, 환경이 MDP를 따라야 한다.
- 다음 상태가 현재 상태에서 선택한 행동에 따라 확정되는 시스템을 의미
    - 만약, 과거 상태에 의해 다음 상태가 결정되는 환경은 마르코프 결정 과정을 따르는 환경이 아니다

- 벨만 방정식으로 부터 행동 가치 함수를 학습하는 방법
    - Sarsa, Q 학습 
- 벨만 방정식으로 부터 상태 가치 함수를 학습하는 방법
    - Dueling Network, A2C (생략)

"""
# 패키지 임포트



# %%
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from matplotlib import animation
from IPython.display import HTML
