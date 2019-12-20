# 단위 테스트용 
# 정수 값을  input으로 받아서 타입을 체크 

# 렌덤 및 셔플 테스트 
import random

ori_data = list(i for i in range(1,6))
target_data = ori_data[:]

random.shuffle(target_data) 
# .shuffle() : 섞기 함수 
print(ori_data)
print(target_data)

#random.seed(1)
# 일정하게 섞이는 값을 원한다면 => seed를 고정하면 됨
# seed는 값이 일정하게 나온다 
# 그래서 seed를 고정해서 난수가 나오는 순서를 동일하게 해서 
# 일정한결과를 내는 작업에 많이사용된다. 
# 주로 변수를 바꿔가면서 영향성등등 분석 가능하다. 
# seed를 고정하지 않으면 => 현재 시간이 seed의 값이 된다 
# 이유는 시간은 흘러가니까 

