# 트럼프카드 => 타입이 4개, 타입별 카드가 13장
# 총카드수 = 13 * 4 = 52->일렬로 배치하면
CARD_TYPE = 4
CARD_PER_TYPE_SIZE = 13
TOTAL_CARD_COUNT = CARD_TYPE * CARD_PER_TYPE_SIZE
# 모든 카드 생성 
all_cards = list(range(TOTAL_CARD_COUNT))
# 카드 타입의 순서는
seq = list('♠◆♥♣')
card_id = list('A23456789')+['10']+list('JQK')
print( seq, card_id )
# 33번이라는 숫자는 어떤 카드인가?
target_num = 33
print( seq[int(target_num/CARD_PER_TYPE_SIZE)] )
print( card_id[target_num%CARD_PER_TYPE_SIZE] )
