# 게임을 땡겨서 연습 
# 특정 모듈이 개발하면서 작성한 코드나, 
# 단독 구동시 작동해야하는 코드는 if __name__~ 내부로 처리 
# 왜냐하면 from 수행하면 해당모듈이 메모리에 로드된다. 
# 경우에 따라서는 코드가 실행될수도 있으므로, 주의 

# test5.py 확인 

from game_nocomment2_func_ending import game_level
# game_level

# from MyMath.metrix.mod import PI, add