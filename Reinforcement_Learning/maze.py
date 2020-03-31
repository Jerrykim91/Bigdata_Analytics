"""
#  미로 게임 
# 
"""
# 텐서 2.0 대비
# ! pip install tensorflow==1.15


# 모듈 가져오기 
import numpy as np
import matplotlib.pyplot as plt
# %% %matplotlib inline

# 애니메이션 처리
from matplotlib import animation
# 코렙에 html을 삽입하는 모듈
from IPython.display import HTML # 이거는 차차 해결해보자 뭘 구현하실지 모르니 


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
plt.plot([0.5],[2.5], marker='o', color ='#dadada', markersize= 40 )

# 눈금, 테두리 정의 
plt.tick_params( axis='both', which='both', bottom=False, top=False,
            labelbottom=False, right=False, left=False, labelleft=False )
# 화면에 보이기
plt.box('off')
plt.show()