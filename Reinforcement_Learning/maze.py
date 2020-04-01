"""
#  미로 게임 
# 
"""
# 텐서 2.0 대비
# ! pip install tensorflow==1.15


# 모듈 가져오기 
import numpy as np
import matplotlib.pyplot as plt
# %%%matplotlib inline

# 애니메이션 처리
from matplotlib import animation, rc
# 코렙에 html을 삽입하는 모듈
# from IPython.display import HTML # 이거는 차차 해결해보자 뭘 구현하실지 모르니 
from IPython.display import display, HTML

"""
#  베이스 생성
- 게임 베이스 그리기 : 미로 게임판 생성 
- 미로게임판은 입구와 출구가 각각 1개만 존재 
- 바둑판 같은 사각형에 열린곳과 막힌곳이 존재
- 에이전트(마우스)는 4방향으로 이동이 가능 
    - 상:0, 우:1, 하:2, 좌:3, 시계방향
- 게임판은 위에서 투시해서 직각으로 보는 뷰를 사용 
- 게임판은 3x3

"""
# 미로 판의 크기 
fig = plt.figure(figsize=(3,3))

# 벽그리기 
plt.plot( [0,3], [3,3], color='k' ) # 맨 상단 가로 벽
plt.plot( [0,3], [0,0], color='k' ) # 맨 하단 가로 벽
plt.plot( [0,0], [0,2], color='k' ) # 왼쪽 세로 벽  -> 입구
plt.plot( [3,3], [1,3], color='k' ) # 오른쪽 세로 벽 -> 출구

plt.plot( [1,1], [1,2], color='k' ) # 내부벽 
plt.plot( [2,3], [2,2], color='k' ) # 내부벽
plt.plot( [2,1], [1,1], color='k' ) # 내부벽
plt.plot( [2,2], [0,1], color='k' ) # 내부벽

# 각 포인트에 숫자 표현하기 -> 연속적으로 그린다. 
# 이거는 2D차트라서 1/4 분면 
# pc는 4/4분면 
for n in range(3):
    for m in range(3): # 사이즈 : size=20,
        plt.text( n + 0.5, (3.0) - m - (0.5), str( n + m * 3 ), ha='center', va='center' ) 
        
# 마우스 그리기(원) # '#dadada', '#50bcdf'
mouse = plt.plot([0.5],[2.5], marker='o', color ='#dadada', markersize= 40 )

# 눈금, 테두리 정의 
plt.tick_params( axis='both', which='both', bottom=False, top=False,
            labelbottom=False, right=False, left=False, labelleft=False )
# 화면에 보이기
plt.box('off')
plt.show()



"""

"""
# 파라미터 θ의 초기값 준비
# 미로게임판을 기반으로 설계 (차후에 자동화하면 좋겟다)
theta_0 = np.array([
  # [상, 우, 하, 좌], 
  [ np.nan, 1, 1,np.nan ], # 0
  [ np.nan, 1, 1,1 ], # 1
  [ np.nan, np.nan, np.nan,1 ], # 2
  [ 1,np.nan , 1,np.nan ], # 3
  [1 , 1, np.nan, np.nan], # 4
  [ np.nan, np.nan, 1, 1], # 5
  [ 1, 1, np.nan,np.nan ], # 6
  [ np.nan, np.nan, np.nan, 1], # 7 포인트  
])
# 8 포인트는 골인 지점이므로 매개변수를 고려하지 않음


# 확률 = 개별값/전체 총합 
a = theta_0[0]
# print(a)
a / np.nansum(a)
# print(a / np.nansum(a))


a = theta_0[0]
b = np.exp(a)   # 지수함수 
b/np.nansum(b)


# nan을 0으로 변환, nan을 수치로 변환s
np.nan_to_num(b/np.nansum(b))
# print(np.nan_to_num(b/np.nansum(b)))


# softmax 처리 함수 구현, 사용
# label이 다양한 경우 , 3-class 이상의 분류를 
# 목적으로 하는 딥러닝 모델의 출력층으로 보내는 활성화 함수
# softmax을 처리한 구성원들의 총합이 1이 된다 => 행동결정의 확률
# 0 ~ 1사이로 theta_0가 만들어져야 하위 작업을 진행
# 세타가 인자 
def mySoftmax(theta):
  # 1. 세타와 같은 크기로 배열을 생성, 초기값은 0 
  output = np.zeros_like(theta)
  # print(output)
  # 2. 세타를 지수함수로 처리(결과만 봤을 때 안해도 ok)
  exp_theta = np.exp(theta)
  # print(exp_theta)
  # print(exp_theta.shape[0])
  # 3. 한줄 씩 개별값/ 총합등 처리하여 1번 자료구조에 반복적으로 담는다.
  for i in range(exp_theta.shape[0]):
    # print(i)
    # 한줄씩 처리해서 한줄싹 담는다. 
    output[i, :] = exp_theta[i, :] / np.nansum(exp_theta[i, :])
    # print(i)
    # 4.데이터를 모두 담은 배열 리턴(nan 처리)
  return np.nan_to_num(output)
  
# print(mySoftmax(theta_0))


# 정책에 따른 행동 정보 획득
# 인자 : policy, state 
# policy : 각 위치에 대한 행동을 선택할수 있는 정책
# state  : 에이전트의 현재 위치

def getAction(policy, state):
  # 리턴값을 선택하는 기준 -> 정책을 기준으로 선택 -> 정책
  # 현태 위치에서 갈 수 있는 곳들중 랜덤하게 선택 -> 행동이 중요하다. 가치 x -> 가중치 x 

  # 리턴값 => 현재 위치에서 0:상 1:우 2:하 3:좌로 이동하는 것
  return np.random.choice([0,1,2,3], p = policy[state])


# 행동에 따른 다음 상태(위치정보) 획득 
# 화면 처리(에이전트가 이동을 실제로 해야하므로, 그 이동량을 계산)
# 미로 게임의 판은 3x3이다. 
# 좌, 우 이동 => 위치 변동량 => (+ or -)1 => 0 <- 1(현재위치) -> 2
# 상, 하 이동 => 위치 변동량 => (+ or -)3 => 1 <- 4(현재위치) -> 7

# 인자 : curState, nextAction
# curState  : 현재 상태(본 게임에서는 에이전트의 위치) 
# nextAction: 현재 상태에서 취해지는 다음 행동 (0, 1, 2, 3)
def getNextState(curState, nextAction):

  if nextAction == 0:   # 상
    return curState - 3 # 위로 가는 액션을 취하면, 다음 위치는 현재위치-3이다
  elif nextAction == 1: # 우
    return curState + 1
  elif nextAction == 2: # 하
    return curState + 3
  elif nextAction == 3: # 좌
    return curState - 1
  
  # 리턴 : NextState

# 시뮬레이션 상 데이터를 담을 자료구조 준비 
# [[에이전트의상태(위치), 행동(상,우,하,좌)], ...., [8, np.nan]]
# [8, np.nan] : 최종위치, 에피소드의 종료, 시뮬레이션상에서 파라미터 갱신시
# 비대상이 될 것이다. 

# 초기 데이터 
AGENT_FIRST_STATE = 0
AGENT_LAST_STATE = 8
#st_act_his = [ [AGENT_FIRST_STATE, np.nan] ]

# 현재 정책 
theta = mySoftmax(theta_0)

# 시뮬레이션 준비 
# 에피소드 1만 수행한다.
# 인자 : updatedPolicy
# updatedPolicy : 갱신된 정책이 들어온다

def simulation_MIRO(updatedPolicy):
  # 최초 상태에 대한 내역만 가지고, 이동에대한 히스토리를 담을 자료 구조 준비 
  st_act_his = [ [AGENT_FIRST_STATE, np.nan] ]
  # 에이전트 현재위치는 변수로 받겠다. 
  # 반복문이 돌면서 현재위치가 바뀌니까 
  cur_agent_state = AGENT_FIRST_STATE
  # 에이젼트의 상태가 8이 될때까지 이하 내용 반복 => 미로 탈출하기
  while True:
    # 에이젼트 현재상태 
    # 현재위치 -> 정책 -> 다음 행동 결정 -> 에이전트 이동 : 행동수행 => 에이전트의 상태가 변경 
    # 1. 정책에 따른 현재 상태(위치)에서 행동 얻기 
    agent_action      = getAction( updatedPolicy, cur_agent_state )
    # 2. 해당 행동에 따른 다음 상태(위치)를 획득(0~8)
    next_agent_state  = getNextState( cur_agent_state, agent_action )
    # 3. 에이전트의 이동 내역을 정리 
    # [ [0, np.nan] ] 
    # 3-1. 현재 위치에서 이동한 방향(액션)을 기록
    # 항상 리스트의 마지막 맴버의 2번째 내용을 nan에서 구한값으로 변경
    st_act_his[-1][-1]= agent_action
    # [[0, agent_action]]
    # 3-2. 새로운 위치에 대한 로그를 추가 
    st_act_his.append([next_agent_state,np.nan])
    # [ [0, agent_action], [next_agent_state, np.nan] ]
    # 4. 다음 상태에 대한 위의 과정을 동일하게 반복하기 위해 
    # cur_agent_state를 next_agent_state값으로 갱신한다.
    cur_agent_state = next_agent_state

    # if 에이전트의 상태 == AGENT_LAST_STATE:
    if next_agent_state == AGENT_LAST_STATE:
      break
    # print(st_act_his)
  return st_act_his

a_s_his = simulation_MIRO( theta )
# print( '에피스드 1의 총 액션수(스텝수)', len(a_s_his)-1 ) # 매번 수가 다르다. 



"""

# 에피스드1 이 끝날때까지 에이전트는 len(a_s_his)-1번 이동했는데
그 중에서 에이전트가 1번 위치에 있었을 때, 1(오른쪽을) 몇번을 선택했는가? = N(s,a)
s = 1
a = 1 
for s0, a0 in a_s_his :
  if s0==s and a0==a : 
    print(s0, a0) 


# N(s,a)
print( len([ 1 for s0, a0 in a_s_his if s0==s and a0==a ]) )
print( sum([ 1 for s0, a0 in a_s_his if s0==s and a0==a ]) )
# N(s)
print( sum([ 1 for s0, a0 in a_s_his if s0==s ]) )

"""


# 정책 경사법을 적용한, 파라미터 θ 갱신 처리(핵심)
# 수학 공식도 코드랑 같다 풀어서 각 의미들이 변수에 담겨 있는것과 같다. 그렇기 때문에 공식을 코드화 할 경우
# 모두 풀어서 나열하면서 쌓아가면 조금도 수월하게 수식을 코드화 가능하다.  

# 인자 : theta_0, act_st_his + policy  -> theta_0, policy, act_st_his
# theta_0     : 미로 게임이 만들어지고 나서 각 상태별로 취할 수 있는 행동을 기술(정책)
# policy       : theta_0를 softmax()를 통과시켜서 확률적으로 정리한 정책
# act_st_his  : 한번의 에피소드가 종료되고 난 이후의 히스토리

def update_theta(theta_0, policy, act_st_his):

  eta = 0.1             # 학습 계수 
  # 학습량의 계수는 사용자에 따라 바뀔 수 있다. 
  total = len(act_st_his) - 1     # 에피소드 1이 종료 될 때까지 발생한 총 액션 수(행동수), 스탭 수 
  state_cnt, act_cnt = theta.shape  # 상태의 총 수(8개), 액션의 총 수(4개)
  # print(total, state_cnt, act_cnt)
  
  # 정책을 갱신하여 담을 자료 구조 
  upTheta = theta_0.copy()
  # 정책 갱신 : 파라미터 세터의 변동량 계산 
  for s in range( state_cnt ): # 0번, 1번, 2번, .. 7번위치 : 상태
    for a in range( act_cnt ): # 0:상, 1:우, 2:하, 3:좌    : 액션
      # np.nan이 아닌것만 갱신
      if not (np.isnan(theta_0[s,a])):
        # 변동량 계산
        
        # 특정 상태에서 특정행동을 몇번했는가? = 상태 s에서 행동 a를 선택한 횟수
        n_sa = len([ 1 for sa in act_st_his if sa==[s,a] ])
        # 특정 상태에서 특정행동을 하는 정책값(확률) = 상태 s에서 행동 a를 선택하는 정책 
        p_sa = policy[s, a]
        # 특정 상태에서 행동을 몇번했는가? = 상태 s에서 무엇인가 행동을 선택한 횟수 
        n_s  = sum([ 1 for sa in act_st_his if sa[0]==s ])
        #n_s  = len([ 1 for sa in act_st_his if sa[0]==s ])

        # 갱신 
        upTheta[s,a] = (n_sa - p_sa * n_s ) / total 

  # theta_0 : 상태 s에서 행동 a를 선택하는 파라미터 세타 
  # eta : 학습률(1회 학습에서의 갱신 크기)
  # upTheta : 파라미터의 세타의 변경량

  # 최종 갱신된 파라미터 세타를 반환
  return theta_0 + eta * upTheta


# 1차 갱신을 시도해서 값 확인 
# nan은 그대로 존재, 각 선택지의 확률값들이 갱신된 값에 의해 변경되었다. 
# print(update_theta(theta_0, theta, a_s_his))

# 확인 
# print(theta, theta_0)

# 에피소드 반복 처리 (1000번)
SIMULATOR_COUNTS = 1000
policy        = theta  # cur_theta
# 
STOP_EPISODE_VALUE = 10**-3 # 10^-3 -> 0.001 

for episode in range(SIMULATOR_COUNTS):
  # 에피소드 수행(갱신된 파라미터 세타를 적용)
  a_s_his = simulation_MIRO( policy )

  # 파라미터 갱신 
  #(새로운 파라미터 theta)= update_theta(theta_0, policy, a_s_his)

  # nan 값이 있어서 세타로 표현
  new_theta = update_theta( theta_0, policy, a_s_his )
  # 새로운 정책 
  new_policy = mySoftmax( new_theta )

  # 정책의 변동량(변화량)측정 
  # theta_delta = (새로운 파라미터 theta) - cur_theta
  # cur_theta   = (새로운 파라미터 theta)
  policy_delta = np.sum(np.abs(new_policy - policy))

  # 로그 
  print('에피소드:%10s, 스텝:%10s, 정책변동량:%10s' % (
                                    episode, len(a_s_his)-1, policy_delta) )

  # 이번 에피소드에 대한 내용 종료
  # 정책을 갱신 
  policy = new_policy

  # 변동량(변화량)이 임계값보다 작으면, 학습이 완료된것으로 간주 -> 중단한다. 
  # if 변동량 < 임계값(설정) :

  if policy_delta < STOP_EPISODE_VALUE :
    break
  pass

# 최단거리 이동 시뮬레이션 드로잉(자동연출)
# 최종 히스토리
# print(a_s_his)

def simulatorPlay(frame): 
  # 작업 내역에서 첫번째 요소는 에이전트이 상태 값(위치 정보)
  state = a_s_his[frame][0]
  # 에이전트를 새로운 위치에 그려라
  mouse[0].set_data( (state%3)+0.5,  3-0.5-int(state/3) )
  return mouse[0]


# %% from matplotlib import animation, rc
# from IPython.display import display, HTML
# ani = animation.FuncAnimation(fig, simulatorPlay, frames=len(a_s_his), interval=200, repeat=False)
# HTML( ani.to_jshtml())
