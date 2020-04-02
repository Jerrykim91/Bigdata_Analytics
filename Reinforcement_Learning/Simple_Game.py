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
    # 초기화 -> 확률값 초기화(외부에서 주입)
    # 생성자 함수 생성 
    # p : 객체를 만들 때 주어지는 확률값
    def __init__(self, p):
        # 맴버 변수 self.p가 만들어지고, 외부에서 입력된 p로 인해 값이 초기화 
        self.p = p 
        
    # 팔 선택시 보상 지급 처리 -> 세팅된 확률보다 랜덤값이 적으면 -> 1.0
    # 아니면 0.0 
    # draw() - 얘가 보상을 지급 
    def draw(self): 
        # 랜덤 값 : 0 ~ 1 
        if self.p > random.random() : 
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

# 멤버 변수의 파라미터들은 구현하면서 설정
# 알고리즘 검토 후 필요 변수 확인후 조정 


# class GameEngine() - 일단 틀 생성 
class GameEngine():
    # 초기화 = 생성자 
    # 알고리즘에 필요한 값을 초기화 
    def initialize(self):
        pass

    # 팔(arm)선택
    def select_arm(self):
        pass

    # 액션 마다의 정책(policy-룰)조정
    # 파라미터를 조정
    def policyUpdate(self):
        pass

    # 알고리즘 이름을 출력 
    def getName(self):
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
# 현재 행동후 현재의 가치=(처음부터이전시도까지의수행양)*이전번가치 
#                         + (1/전체시도횟수)*현재받은보상


# 클래스로 구현
# class EpsilonGreedyEngine() -> 상속 받은건가 ?
class EpsilonGreedyEngine(GameEngine):
# 해당 알고리즘에서 팔을 선택시 랜덤 or 이미 선택해 본 것 중 선택
# 경험해본 팔중에 가치가 높은 팔을 선택할 것이니 그것을 
# 결정하는 기준값, 통상 0.1이 가장 좋은 성능을 냈다.
    def __init__(self, epsilon = 0.1):
        self.epsilon = epsilon  # 탐색하는 확률 
        pass

    # n_arms:arm의 개수 - 경험을 들고 있어야 하므로, 시도, 가치(보상)-> 배열에 저장 
    def initialize(self, n_arms):
        self.n = np.zeros(n_arms) # 각 팔의 시행 횟수 -> [0,0,0]
        self.v = np.zeros(n_arms) # 각 팔의 가치      -> [0,0,0]
        pass 
  
    # select_arm() -> 랜덤하게 arm을 선택 -> 정책에 가까움 
    # 탐험과 활용 혹은 탐색과 이용
    def select_arm(self):
        # 탐색 
        if self.epsilon > random.random():  # 0.1 보다 난수 값이 적으면 
            # 랜덤하게 팔을 선택 
            # 0<= ~ < len(self.n) => 0<= x < 3 => 0, 1, 2중에 하나
            return np.random.randint(0, len(self.n))
        else: # 이용
            # 가치가 높은 팔의 인덱스를 구해서 리턴-> 팔번호 : 0, 1, 2 중에 하나
            return np.argmax(self.v)
        pass  


    # valueUpdate() - 턴 당 한번 
    def valueUpdate(self, choice_arm, reward ):

        # 1. 이번 에피소드에 arm의 수행 횟수를 증가
        self.n[ choice_arm ] += 1

        # 2. 이번 에피소드에 선택한 arm의 가치를 증가한다.
        # 수식 (n-1)/n*Vt-1 + (1/n)*Rt 
        n = self.n[ choice_arm ]
        # 직전의 가치
        v = self.v[ choice_arm ]

        self.v[ choice_arm ] = ((n-1)/n)*v + (1/n) * reward
        pass

    def getName(self):
        # 리턴 값 -> ε-greedy 알고리즘 이용
        return 'ε-greedy 알고리즘 이용'


"""
# UCB1 알고리즘

- 절차
    - 1. 선택한 팔의 시행 횟수 +1
    - 2. 성공시(보상을 받으면), 선택한 팔의 성공 횟수 +1
    - 3. 시행 횟수가 0인 팔이 존재하는 경우, 가치를 갱신하지 않는다 => 0으로 나눌수가 없어서
    - 4. 시행 횟수가 모두 0이상이면, 팔의 가치에 대해서 탐색과 이용에 대한 균형을 잡는다는 대전에 하에, 모든 팔의 가치를 갱신한다.

    - 모든 팔을 한번 이상 사용할때까지는 가치 갱신을 하지 않는다 => 탐색
    - 모든 팔을 최소 1회 이상 사용해 봤다면, 전체 arm에대 가치 갱신을 시도한다.

"""
# Image( '/content/drive/My Drive/Colab Notebooks/2기/dl_data/UCB1.jpeg', width=400 )
"""
    algo = '' 
    arms = '' 
    simulator_count = ''
    episode_count = ''
    
"""
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


# 시뮬레이션 
def simulator_play(algo, arms, simulator_count, episode_count):
    # 몇번의 시도만에 (0~249회) 보상이 높은 팔만 선택하게 되는가 ? 
    # 위의 실험을 1000번 수행 
    # 저장 정보 크기(0,1,2,..249,0,1,2,..249, ... 249 <= 1000*250)
    # 저장 정보 내용 시도 정보, arm에서 받은 보상값
    
    times   = np.zeros( simulator_count * episode_count) # 횟수
    rewards = np.zeros_like( times ) # 보상(0.0 or 1.0)

    # 시뮬 가동 
    for sim in range(simulator_count):
        # 주어진 팔의 개수만큼 자료구조를 생성하면서 0으로 초기화 
        # 이전 시뮬레이션 단계의 250회 행동 -> 흔적은 다 사라진다. 
        algo.initialize(len(arms))
        # 250회 에피소드 시뮬레이션 수행 -> 250회 arm 선택 -> 
        # 가치 업데이트 -> 정책 변화?(없다, )

        for time in range(episode_count): # 0 ~ 249번
            # 데이터를 1차 행렬(배열)(times or rewards)에 데이터를 다 넣다 보니
            # 데이터를 정확한 위치에 넣을수 잇는 offset 계산이 필요
            offset           =  episode_count * sim # (0,250, 500,...)=>(250*0, 250*1, 250*2,...)
            # 데이터를 넣어야 하는 위치
            index            =  offset + time
            # 시도 횟수를 기록 
            times[ index ]   = time + 1  # [1,..250,1,..250,...1,..250]
            # 팔, Arm을 선택(행동을 수행, 정책을 기반으로 판단하여 행동을 수행)
            # 알고리즘에서 팔을 선택하고
            choice_arm       = algo.select_arm()
            # 해당 팔을 당겨서, 리워드를 받는다
            reward           = arms[choice_arm].draw()
            # 리워드를 기록 
            rewards[ index ] = reward
            # print(rewards)
            # 그 리워드를 가지고 가치 업데이트
            algo.valueUpdate( choice_arm, reward )
    
    return times , rewards


# 게임 시뮬레이터 생성 
# 1단계 - 슬롯머신의 팔을 3개 준비한다. 
# 3개의 Arm은 reward(1.0)를 지급하는 확률이 다르다.
arms = [ SlotArm(0.3), SlotArm(0.5), SlotArm(0.9) ] # 30%, 50%, 90%

# 2개의 알고리즘 필요 
algos = [EpsilonGreedyEngine()]

# 알고리즘별로 시뮬레이션을 1000번 한다. 
SIMULATION_COUNT = 1000
# 1번의 시뮬레이션에서는 250의 에피소드가 존재
EPISODE_COUNT    = 250

for algo in algos: # 알고리즘 별로 시뮬레이션 
    result = simulator_play( algo, arms, SIMULATION_COUNT, EPISODE_COUNT )
    df = pd.DataFrame( {'times':result[0], 'reward':result[1]} )
    tmp = df.groupby( 'times' ).mean()
    # 시각화 (선형차트)
    plt.plot( tmp,  label=algo.getName() )

# 그래프 표시
plt.xlabel('Episode')
plt.ylabel('Reward Average')
plt.legend(loc='best')
plt.show()

# print(result[0].shape, result[1].shape)


# print(df.shape)
# 슬롯머신의 암으 선택하는 횟수가 증가될수록 - 보상을 많이주는 암을 선택 
# 보상 값이 주로 1인 것을 보면, 보상을 잘주는 팔만 선택한것을 알수 있다. 
# print(df.tail(100))


# print(tmp.shape)

# print(tmp.tail(1))

# 슬롯머신의 암을 선택하는 횟수가 증가 될수록 보상을 많이 주는 암을 선택하는 경향이 보인다.
# 보상 값이 주로 1인 것을 보면 보상을 잘주는 팔만 선택하고 있다는 것을 알 수 있다.
# print(df.tail(100)) 

