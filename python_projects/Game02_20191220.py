# 모듈 가져오기 
import random
import time 

# 변수 선언 
GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = True

# 
if not IS_DEV_MODE: # release 버전의 코드가 작동
    # step1 : 인트로 문구 작성
    print( "Enjoy Custom Game world" )
    # step2 : 사용자로부터 제목 입력 받기 
    while True:
        tmp = input("게임 제목을 입력하시오, 단 {}자 \이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    print( 'gameTitle', gameTitle )
    # step 3  : 사용자로부터 플레이어의 닉네임을 입력 받는다.
    while True:
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            # 플레이어 이름으로 저장된 점수를 읽어서 로드 
            # 만약 없으면 0점으로 시작 
            myTotalScore = 0   # 나의 총 점수 
            break
    # step4
    while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')
            continue
        if not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue    
        game_level = tmp
        break
else:# test or dev(개발) 버전으로 코드가 작동
    gameTitle    = 'test game'
    player_name  = 'guest'
    myTotalScore = 0 
    game_level   = 1

# step 5
if IS_DEV_MODE : # 개발시에만 작동한다.
    print( '-'*20 )
    print( '현재 까지 입력 상황' )
    print( 'gameTitle',   gameTitle )
    print( 'player_name', player_name )
    print( 'game_level',  game_level )
    print( '-'*20 )

# step 6
# 인트로 만들기
# 사용자로부터 받은 인포로 _ 시각화

print('='*40)
print('+{0:^38}+'.format(gameTitle))
print('+{0:^38}+'.format( 'lv : %s' % game_level ))
print('+{0:^34}+'.format( '"%s"의 연대기' % player_name ))
print('='*40)
print('{0:^40}'.format('press Enter key!!'))

# step 6 - 1 
# 사용자가 아무키나 누르면 지나간다.
while True:
    input();break
# 줄 구분을 위해서(구분자)

# step 7 : 실제 게임 
# == 1번만 수행하는 초기화 01 ==
types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK') # 정적 
# 리스트 내포 
cards = [ i+j for i in types for j in nums ]
# 사본 생성 
# gamecards = cards[:]
# 구구단을 통해서 문법 확인 => 동일 문법 사용 
score_table = dict()
# 문법 확인 하기 
for key in nums:score_table[ key ] = nums.index( key ) +1
# 트럼프 k는 패널티를 주어서 -5점
score_table[ 'K' ]  = -5

# 게임 _ main stage is running
MainStage_IsRunning = True
while MainStage_IsRunning:

    # == 할때마다 수행하는 초기화 02 ==
    # cards의 사본이용 _ 데이터 보호차원
    gamecards = cards[:]
    random.shuffle(gamecards)

    # 2. 카드를 순서대로 배분 
    # 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 
    # 나한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
    # 어떻게 뽑을건데 ? 
    my_cards       = gamecards[:8:2]
    my_first_cards = my_cards[:2]
    com_cards      = gamecards[1:9:2]
    com_first_cards= com_cards[:2]

    cnt = 0 # 카드를 추가로 준 횟수
    myTotalScore = 0 
    PlayGame = True
    while PlayGame:
        msg = '''
        나의 카드 %s, %s  Vs com의 카드 : %s, [HIDEN]
        ''' % (my_first_cards[0],my_first_cards[1], com_first_cards[0])
        print(msg)
        # 게임성을 데코레이션 정도로 2초정도 대기
        Break_time = 0 
        while True:
            time.sleep(0.5)
            print('.'*Break_time)
            Break_time += 1
            if == '4': 
                break

        choice = input( '1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?' )
        if choice == '1' and cnt <2:
            cnt += 1
            my_first_cards  = my_cards[:2+cnt]
            com_first_cards = com_cards[:2+cnt]
        elif choice == '2':
            # 비교시 A는 합산값의 *2을 한다 : 
            # ex) A, 3 => (1+3)*2 = 8점
            # 저장= (내점수-컴점수)*100 + 카드를 더 받은 횟수*(-20) 
            myScore  = 0
            comScore = 0
            for n in my_first_cards :  myScore += score_table[ n[1:] ]
            for n in com_first_cards: comScore += score_table[ n[1:] ]
            print('myScore', myScore)
            print('comScore',comScore)

            # 엔터키를 누르면 아래를 진행 => ??? 
            if myScore > comScore:
                # 점수 산출 표시 및 표시 
                # 내가 받은 점수 = (기본 점수 - 컴 점수 )*100 + cnt*(감점 점수)
                MyGetScore = (myScore- comScore)*100 +cnt*(-20)
                # 내점수에 합산
                myTotalScore += MyGetScore
                print('축하합니다. %s점 획득하였습니다. 현재 총 %s점입니다.' % (MyGetScore,myTotalScore) )
                print('You Win, try again? 1.yes, 2.no')
                
            elif myScore < comScore:
                # 점수 산출 표시
                MyGetScore = -5 # 지면 5점 감점
                # 내점수에 합산
                myTotalScore += myGetScore
                print('아쉽습니다. %s점 잃었습니다. 현재 총 %s점입니다.' % (myGetScore,myTotalScore) )
                print('You Lose, try again? 1.yes, 2.no')
            else:
                # 점수 산출 표시 
                MyGetScore = 0
                print('아~ 비겼네요.. 점수 변동없습니다.' )
                print('무승부, try again? 1.yes, 2.no')
            # break
            # 게임 저장 
            # 1혹은 2를 입력 받으면 게임이 끝나거나 다시
            while True:
                # 대문자 소문자 어떤것을 넣던 OK
                # 내부적으로는 결정한다(어느쪽으로 처리할것인지)
                # 공백 날리기, 대문자로 입력받았을대 소문자 처리 
                c_number = input().strip.lower()
                if c_number == '1' or c_number == 'y' or c_number =='yes' :
                    PlayGame = False
                elif c_number == '2'or c_number == 'n' or c_number =='no' :
                    PlayGame = False
                    MainStage_IsRunning = False
                    break
                else:
                    print('정확하게 1.yes, 2.no 중에 하나를 입력하세요')
        else:
            print('정확하게 1 or 2를 입력하세요')
            if cnt == 2:
                print('이미 추가 카드를 다 받았습니다. 2번만 선택할수 있습니다.')

print( 'bye bye ~ \ngame over!!' )