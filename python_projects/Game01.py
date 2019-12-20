# 환경변수 or 게임데이터 

# 절차적 프로그램 실습 
# 간단한 게임을 구현 
# 긴 단위의 프로그램을 작성하고 절차적 프로그램을 이해
# 머드 게임스타일 => 터미널에서 입력하면서 게임을 진행 
# 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어등을 프로그램을 개발하면서 
# 심화 학습한다. 
# ------------------------------------------------------------------------

# 요구사항을 스텝으로 나열 **
# 뭐뭐 배웠는지 생각해보기 
# Step 1   
#      1-1 :  게임이 시작하면 "Enjoy Custom Game world" 문구를 출력

# Step 2   
#      2-2 : 사용자가 입력할때까지 무제한으로 대기
#           -> 반드시 내부에 break가 있어야 한다

#      2-1 : "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력 
#           -> 매번 입력을 대기할때 마다 해당 프럼프트 출력
#              사용자가 엔터키를 칠때까지 코드를 블럭하고 있다


#      
#      2-3 : 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기 
#            - 스페이스바를 몇번치고 엔터를 친것도 같이 처리한다 => .strip() :  공백 제거 
#    2-3-1 : "정확하게 입력하세요!" 출력하고 다시 입력 대기한다

#      2-4 : 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 그리고 대기
#    2-4-1 :  2-4 20자 이상 입력하면,
#    2-4-2 : "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다 

#      2-5 : 20자 이내로 입력하면 gameTitle라는 변수에 게임 제목을 담고 다음 3 단계로 진입
#    2-5-1 : 2-5 20자 이내로 입력
#    2-5-2 : gameTitle라는 변수에 게임 제목을 담고
#    2-5-3 : 다음 3 단계로 진입한다 -> 2단계를 끝내라

# Step 3  
#      3-1 : "플레이어의 닉네임을 입력하시오, 단 15자로 제한"
#      3-2 : 입력에 대한 처리는 step2와 동일
#      3-3 : 플레이어의 이름은 player_name이라는 변수에 담는다

# Step 4  
#      4-1 : "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한"
#      4-2 : 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
#      4-3 : 게임 난이도는 game_level 이라는 변수에 담는다



# =================
# 뭐뭐 배웠는지 생각해보기 
# 뭐뭐 쓰 일지 생각해보기 
LEN_MAX = 10
DECO = 40
GAME_LV_MIN = 1
GAME_LV_MIX = 9

WELLCOM = "Enjoy Custom Game World"
Error_Code_01 = "Error: Get Anything"
Error_Code_02 = "Error: Over Characters"
Error_Code_03 = "Error: Not integer"
Error_Code_04 = "fill out between %d and %d" % (GAME_LV_MIN, GAME_LV_MIX)

Dev = True
if Dev :
# Step 01
    print('='* DECO)
    print('>>{0:^36}<<'.format(WELLCOM))
    print('='* DECO)

# Step 02 
    # 제한 : 글자수 -> 10 
    # 무한으로 => 제목을 입력 받는=> Title_check를 위한 while 
    # // while 제한이라는걸 두기전에 먼저 선언해야한다. 
    Title_check = True
    while Title_check:
        # 제목입력 _ 사용자의 입력(Input_Title) -> INPUT // 포멧을 이용해서 가운데 정렬, 공백 입력 방지 => .strip()
        Input_Title = input('=={0:^36}==\n'.format("Please write down Title")).strip()
        print('='* DECO)
        # 공백을 입력-> 에러 
        if not Input_Title :
            print(Error_Code_01)
        # 글자수 제한 -> 10 
        elif len(Input_Title) > LEN_MAX:
            cunt = len(Input_Title) - LEN_MAX
            # 초과 문구 출력 
            print(Error_Code_02, "Over %s!!" % cunt)
        else: 
            # 정상입력
            GameTitle = Input_Title
            # print('==정상 입력==')
            print('=={0:^36}=='.format('Ckeck Point'))
            print('=={0:^34}=='.format('Title : %s') % GameTitle )
            break
            # 에러가나면 넘어가네 
        break
    # 이거 가운데 정렬 어떻게 할지 생각해보기

# Step 03 
    # 무한으로 => 사용자 이름을 받는 => User_name_check을 위한 while 
    User_name_check = True
    while User_name_check:
        print('='* DECO)
        input_User_name = input('{0:^38}\n'.format("Please write down your name")).strip()
        print('='* DECO)
        # step 02와 동일한 방식으로 진행 
        if not input_User_name:
            print(Error_Code_01)
            # ===> 재입력을 하고싶다.
        elif len(input_User_name) > LEN_MAX-5:
            cunt = len(input_User_name)-(LEN_MAX-5)
            print(Error_Code_02, "Over: %d!!" % cunt)
        else:
            User_name = input_User_name
            print('==정상 입력2==')
            break
        break
# Step 04
    # 무한으로 => 게임 레벨을 받는 => Game_Lv_Check 위한 while 
        # 정수가 아니면 에러를 출력 
        # 사용자가 넣을 수 있는 케이스를 고려
        # 공백 , 정수가 될수 없는값 , 1-9이외의 값 , 정확하게 넣을경우 
    Runnig = True
    while Runnig:
        Game_Lv_Check = input('{0:^36}\n'.format("Enter Lv  You can fill out \n between %d and %d Must be an integer"% (GAME_LV_MIN, GAME_LV_MIX))).strip()
        if not Game_Lv_Check:       # 공백을 입력-> 에러 
            print(Error_Code_01)
            
        #  정수인지 아닌지 확인 
        if not Game_Lv_Check.isnumeric():  # 정수가 않되면 컷
            print(Error_Code_03)
            continue
        Game_Lv_Check = int(Game_Lv_Check) # 왜 이걸 생각 못했지 ? 
        # if not 1<= Game_Lv_Check <=9:  #  1-9이외의 값 
        if Game_Lv_Check< 1 or 9 <Game_Lv_Check:
            print(Error_Code_04)
            continue
        Game_Lv = Game_Lv_Check
        break
        # else:  # 정확하게 넣을경우 Game_Lv => 변수에 담는다.
        #     Game_Lv = Game_Lv_Check
        #     continue
        # break
# Step 05
print('='*DECO )
print('{0:^34}'.format('Progress to date'))
print('{0:^34}'.format( 'GameTitle : %s') % GameTitle )
print('{0:^34}'.format( 'User_name : %s') % User_name )
print('{0:^34}'.format( 'Game_Lv : %s') % Game_Lv )
print('='*DECO )

# else:
#     # test or dev(개발) 버전으로 코드가 작동
#     # 매번 입력받아서 테스트하기 시간이 많아 소요되므로, 값을 고정하여 개발
#     GameTitle = 'Test_Game'하나
#     User_name = 'Guest'
#     Game_Lv   =  1

# 궁금증 1. 다른사람 코드도 그런가 ? 내가 원하는 오류가 났을때 다시 반복되는가 ?  