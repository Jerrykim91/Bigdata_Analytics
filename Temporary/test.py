# 단위 테스트용
# 정수값을 input으로 받아서 타입을 체크
# a = input()
# if (정수가 될수 있다?):
#     tmp = int(a)
#     print( type(tmp) ) 

# '1'.is

# 랜덤 및 셔플 테스트
import random

ori_data    = [1,2,3,4,5]
target_data = ori_data[:]
# 난 항상 일정하게 섞기는 값을 원한다->난수가 항상 일정하게 나온다->seed고정하면된다
random.seed(1) # 씨드를 고정하면 난수가 나오는 순서가 동일 => 일정한 결과를 낼수있다
# 일정한 결과를 내면 => 항상 같은 결과가 나오는 실험환경을 구축할수 있다 
# 변수를 바꿔가면서 영향성등등 분석할수 잇다
# 씨드를 고정하지 않으면 => 현재 시간이 씨드가 된다
random.shuffle(target_data) # 섞기 함수
print(ori_data)
print(target_data)