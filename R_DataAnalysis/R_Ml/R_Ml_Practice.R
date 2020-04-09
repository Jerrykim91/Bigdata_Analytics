'''
#### 아래 링크를 클릭해 한국복지패널데이터 파일을 다운로드하세요.

[Koweps_hpc10_2015_beta1.sav](http://bit.ly/Koweps_hpc10_2015_v2)  

### 한국 복지 패널 데이터
  - 한국보건사회연구원 발간  
  - 가구의 경제활동을 연구해 정책 지원에 반영할 목적  
  - 2006 ~ 2015년까지 전국에서 7000여 가구를 선정해 매년 추적 조사  
  - 경제활동, 생활실태, 복지욕구 등 수천 개 변수에 대한 정보로 구성 

'''

install.packages("foreign") # foreign 패키지 설치
install.packages("readxl")

library(foreign) # SPSS 파일 로드
library(dplyr) # 전처리
library(ggplot2) # 시각화
library(readxl) # 엑셀 파일 불러오기

# 데이터 불러오기
raw_welfare <- read.spss(file = "R_DataAnalysis/data/Koweps_hpc10_2015_beta1.sav", to.data.frame = T)

# 복사본 만들기
welfare <- raw_welfare

head(welfare, 3)
# tail(welfare)
# View(welfare)
dim(welfare)
str(welfare)
# summary(welfare)
# • 대규모 데이터는 변수가 많고 변수명이 코드로 되어 있어서 전체 데이터 구조를 한눈에 파악하기 어려움
# • 변수명을 쉬운 단어로 바꾼 후 분석에 사용할 변수들 각각 파악해야 함