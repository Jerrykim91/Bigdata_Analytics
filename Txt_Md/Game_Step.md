``` py
========= #
  절차적 프로그램 
========= #

Step 01   
     1-1 : 게임이 시작하면 "Enjoy Custom Game world" 문구를 출력

Step 02   
     2-2 : 사용자가 입력할때까지 무제한으로 대기
          -> 반드시 내부에 break가 있어야 한다 => 아니면 무한 루프 

     2-1 : 사용자로 부터 타이틀을 입력받는다. 그리고 아래 문구를 출력한다. 
          "게임 제목을 입력하시오, 단 10자 이내로 입력 가능합니다."  
          글자수 제한  => 10 
          -> 매번 입력을 대기할때 마다 해당 프럼프트 출력
             사용자가 엔터키를 칠때까지 코드를 블럭(while문 이용 )
     
     2-3 : 프롬프트에 아무것도 입력하지 않고 엔터를 치면
           "정확하게 입력하세요!" 출력하고 다시 입력 대기 
            # 제목입력 _ 사용자의 입력(Input_Title) -> INPUT // 포멧을 이용해서 가운데 정렬, 공백 입력 방지 => .strip()
   2-3-1 : "정확하게 입력하세요!" 출력하고 다시 입력 대기  => .strip() :  공백 제거 

     2-4 : 10자 이상 입력하면 "10자가 초과되었습니다." 출력하고, 다시 입력 그리고 대기
   2-4-1 : 10자 이상 입력 
   2-4-2 : "10자가 초과되었습니다." 출력하고, 다시 입력 대기 

     2-5 : 10자 이내로 입력하면 gameTitle라는 변수에 게임 제목을 담고 다음 3 단계로 진입
   2-5-1 : 10자 이내로 입력
   2-5-2 : gameTitle라는 변수에 게임 제목 - > 
   2-5-3 : 다음 3 단계로 진입 -> 2단계를 마무리

Step 03  
     # 무한으로 => 사용자 이름을 받는 => User_name_check을 위한 while 
     3-1 : "플레이어의 닉네임을 입력하시오, 단 5자로 제한"
     3-2 : 입력에 대한 처리는 step2와 동일
     3-3 : 플레이어의 이름은 player_name 변수에 담는다

Step 04  
        # 무한으로 => 게임 레벨을 받는 => Game_Lv_Check 위한 while 
        # 정수가 아니면 에러를 출력 
        # 사용자가 넣을 수 있는 케이스를 고려
        # 공백, 정수가 될 수 없는 값, 1-9이외의 값, 정확한 값
     4-1 : "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한"
     4-2 : 입력에 대한 처리는 step2와 동일
   4-2-1 : 공백, 정수가 될 수 없는 값, 1-9이외의 값, (정확한 값) 에러를 출력
     4-3 : 게임 난이도는 game_level => 변수에

Step 05
      # 현재 상황 출력 

Step 06 __ StartIntro
# 인트로 만들기
# 사용자로부터 받은 인포로 _ 시각화
# => 만들기 아래와 같이 
'''
========================================
+           게임제목(중앙정렬)           +
+                lv 레벨값              +
+       "플레이어이름"의 연대기          +
========================================
            press any key!!
'''
# press any key!! => 누르면 지나간다 

Step 07 __ CadeGame
# 실제 게임이 진행되는 구간 
# 카드 종류 -> 4타입, 타입별로 13장의 카드가 존재
# 타입 => 4
# 넘버 => 13 (A, J, Q, K 포함)
'''
♠ : A,2 ~ 10, J, Q, K
♥ : A,2 ~ 10, J, Q, K
♣ : A,2 ~ 10, J, Q, K
◆ : A,2 ~ 10, J, Q, K
'''
# 카드 종류 -> 4타입, 타입별로 13장의 카드가 존재
# [0] : ♠(sp=[1:13]) | [1] : ♥(ha=[1:13]) | [2] : ♣(cl=[1:13]) | [3] :♦(da=[1:13])
# 일단 카드를 먼저 만들어야해 

# 카드를 섞는다. 
# 카드를 순서대로 배분 ! 나한장(0), 컴퓨터 한장(1), 
# 나한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)











``` 















```

# 전체 룰
  1. 게임이 시작하면 카드를 섞는다 
  => 셔플 => random 모듈을 활용(외장함수, 구현을 위해 사용)

  2. 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 나한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
  3. 플레이어는 최대 2장까지 더 받을수 있다
    다시 나한장(4,6), 컴퓨터 한장(5,7) -> 최대 2번까지 가능
  4. 승패 => 내가 가진 카드중 최대값 2개를 합산해서, 
        특별기능이 있다면 추가 계산해서 높은쪽이 승리한다
  5. 한번에 이기면 (내카드의합-컴퓨터카드의합)*100, 카드르 한번 받으면 20점씩 깐다
  6. 카드를 받으면 
        1) 카드를 더 받겠습니까? 아니면 2) 승부를 내겠습니까?
  7. 다시 하시겠습니까? 
        yes => 다시 1번부터 시작
        no-> game over!! 종료




```





궁금증 1. 다른사람 코드도 그런가 ? 내가 원하는 오류가 났을때 다시 반복되는가 ?  
게임의 다음 step06 이후의 코드는 조금 더 코드를 이해하고 진행 (2019.12.19~ )

``` py
============================================================================ #
객체지향적 프로그램 (미정_ 아마 절차적코드 다 짜고 클래스를 한번 보고 넘어갈 예정 )
============================================================================ #
```