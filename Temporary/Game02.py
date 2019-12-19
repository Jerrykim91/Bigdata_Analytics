LEN_MAX = 10
DECO    = 40
GAME_LV_MIN = 1
GAME_LV_MIX = 9

WELLCOM       = "Enjoy Custom Game World"
Error_Code_01 = "Error: Get Anything"
Error_Code_02 = "Error: Over Characters"
Error_Code_03 = "Error: Not integer"
Error_Code_04 = "fill out between %d and %d" % (GAME_LV_MIN, GAME_LV_MIX)

Dev = True
if not Dev :
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
            print('=={0:^36}=='.format('Ckeck Point_1'))
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
            print('=={0:^36}=='.format('Ckeck Point_2'))
            break
        break
# Step 04
    # 무한으로 => 게임 레벨을 받는 => Game_Lv_Check 위한 while 
        # 정수가 아니면 에러를 출력 
        # 사용자가 넣을 수 있는 케이스를 고려
        # 공백, 정수가 될 수 없는 값, 1-9이외의 값, 정확한 값
    Runnig = True
    while Runnig:
        Game_Lv_Check = input('{0:^36}\n'.format("Enter Lv \n You can fill out between %d and %d Must be an integer"% (GAME_LV_MIN, GAME_LV_MIX))).strip()
        if not Game_Lv_Check:       # 공백을 입력-> 에러 
            print(Error_Code_01)
            
        #  정수인지 아닌지 확인 
        if not Game_Lv_Check.isnumeric():  # 정수가 아니면 컷
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

else:
    # test or dev(개발) 버전으로 코드가 작동
    # 매번 입력받아서 테스트하기 너어무 시간이 많이 소요
    #   => 값을 고정하여 개발
    GameTitle = 'Test_Game'
    User_name = 'Guest'
    Game_Lv   =  1

# Step 05
print('='* DECO )
print('{0:^38}'.format('Progress to Date'))
print('{0:^34}'.format( 'GameTitle : %s') % GameTitle )
print('{0:^38}'.format( 'User_name : %s') % User_name )
print('{0:^40}'.format( 'Game_Lv : %s') % Game_Lv )
print('='* DECO )

# Step 06 __ StartIntro
'''
========================================
+           게임제목(중앙정렬)           +
+                lv 레벨값              +
+       "플레이어이름"의 연대기          +
========================================
            press any key!!
'''
print('='* DECO )
print('={0:^38}='.format(GameTitle))
print('={0:^40}='.format( 'Lv : %0s' ) % Game_Lv )
print('={0:^38}='.format( User_name ))
print('='* DECO )
print('={0:^38}='.format( 'press any key!!' ))
print('='* DECO )

# step 7 __ CadeGame
'''
♠ : A,2 ~ 10, J, Q, K
♥ : A,2 ~ 10, J, Q, K
♣ : A,2 ~ 10, J, Q, K
◆ : A,2 ~ 10, J, Q, K
'''
# 카드 종류 -> 4타입, 타입별로 13장의 카드가 존재
# [0] : ♠(sp=[1:13]) | [1] : ♥(ha=[1:13]) | [2] : ♣(cl=[1:13]) | [3] :♦(da=[1:13])
# 일단 카드를 먼저 만들어야해 
CARD_TYPES = list('♠♥♣◆')
CARD_NUMS  = list('123456789') + list('10') + list('JQK')
CARDS      = [i+j for i in CARD_TYPES for j in CARD_NUMS]

print(CARD_TYPES)
print(CARD_NUMS)

# Py_Test01.py
# 게임이 시작하면 카드를 섞는다 
# import random
import random
# 카드를 섞는다. 
random.shuffle(CARDS) 

#2. 카드를 순서대로 
# 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 
# 나한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
# 어떻게 뽑을건데 ? 

# 셔플된 카드를 어떻게 하나씩 ? 





# 전체 룰
# 1. 게임이 시작하면 카드를 섞는다 
# => 셔플 => random 모듈을 활용(외장함수, 구현을 위해 사용)

# 2. 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 나한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
# 3. 플레이어는 최대 2장까지 더 받을수 있다
#    다시 나한장(4,6), 컴퓨터 한장(5,7) -> 최대 2번까지 가능
# 4. 승패 => 내가 가진 카드중 최대값 2개를 합산해서, 
#       특별기능이 있다면 추가 계산해서 높은쪽이 승리한다
# 5. 한번에 이기면 (내카드의합-컴퓨터카드의합)*100, 카드르 한번 받으면 20점씩 깐다
# 6. 카드를 받으면 
#       1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?
# 7. 다시 하시겠습니까? 
#        yes => 다시 1번부터 시작
#        no-> game over!! 종료