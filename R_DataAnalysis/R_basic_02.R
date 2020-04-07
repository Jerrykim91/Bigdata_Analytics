#--------------------------------------------------------------------#

# 데이터 프레임 만들기 
# 시험 성적데이터를 만들어 봅세 
english <- c(90, 80, 60, 70)  # 영어 점수 변수 생성
english

math <- c(50, 60, 100, 20)    # 수학 점수 변수 생성
math

# english, math로 데이터 프레임 생성해서 df_midterm에 할당
df_midterm <- data.frame(english, math)
df_midterm

class <- c(1, 1, 2, 2)
class

# 데이터 프레임에 영어,수학, 강의실을 담아 출력 
df_midterm <- data.frame(english, math, class)
df_midterm

# 평균 : 데이터프레임 $ 시리즈 -> 내가 입력한 시리즈의 평균이 산출   
mean(df_midterm$english)  # df_midterm의 english로 평균 산출
mean(df_midterm$math)     # df_midterm의 math로 평균 산술

df_midterm <- data.frame(english = c(90, 80, 60, 70),
                         math = c(50, 60, 100, 20),
                         class = c(1, 1, 2, 2))

df_midterm

#--------------------------------------------------------------------#

install.packages("readxl") # 설치
library(readxl)

# 엑셀 파일 불러오기
df_exam <- read_excel("./data/excel_exam.xlsx")  # 엑셀 파일을 불러와서 df_exam에 할당
df_exam                                          # 출력

mean(df_exam$english)
mean(df_exam$science)


df_exam_novar <- read_excel("./data/excel_exam_novar.xlsx")
df_exam_novar

df_exam_novar <- read_excel("./data/excel_exam_novar.xlsx", col_names = F)
df_exam_novar

# 엑셀 파일의 세 번째 시트에 있는 데이터 불러오기
df_exam_sheet <- read_excel("./data/excel_exam_sheet.xlsx", sheet = 3)
df_exam_sheet

#-------------------------------------------------------------------------------#

# df_csv_exam <- read.csv('./data/csv_exam.csv') 
# df_csv_exam
# df_csv_exam <- read.csv("csv_exam.csv", stringsAsFactors = F)

#-------------------------------------------------------------------------------#

df_midterm <- data.frame(english = c(90, 80, 60, 70),
                         math = c(50, 60, 100, 20),
                         class = c(1, 1, 2, 2))
df_midterm
write.csv(df_midterm, file = "./data/df_midterm.csv")

#-------------------------------------------------------------------------------#

save(df_midterm, file = "./data/df_midterm.rda") # 저장
rm(df_midterm) # 
load("./data/df_midterm.rda") # 로딩해보기

#-------------------------------------------------------------------------------#

# 1.변수 만들기, 데이터 프레임 만들기
english <- c(90, 80, 60, 70)  # 영어 점수 변수 생성
math <- c(50, 60, 100, 20)    # 수학 점수 변수 생성
data.frame(english, math)     # 데이터 프레임 생성

# 2. 외부 데이터 이용하기

# 엑셀 파일
library(readxl)                                 # readxl 패키지 로드
df_exam <- read_excel("excel_exam.xlsx")        # 엑셀 파일 불러오기

# CSV 파일
df_csv_exam <- read.csv("csv_exam.csv")         # CSV 파일 불러오기
write.csv(df_midterm, file = "df_midterm.csv")  # CSV 파일로 저장하기

# Rda 파일 -> R 객체를 R 고유의 형식으로 저장하는 데 사용
load("df_midterm.rda")                          # Rda 파일 불러오기
save(df_midterm, file = "df_midterm.rda")       # Rda 파일로 저장하기

#-------------------------------------------------------------------------------#
# 혼자 해보기 
# 제품 -> Product
Product <- c("Apple", "Strawberry", "Watermelon") # 사과, 딸기, 수박
Product
# 금액 -> Price
Price <- c(1800,1500,3000)
Price
# 판매량 -> SalesRate
SalesRate <- c(24, 38, 13)
SalesRate
# 데이터 프레임 생성 
df_sales<- data.frame(Product, Price , SalesRate)
df_sales

mean(df_sales$Price)      # Price 기준으로
mean(df_sales$SalesRate)  # SalesRate 기준으로
#-------------------------------------------------------------------------------#
