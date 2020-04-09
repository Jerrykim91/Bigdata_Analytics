### paste()

# 나열된 원소를 이어 붙여서 결과값을 제공 
paste(1,2,3,4)
# paste('문자열을','합쳐','주세요') -> R스튜디오에서 하면 동작 

# 묶인 원소 
test<-c(1,2,3,4,5) 
paste(test)
length(paste(c(1,2,3,4,5,6,7,9)))

# paste는 변수, rep, c로 묶인 원소들을 개별로 인식  
# 이 경우 결과값의 개수는 paste에 나열된 원소의 개수이다.
# 원소들이 c나 rep로 묶여있으면 각각의 원소들을 매칭하여 이어 붙인다.
paste(c('2','3','4','5','6'), rep('times', 5))
paste(1:10, c('st','nd','rd', rep('th', 7)))



# 한 쪽만 묶을 경우 
# 묶이지 않은 개별 원소들과 c 혹은 rep를 함께 쓰면 묶인 원소의 개수만큼 결과값을 출력
paste('2','3','4','5','6', rep('times', 5)) 

# 개수가 다른 경우
# 묶인 원소들의 개수가 상이하다면 긴 쪽의 원소가 모두 출력될 때까지 시행을 반복
paste(c('2','3','4','5','6'), rep('times', 7)) 

## sep 
paste(1,2,3,4 ,  sep ='-')  # - 로 구분하기
paste('function','in','r', sep='   ')   # 공백(스페이스바)로 구분하기
paste('NO','-','space', sep='')   # 공백(스페이스바)로 구분하기

# sep는 구분하다를 뜻하는 seperate의 약자 -> 이를 이용 paste에 나열된 원소 사이에 옵션을 적용하여 구분 가능 
# 이때 따음표 안에 아무것도 입력하지 않은 채 옵션을 설정 
    # -> 각각의 원소 사이의 공백을 없애고 이어 붙여준다
    # -> 이는 paste0과 결과값이 동일 

## collapse
paste(c('2','3','4','5','6'), rep('times', 5), sep='', collapse=', ')
paste(1:10, c('st','nd','rd', rep('th', 7)), sep='', collapse = '_') 
# 결과값이 두개 이상일 때, 각각의 결과값에 옵션을 주어 이어붙일 때 사용
paste(1,2,3,4, collapse ='-') # 결과 값이 하나일때는 적용되지 않는다. 

# 연습 
test<-paste(c('1','2','3','4'), c('time', rep('times',3)), sep='')
test

# 변수에 담아서 출력 -> 각 변수 길이가 안 맞으면 짧은 변수는 반복 된다. 
Alphabet<-c('A','B','C','D')
Alphabet
order<-paste(1:4, c('st','nd','rd', rep('th', 1)), sep='') 
order

paste(Alphabet, 'is', order, 'Alphabet')
paste(Alphabet, 'is', order, 'Alphabet', collapse=', and ')

# 벡터와 개별 변수가 함께 쓰일 때는 벡터의 개별 값들이 모두 출력 될 때까지 시행을 반복



### paste0 -> 나열된 원소 사이에 공백없이 출력

# 비교 
paste('a','b','c','d','e', sep='')
paste0('a','b','c','d','e')

# paste0은 paste함수에서 sep=''를 적용해 준 것과 같이 각각의 원소를 공백없이 이어주는 함수입니다.