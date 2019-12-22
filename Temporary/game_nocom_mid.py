print( "Enjoy Custom Game world" )
while True:
    tmp = input("게임 제목을 입력하시오,\n \
    단 20자 이내로 입력 가능합니다.\n").strip()
    if not tmp:
        print("정확하게 입력하세요!")
    elif len(tmp)>20:
        print("20자가 초과되었습니다.") 
    else:
        gameTitle = tmp
        break
print( 'gameTitle', gameTitle )

while True:
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

while True:
    tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    if not tmp:
        print('정확하게 입력하세요')        
    elif not tmp.isnumeric():
        print('1-9까지 사이값으로 정확하게 입력하세요')        
    elif int(tmp)>9 or int(tmp)<1:
        print('1-9까지 사이값으로 정확하게 입력하세요')        
    else:
        game_level = tmp
        break

while True:
    tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    if not tmp:
        print('정확하게 입력하세요')        
    elif not tmp.isnumeric():
        print('1-9까지 사이값으로 정확하게 입력하세요') 
    else:       
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')        
        else:
            game_level = tmp
            break

# 긍정 상황을 잡아서 처리
while True:    
    try:# 오류가 발생하면 잡아서 처리->s/w가 다운되지 않는다:예외처리
        tmp = int(input("게임 난이도를 입력하시오, 단 %d~%d까지\
         정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip())
        if 1<=tmp<=9:
            game_level = tmp
        else:
            print('1-9까지 사이값으로 정확하게 입력하세요')    
    except Exception as e:        
        print('1-9까지 사이값으로 정확하게 입력하세요')
















































