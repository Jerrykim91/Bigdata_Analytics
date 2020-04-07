# 데이터 전처리
# filter()   |행 추출
# select()   |열(변수) 추출
# arrange()  |정렬
# mutate()   |변수 추가
# summarise()|통계치 산출
# group_by() |집단별로 나누기
# left_join()|데이터 합치기(열)
# bind_rows()|데이터 합치기(행)

# warning(library(dplyr))
# suppressWarnings(library(dplyr))

library(dplyr)
exam <- read.csv("./data/csv_exam.csv")
exam

# filter : 행 추출
# exam에서 class가 1인 경우만 추출하여 출력
exam %>% filter(class == 1)

# 2반인 경우만 추출
exam %>% filter(class == 2)

# 3반이 아닌 경우
exam %>% filter(class != 3)

# 수학 점수가 50점을 초과한 경우
exam %>% filter(math > 50)

# 1반이면서 수학 점수가 50점 이상인 경우
exam %>% filter(class = 1 & math >= 50)

# 2반이면서 영어 점수가 80점 이상인 경우
exam %>% filter(class = 2 & english >= 50)

# 수학 점수가 90점 이상이거나 영어점수가 90점 이상인 경우
exam %>% filter(math >= 90 | english >= 90)

# 목록에 해당되는 행 추출 
# 1,3,5 반에 해당하면 추출
exam %>% filter(class == 1 | class == 3 | class == 5)  # 1, 3, 5 반에 해당되면 추출
exam %>% filter(class %in% c(1,3,5))

# 추출한 행으로 데이터 만들기
class1 <- exam %>% filter(class == 1)  # class가 1인 행 추출, class1에 할당
class2 <- exam %>% filter(class == 2)  # class가 2인 행 추출, class2에 할당

# 논리 연산자 기능
# <            | 작다
# <=           | 작거나 같다
# >            | 크다
# >=           | 크거나 같다
# ==           | 같다
# !=           | 같지 않다
# │            | 또는
# &            | 그리고
# %in%         | 매칭 확인

# 산술 연산자 기능
#  +          | 더하기
# -          | 빼기
# *          | 곱하기
# /          | 나누기
# ^ , **     | 제곱
# %/%        | 나눗셈의 몫
# %%         | 나눗셈의 나머지

# QUIZ 1
mpg <- as.data.frame(ggplot2::mpg)

hwy_1 <- mpg %>% filter ( displ <= 4)
hwy_2 <- mpg %>% filter ( displ >= 5)

mean(hwy_1$hwy) > mean(hwy_2$hwy)

# QUIZ 2
cty_1 <- mpg %>% filter(manufacturer =="audi")
cty_1

cty_2 <- mpg %>% filter(manufacturer =="toyota")
cty_2

mean(cty_1$cty) < mean(cty_2$cty)

# QUIZ 3
hwy_mean <- mpg %>% filter(manufacturer =="chevrolet" | manufacturer =="ford" | manufacturer =="honda")
mean(hwy_mean$hwy)

# 필요한 변수만 추출하기
# select : 열 추출
exam %>% select(math)  # math 추출
exam %>% select(-math) # math만 추출
exam %>% select(class, math, english) # class, math, english 변수 추출

# class가 1인 행만 추출한 다음 english 추출
exam %>% filter(class == 1) %>% select(english)

exam %>%
  filter(class == 1) %>%  # class가 1인 행 추출
  select(english)         # english 추출

# QUIZ 1
mpg <- as.data.frame(ggplot2::mpg)
mpg_new <- mpg %>% select(class, cty)
mpg_new

# QUIZ 2
mpg_another1 <- mpg %>% filter(class == "suv")
mpg_another2 <- mpg %>% filter(class == "compact")

mean(mpg_another1$cty)
mean(mpg_another2$cty)

# 정렬
mpg <- as.data.frame(ggplot2::mpg)          # mpg 데이터 불러오기
mpg %>% filter(manufacturer == "audi") %>%  # audi 추출
  arrange(desc(hwy)) %>%                    # hwy 내림차순 정렬
  head(5)                                   # 5행까지 출력

# 파생변수 추가하기
exam %>%
  mutate(total = math + english + science) %>%  # 총합 변수 추가
  head(5) -> exam_total                         # 일부 추출
exam_total

# 여러 파생변수 한 번에 추가하기
exam %>%
  mutate(total = math + english + science,          # 총합 변수 추가
         mean = (math + english + science)/3) %>%   # 총평균 변수 추가
  head                                              # 일부 추출

# `mutate()`에 `ifelse()` 적용하기
exam %>%
  mutate(test = ifelse(science >= 60, "pass", "fail")) %>%
  head

# 추가한 변수를 `dplyr` 코드에 바로 활용하기
exam %>%
  mutate(total = math + english + science) %>%  # 총합 변수 추가
  arrange(total) %>%                            # 총합 변수 기준 정렬
  head                                          # 일부 추출

# QUIZ 1
mpg <- as.data.frame(ggplot2::mpg)
mpg_new <- mpg
mpg_new <- mpg_new %>%
  mutate(sum = cty + hwy)

# QUIZ 2
mpg_new <- mpg_new %>% 
  mutate(mean = sum/2) 

# QUIZ 3
mpg_new %>%
  arrange(desc(mean)) %>%
  head(3)

# QUIZ 4
mpg %>%
  mutate(sum = cty + hwy, mean = sum/2) %>%
  arrange(desc(mean)) %>%
  head(3)

# 요약하기
exam %>% summarise(mean_math = mean(math))  # math 평균 산출

# 집단별로 요약하기
exam %>%
  group_by(class) %>%                # class별로 분리
  summarise(mean_math = mean(math))  # math 평균 산출

# 여러 요약통계량 한 번에 산출하기
exam %>%
  group_by(class) %>%                   # class별로 분리
  summarise(mean_math = mean(math),     # math 평균
            sum_math = sum(math),       # math 합계
            median_math = median(math), # math 중앙값
            n = n())                    # 학생 수

# 자주 사용하는 요약통계량 함수
'''
함수    |의미
--------|-----
mean()  |평균
sd()    |표준편차
sum()   |합계
median()|중앙값
min()   |최솟값
max()   |최댓값
n()     |빈도
'''

# 각 집단별로 다시 집단 나누기
mpg %>%
  group_by(manufacturer, drv) %>%      # 회사별, 구방방식별 분리
  summarise(mean_cty = mean(cty)) %>%  # cty 평균 산출
  head(10)                             # 일부 출력

# 분석 절차 생각해보기
'''
절차  |기능                |dplyr 함수
:----:|-------------------|---------
1     |회사별로 분리       |group_by()
2     |suv 추출           |filter()
3     |통합 연비 변수 생성 |mutate()
4     |통합 연비 평균 산출 |summarise()
5     |내림차순 정렬       |arrange()
6     |1~5위까지 출력      |head()
'''

# dplyr 조합하기
mpg %>%
  group_by(manufacturer) %>%           # 회사별로 분리
  filter(class == "suv") %>%           # suv 추출
  mutate(tot = (cty+hwy)/2) %>%        # 통합 연비 변수 생성
  summarise(mean_tot = mean(tot)) %>%  # 통합 연비 평균 산출
  arrange(desc(mean_tot)) %>%          # 내림차순 정렬
  head(5)                              # 1~5위까지 출력

# QUIZ 1 
mpg_new <- mpg
mpg_new <- mpg_new %>%
  group_by(class) %>%
  summarise(mean_cty = mean(cty))

# QUIZ 2
mpg_new <- mpg_new %>%
  arrange(desc(mean_cty))
mpg_new

# QUIZ 3
mpg %>%
  group_by(manufacturer) %>%  
  summarise(mean_hwy = mean(hwy)) %>%
  arrange(desc(mean_hwy)) %>%
  head(3)

# QUIZ 4
mpg %>%
  filter(class == "compact") %>%  # compact 추출
  group_by(manufacturer) %>%      # manufacturer별 분리
  summarise(count = n()) %>%      # 빈도 구하기
  arrange(desc(count))            # 내림차순 정렬

# https://github.com/youngwoos/Doit_R/blob/master/Lecture/RMD/Doit_part06.Rmd

# 중간고사 데이터 생성
test1 <- data.frame(id = c(1, 2, 3, 4, 5),
                    midterm = c(60, 80, 70, 90, 85))
# 기말고사 데이터 생성
test2 <- data.frame(id = c(1, 2, 3, 4, 5),
                    final = c(70, 83, 65, 95, 80))
test1
test2

# 다른 데이터 활용해 변수 추가하기
# 반별 담임교사 명단 생성
name <- data.frame(class = c(1,2,3,4,5),
                   teacher = c("kim", "lee","park", "choi", "jung"))
name

# class 기준 합치기
exam_new <- left_join(exam, name, by = "class")
exam_new

# 세로로 합치기
# 데이터 생성
# 학생 1~5번 시험 데이터 생성
group_a <- data.frame(id = c(1, 2, 3, 4, 5),
                      test = c(60, 80, 70, 90, 85))
# 학생 6~10번 시험 데이터 생성
group_b <- data.frame(id = c(6, 7, 8, 9, 10),
                      test = c(70, 83, 65, 95, 80))

# 세로로 합치기
group_all <- bind_rows(group_a, group_b) # 데이터 합쳐서 group_all에 할당
group_all

# QUIZ 1
fuel <- data.frame(fl = c("c", "d", "e", "p", "r"),
                   price_fl = c(2.35, 2.38, 2.11, 2.76, 2.22),
                   stringsAsFactors = F)
fuel
mpg <- left_join(mpg, fuel, by='fl')
mpg

# QUIZ 2
mpg %>% select(model, fl, price_fl) %>%
  head

# Review

# 1.조건에 맞는 데이터만 추출하기
exam %>% filter(english >= 80)
# 여러 조건 동시 충족
exam %>% filter(class == 1 & math >= 50)
# 여러 조건 중 하나 이상 충족
exam %>% filter(math >= 90 | english >= 90)
exam %>% filter(class %in% c(1,3,5))

# 2.필요한 변수만 추출하기
exam %>% select(math)
exam %>% select(class, math, english)

# 3.함수 조합하기, 일부만 출력하기
exam %>%
  select(id, math) %>%
  head(10)

# 4.순서대로 정렬하기
exam %>% arrange(math)         # 오름차순 정렬
exam %>% arrange(desc(math))   # 내림차순 정렬
exam %>% arrange(class, math)  # 여러 변수 기준 오름차순 정렬

# 5.파생변수 추가하기
exam %>% mutate(total = math + english + science)
# 여러 파생변수 한 번에 추가하기
exam %>%
  mutate(total = math + english + science,
         mean = (math + english + science)/3)
# mutate()에 ifelse() 적용하기
exam %>% mutate(test = ifelse(science >= 60, "pass", "fail"))
# 추가한 변수를 dplyr 코드에 바로 활용하기
exam %>%
  mutate(total = math + english + science) %>%
  arrange(total)

# 6.집단별로 요약하기
exam %>%
  group_by(class) %>%
  summarise(mean_math = mean(math))
# 각 집단별로 다시 집단 나누기
mpg %>%
  group_by(manufacturer, drv) %>%
  summarise(mean_cty = mean(cty))

# 7.데이터 합치기
# 가로로 합치기
total <- left_join(test1, test2, by = "id")
# 세로로 합치기
group_all <- bind_rows(group_a, group_b)

# QUIZ
# midwest 불러오기
midwest <- as.data.frame(ggplot2::midwest)

# QUIZ 1 - 백분율 변수 추가
midwest <- midwest %>%
  mutate(pop_non_adults_total = (poptotal-popadults)/poptotal*100)
midwest

# QUIZ 2 
midwest %>%
  arrange(desc(pop_non_adults_total)) %>%
  select(county, pop_non_adults_total) %>%
  head(5)

# QUIZ 3
midwest <- midwest %>%
  mutate(grade = ifelse(pop_non_adults_total >= 40, "large", ifelse(pop_non_adults_total >= 30, "middle","small")))
midwest
  
# QUIZ 4
midwest %>%
  mutate(ratio_asian = (popasian/poptotal)*100) %>%
  arrange(ratio_asian) %>%
  select(county,ratio_asian) %>%
  head(5)

# 결측치(Missing Value)

# - 누락된 값, 비어있는 값
# - 함수 적용 불가, 분석 결과 왜곡
# - 제거 후 분석 실시

# 결측치
df <- data.frame(sex = c("M", "F", NA, "M", "F"),
                 score = c(5, 4, 3, 4, NA))
is.na(df)         # 결측치 확인
table(is.na(df))  # 결측치 빈도 출력
table(is.na(df$sex))    # sex 결측치 빈도 출력
table(is.na(df$score))  # score 결측치 빈도 출력

mean(df$score)  # 평균 산출
sum(df$score)   # 합계 산출

library(dplyr) # dplyr 패키지 로드
df %>% filter(is.na(score))   # score가 NA인 데이터만 출력
df %>% filter(!is.na(score))  # score 결측치 제거

df_nomiss <- df %>% filter(!is.na(score))  # score 결측치 제거
mean(df_nomiss$score)                      # score 평균 산출
sum(df_nomiss$score)                       # score 합계 산출

# score, sex 결측치 제외
df_nomiss <- df %>% filter(!is.na(score) & !is.na(sex))
df_nomiss  
df_nomiss2 <- na.omit(df)  # 모든 변수에 결측치 없는 데이터 추출
df_nomiss2                 # 출력

# 분석에 필요한 데이터까지 손실 될 가능성 유의
# ex) 성별-소득 관계 분석하는데 지역 결측치까지 제거

# 함수의 결측치 제외 기능 이용하기 - `na.rm = T`
mean(df$score, na.rm = T)  # 결측치 제외하고 평균 산출
sum(df$score, na.rm = T)   # 결측치 제외하고 합계 산출

# summarise()에서 `na.rm = T`사용하기
# 결측치 생성
exam <- read.csv("./data/csv_exam.csv")            # 데이터 불러오기
exam[c(3, 8, 15), "math"] <- NA             # 3, 8, 15행의 math에 NA 할당

# 평균 구하기
exam %>% summarise(mean_math = mean(math))             # 평균 산출
exam %>% summarise(mean_math = mean(math, na.rm = T))  # 결측치 제외하고 평균 산출

### 다른 함수들에 적용
exam %>% summarise(mean_math = mean(math, na.rm = T),      # 평균 산출
                   sum_math = sum(math, na.rm = T),        # 합계 산출
                   median_math = median(math, na.rm = T))  # 중앙값 산출

# 결측치 대체하기
# 결측치 많을 경우 모두 제외하면 데이터 손실 큼
# 대안: 다른 값 채워넣기

# 결측치 대체법(Imputation)
# 대표값(평균, 최빈값 등)으로 일괄 대체
# 통계분석 기법 적용, 예측값 추정해서 대체

mean(exam$math, na.rm = T)  # 결측치 제외하고 math 평균 산출

exam$math <- ifelse(is.na(exam$math), 55, exam$math)  # math가 NA면 55로 대체
table(is.na(exam$math))                               # 결측치 빈도표 생성

exam  # 출력
mean(exam$math)  # math 평균 산출

# QUIZ
mpg <- as.data.frame(ggplot2::mpg)           # mpg 데이터 불러오기
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA  # NA 할당하기

# QUIZ 1
table(is.na(mpg$drv)) # 결측치 X
table(is.na(mpg$hwy)) # 결측치 5개

# QUIZ 2
mpg %>%
  filter(!is.na(hwy)) %>%
  group_by(drv) %>%       # 구동 방식별로
  summarise(mean_hwy = mean(hwy))

# 이상치(Outlier) - 정상범주에서 크게 벗어난 값
# 이상치 포함시 분석 결과 왜곡
# 결측 처리 후 제외하고 분석
'''
이상치 종류      |예                |해결 방법
-----------------|------------------|---------
  존재할 수 없는 값|성별 변수에 3     |결측 처리
극단적인 값      |몸무게 변수에 200 |정상범위 기준 정해서 결측 처리
'''

# 이상치 제거하기 - 1. 존재할 수 없는 값
outlier <- data.frame(sex = c(1, 2, 1, 3, 2, 1),
                      score = c(5, 4, 3, 4, 2, 6))
table(outlier$sex)
table(outlier$score)

# 결측 처리 - sex
# sex가 3이면 NA 할당
outlier$sex <- ifelse(outlier$sex == 3, NA, outlier$sex)
outlier

# 결측 처리 - score
# sex가 1~5 아니면 NA 할당
outlier$score <- ifelse(outlier$score > 5, NA, outlier$score)
outlier

# 결측치 제외하고 분석
outlier %>%
  filter(!is.na(sex) & !is.na(score)) %>%
  group_by(sex) %>%
  summarise(mean_score = mean(score))

# 이상치 제거하기 - 2. 극단적인 값
# 정상범위 기준 정해서 벗어나면 결측 처리
'''
판단 기준   |예
------------|---
논리적 판단 |성인 몸무게 40kg~150kg 벗어나면 극단치
통계적 판단 |상하위 0.3% 극단치 또는 상자그림 1.5 IQR 벗어나면 극단치
'''

mpg <- as.data.frame(ggplot2::mpg)
boxplot(mpg$hwy)
boxplot(mpg$hwy)$stats
'''
상자 그림          |값                   |설명
------------------|--------------------|---
상자 아래 세로 점선 |아래수염             |하위 0~25% 내에 해당하는 값
상자 밑면          |1사분위수(Q1)        |하위 25% 위치 값
상자 내 굵은 선    |2사분위수(Q2)         |하위 50% 위치 값(중앙값)
상자 윗면          |3사분위수(Q3)         |하위 75% 위치 값
상자 위 세로 점선  |윗수염                |하위 75~100% 내에 해당하는 값
상자 밖 가로선     |극단치 경계           |Q1, Q3 밖 1.5 IQR 내 최대값
상자 밖 점 표식    |극단치                |Q1, Q3 밖 1.5 IQR을 벗어난 값
'''

# 결측 처리하기
# 12~37 벗어나면 NA 할당
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)
table(is.na(mpg$hwy))

# 결측치 제외하고 분석하기
mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy, na.rm = T))

# QUIZ
mpg <- as.data.frame(ggplot2::mpg)                  # mpg 데이터 불러오기
mpg[c(10, 14, 58, 93), "drv"] <- "k"                # drv 이상치 할당
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42)  # cty 이상치 할당

# QUIZ 1
table(mpg$drv)
mpg$drv <- ifelse(mpg$drv %in% c('4','f','r'), mpg$drv, NA)
table(mpg$drv)

# QUIZ 2
boxplot(mpg$cty)$stats
mpg$cty <- ifelse(mpg$cty < 9 | mpg$cty > 26, NA, mpg$cty)
boxplot(mpg$cty)


