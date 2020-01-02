# 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어등을 프로그램을 개발하면서 
# 심화 학습한다. 
# ------------------------------------------------------------------------
# 절차적 프로그램 실습 
# 요구사항을 스텝으로 나열 **
# 뭐뭐 배웠는지 생각해보기 
# Step 1   
#      1-1 :  게임이 시작하면 "Enjoy Custom Game world" 문구를 출력

# Step 2   
#      2-1 : "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력 
#      2-2 : 사용자가 입력할때까지 무제한으로 대기
#      2-3 : 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기 
#      2-4 : 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 그리고 대기
#      2-5 : 20자 이내로 입력하면 gameTitle라는 변수에 게임 제목을 담고 다음 3 단계로 진입

# Step 3  
#      3-1 : "플레이어의 닉네임을 입력하시오, 단 15자로 제한"
#      3-2 : 입력에 대한 처리는 step2와 동일
#      3-3 : 플레이어의 이름은 player_name이라는 변수에 담는다

# Step 4  
#      4-1 : "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한"
#      4-2 : 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
#      4-3 : 게임 난이도는 game_level 이라는 변수에 담는다
# =================

print("Enjoy Custom Game world")
Runnig = True
while Runnig:
    # .strip() :  공백 제거 
    game_name = input("게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다.").strip()
    
    if not game_name:
        print("정확하게 입력하게세요")
        pass
    elif len(game_name) > 20 : 
        print(" 20자 글자수 초과 ")
        pass 
    else:
        gameTitle = game_name
        break
        pass
    break


print('Title : ', gameTitle)    
