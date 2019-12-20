# 카드 => 4개의 타입
#      => 13가지의 수
# 총 카드수는 = 13*4 
#            =  52 

User_name = 'Jerry'
CARD_TYPEs = 4 
CARD_TYPE_NUMs = 13
TOTAL_CARD_CNT =  CARD_TYPEs * CARD_TYPE_NUMs
print(TOTAL_CARD_CNT)

# 카드 생성 
ALL_CARDs = list(range(TOTAL_CARD_CNT))
print(ALL_CARDs)
print('='*20)

# 카드 순서 
CARD_TYPES = list('♠♥♣◆')
CARD_NUMS = list('123456789') + list('10') + list('JQK')
CARDS = [i+j for i in CARD_TYPES for j in CARD_NUMS]
print(CARDS)
print(CARDS[33:34])
print( CARD_TYPES, CARD_NUMS )
print('='*20)

# 33번이 왜? 
target_num = 33
print( CARD_TYPES[int(target_num/CARD_TYPE_NUMs)] )
print( CARD_NUMS[target_num%CARD_TYPE_NUMs] )


print('=*='*20)
# 카드 준비 
CARD_TYPES = list('♠♥♣◆')
CARD_NUMS = list('123456789') + list('10') + list('JQK')
CARDS = [i+j for i in CARD_TYPES for j in CARD_NUMS]

# 셔플하기
import random
# 씨드 고정 : 난수가 나오는 순서를 고정 => 난수 값은 상관 없음 
random.seed(1)
random.shuffle(CARDS)
print(CARDS[:8])
print('=='*20)
print('%s Card =>'% User_name, CARDS[:8:2])
print('AI_Card    =>',CARDS[1:9:2])
print('=='*20)

# 카드 합산 
# 내카드 합산 : 최초 2개 => 2장을 추출하라

