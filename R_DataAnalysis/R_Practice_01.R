# ----------------------------------------------------------------# 
library("dplyr") #  패키지 호출 
# ggplo2의 midwest 데이터를 데이터 프레임 형태로 불러오기
midwest <- as.data.frame(ggplot2::midwest)

head(midwest)     # Raw 데이터 앞부분 확인
tail(midwest)     # Raw 데이터 뒷부분 확인
View(midwest)     # Raw 데이터 뷰어 창에서 확인
dim(midwest)      # 행, 열 출력
str(midwest)      # 데이터 속성 확인
summary(midwest)  # 요약 통계량 출력

# ----------------------------------------------------------------# 
midwest_new <- midwest # 사본생성 
midwest_new <- rename(midwest_new, total = poptotal)  # 이름 변경 poptotal -> total
midwest_new <- rename(midwest_new, asian = popasian)  # 이름 변경 popasian -> asian
# ----------------------------------------------------------------# 
# 파생변수 
# midwest_new$total_n <- (midwest_new$total + midwest_new$asian)/2  
midwest_new$total_persent <- (midwest_new$asian/midwest_new$total )*100

head(midwest_new) # 데이터 확인 
hist(midwest_new$total_persent) # 히스토그램 생성 
total_mean <- mean(midwest_new$total_persent) # 사용하기 쉽게 변수에 담기
# ----------------------------------------------------------------# 

# 조건문 파생변수 
midwest_new$asian_separate <- ifelse( midwest_new$total_persent >= total_mean, "large", "small")  # 조건문 활용

# 5. 빈도 확인 
table(midwest_new$asian_separate) # 위에서 만든 midwest_new$asian_separate 대한 빈도표 생성 
library("ggplot2") # bar chart
qplot(midwest_new$asian_separate) # 막대 그래프 그리기

# ----------------------------------------------------------------# 

