import numpy as np
import pandas as pd
import random
import math

import matplotlib.pyplot as plt

class Machine():
    # 속성 - 확률
    def __init__(self,p):
        # 확률이라는 속성을 부여 
        self.percentage = p
        # 외부에서 입력된 p로 인해 값이 초기화
        
    # 보상
    def reward(self):
        # 머신 선택시 보상 지급 
        # 세팅된 확률보다 랜덤 값이 적으면 1 아니면 0 
        if self.percentage > random.random():
            return 1.0
        else:
            return 0.0

# 랜덤 값의 범위 확인
# print([ random.random() for n in range(10)])

# Machines = [ Machine(0.3), Machine(0.5), Machine(0.9) ]
# print(Machines) # 확인용

class Engine():
    # 초기화 함수 -> 알고리즘에 필요한 값을 초기화
    def initialize(self):
        # 값을 초기화
        pass

    def select_machin(self):
        # 기계를 선택
        pass

    # 폴리시 업데이트 -> 각 액션마다
    def policyUpdate(self):
        # 파라미터를 핸들링
        pass
    
    # 알고리즘 이름 출력
    def Algo_Naming(self):
        pass
    

"""
# Engine Class
- 표준 인터페이스
- 알고리즘 2개를 사용 예정 
"""

# EpsilonGreedy 알고리즘 이용 
# Engine을 상속 
class E_Greedy_Engine(Engine):

    """
    # ε-greedy 알고리즘

    - 확률 ε(0~1)으로 랜덤하게 행동을 선택한다.
    - 머신을 선택하는 행위
    - 확률 1-ε는 현재 가치가 가장 높은 머신을 선택한다.
    - 이런 확률값 중 가장 좋은 성능을 내는값이 0.1인 경우가 많다.
    """
    # 0.1 이 성능이 좋기 때문에 사용 
    def __init__(self, epsilon = 0.1 ):
        # 속성부여 
        self.epsilon = epsilon  # 탐험하는 확률 

    # 초기화 함수 -> 알고리즘에 필요한 값을 초기화
    def initialize(self, machin_cnt):
        # 값을 초기화 -> 머신의 시행 횟수, 머신의 경험(가치)
        self.n = np.zeros(machin_cnt) # machin_cnt : 머신의 개수 
        # 각 경험을 보유해야함 -> 시도, 가치(보상)을 배열에 저장 
        self.v = np.zeros(machin_cnt)  # 이전 경험 
        
    def select_machin(self): # 엡실론 그리디 알고리즘 핵심
        # 기계를 선택 -> 랜덤하게 ->
        # 탐험과 활용 혹은 탐색과 이용
        # 탐색 
        if self.epsilon > random.random(): # 0.1(self.epsilon)보다 난수 값이 작으면 
            # 랜덤하게 머신을 선택 : 0 <= ~ < len(self.n) 
            # => 0 <= x < 3
            # => 0, 1, 2중에 하나
            return np.random.randint(0, len(self.n))
        else:
            # 이용 
            # 가치가 높은 팔의 인덱스를 구해서 돌려준다.
            # -> 팔번호 : 0, 1 ,2 중 하나
            return np.argmax(self.v)

    # 폴리시 업데이트 -> 각 액션마다
    def policyUpdate(self, choice_machine, new_reward):
    # 어디서 choice_machine, reward를 받는지 확인 할 것 
        # 파라미터를 핸들링

        # 에피소드 당 머신의 동작 횟수를 증가
        self.n[choice_machine] += 1

        # 현 에피소드에 선택한 머신의 경험을 증가 시킨다. 
        # (n-1)/n*Vt-1 + (1/n)*Rt 
        n = self.n[choice_machine]
        # 직전의 가치 
        v = self.v[choice_machine]

        '''
        현재 행동 후 현재의 가치 = (처음부터 이전 시도까지의 수행양) * 이전번 가치(v) 
                                + (1/전체 시도 횟수) * 현재 받은 보상

        '''

        # 수식을 코드화 
        self.v[choice_machine] = ((n-1)/n)*v + (1/n) * new_reward
    
    # 알고리즘 이름 출력
    def Algo_Naming(self):
        return 'ε-greedy 알고리즘 이용'



def simulator(algo, Machines, simulator_cnt, episode_cnt):

    times   = np.zeros(simulator_cnt * episode_cnt) #'횟수'
    rewards = np.zeros_like(times)#'보상'

    # 시뮬 동작
    for action in range(simulator_cnt):
        # 주어진 팔의 개수만큼 자료구조를 생성 -> 0으로 초기화 
        algo.initialize(len(Machines))

        for time in range(episode_cnt):
            offset         = episode_cnt * action
            index          = offset + time
            times[index]   = time + 1 
            choice_machine = algo.select_machin()
            new_reward     = Machines[choice_machine].reward()
            rewards[index] = new_reward
            # 경험을 업데이트 
            algo.policyUpdate(choice_machine, new_reward)

    return times, rewards



# 시뮬레이터     
# 머신을 준비 -> 각 확률을 부여 
Machines = [ Machine(0.3), Machine(0.5), Machine(0.9) ]  # 30%, 50%, 90%
# print(Machines) 
# 1개의 알고리즘 
# algos = [E_Greedy_Engine()]
# 알고리즘 별로 시뮬레이션을 1000번
SIMULATION_COUNT = 1000
# 1번의 시뮬레이션에서는 250의 에피소드가 존재
EPISODE_COUNT    = 250

# for algo in algos:
result = simulator(E_Greedy_Engine(), Machines, SIMULATION_COUNT , EPISODE_COUNT )
# print(result)
df      = pd.DataFrame( {'times':result[0], 'rewards':result[1]} )
print('='*50)
print(df['rewards'].value_counts(), df['rewards'].count() )
print('='*50)
tmp     = df.groupby( 'times' ).mean()
# 시각화(선형 차트)
plt.plot( tmp, label=E_Greedy_Engine().Algo_Naming() )

# 그래프 표시
plt.xlabel('Episode')
plt.ylabel('Reward Average')
plt.legend(loc='best')
plt.show()