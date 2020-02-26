# 코드 작성전 어떤 그림이 그려질지 상상하자 
# 그리고 의사코드를 작성 =>  다시 역설계 한다.


'''
의사 코드 작성
목표 : 

step01 
step01 
step01 
step01 
step01 

'''


# 파일 리스트 획득
import glob

# 파일 목록 보기 =>  파일명 전부 확득  
path = './input/train/*.txt'
file_list = glob.glob(path)
print(file_list[:2], len(file_list))

# 오름차순으로 나열 
print(file_list.sort())