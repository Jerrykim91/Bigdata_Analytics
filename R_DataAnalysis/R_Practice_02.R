install.packages("Rcpp")
install.packages("uesthis")
install.packages("glue")

# devtools 설치 및 임포트
install.packages("devtools")
library(devtools)

# remotes 설치 및 임포트
install.packages("remotes")
library(remotes)

'''
# mrchypark/tqk 
# install_github("mrchypark/tqk")
# library(mrchypark/tqk)
# 동일한 아이피로 여러명이 접속 했더니 에러
'''

# 재설정 경로 
install_github ( "mrchypark / krwifi")

install.packages("foreign")  # foreign 패키지 설치
install.packages("readxl")

library(foreign)             # SPSS 파일 로드
library(dplyr)               # 전처리
library(ggplot2)             # 시각화
library(readxl)              # 엑셀 파일 불러오기


# 데이터 불러오기
raw_welfare <- read.spss(file = "./data/Koweps_hpc10_2015_beta1.sav",to.data.frame=T)

# 복사본 만들기
welfare <- raw_welfare
# welfare
# dim(welfare)
head(welfare)     # Raw 데이터 앞부분 확인
tail(welfare)     # Raw 데이터 뒷부분 확인
View(welfare)     # Raw 데이터 뷰어 창에서 확인
dim(welfare)      # 행, 열 출력
str(welfare)      # 데이터 속성 확인
summary(welfare)  # 요약 통계량 출력

# 컬럼명 바꾸기 
welfare <- rename(welfare,
                  sex = h10_g3,            # 성별
                  birth = h10_g4,          # 태어난 연도
                  marriage = h10_g10,      # 혼인 상태
                  religion = h10_g11,      # 종교
                  income = p1002_8aq1,     # 월급
                  code_job = h10_eco9,     # 직종 코드
                  code_region = h10_reg7)  # 지역 코드


head(welfare)      # 행, 열 출력

# 