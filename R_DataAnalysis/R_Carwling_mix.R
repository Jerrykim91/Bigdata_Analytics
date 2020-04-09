install.packages("tidyverse")
install.packages("multilinguer")
install.packages(c('hash','tau','sejong','RSQLite','devtools', type='binary')
install.packages("remotes")
remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts = c("--no-multiarch"))

install.packages("DBI")
install.packages("bit64")
install.packages("blob")


# --------------------------------------------------------------------------------# 
# 지윤이 코드 
install.packages('stringr')
library(stringr)
final_data <- NULL
i <- 20200406
url <- paste0('https://news.nate.com/recent?cate=int&mid=n0104&type=c&date=', i-1)
url
b <- readLines(url, encoding = 'euc-kr')
length(b)
head(b, 10)
b2 <- b[str_detect(b, 'strong class')]
str(b2)
title <- str_extract(b2, ("(?<=\">).*(?=</strong>)"))
str(title)
title[2]
data <- cbind(title)
data
# --------------------------------------------------------------------------------# 
# 장원 오빠 

# 라이브러리 
library(stringr)
# 변수 준비
final_data <- NULL

date = 20200409 # 날짜 
page = 1  # 페이지 

# url 
url   <- paste0("https://news.nate.com/recent?mid=n0100&type=c&date=",date,"&page=",page)
url


b <- readLines(url, encoding="cp949")
str(b)

b2 <- b[str_detect(b, "strong class=\"tit\"")]
str(b2)

title <- str_extract(b2, ("(?<=\">).*(?=</strong>)"))[1:20]
title

b3 <- b[which(str_detect(b, "strong class=\"tit\""))-6][1:20]
head(b3)
b3

b4 <- str_sub(str_extract(b3, ("(?<=href=\").*(?=class)")), end=-4)
url <- paste0("https://", b4)
url # url 따기 

data = cbind(title, url)
data # 제목이랑 링크 ..? 아닌데 ..?
# 일단은 고 

# 네이트 뉴스 크롤링 
library(stringr) # 라이브러리 

final_data <- NULL # 최종 저장 데이터
date = 20200409 # 날짜
page = 1 # 페이지

for(page in 1:10) {
    url   <- paste0("https://news.nate.com/recent?mid=n0100&type=c&date=",date,"&page=",page)
    b <- readLines(url, encoding="cp949")
    b2 <- b[str_detect(b, "strong class=\"tit\"")]
    title <- str_extract(b2, ("(?<=\">).*(?=</strong>)"))[1:20]
    b3 <- b[which(str_detect(b, "strong class=\"tit\""))-6][1:20]
    b4 <- str_sub(str_extract(b3, ("(?<=href=\").*(?=class)")), end=-4)
    url <- paste0("https://", b4)
    data <- cbind(title, url)
    final_data <- rbind(final_data, data)
    }

final_data # 확인 -> 이건 맞아 

# 저장하기
setwd("./")
write.csv(final_data, "./Data/nate_news_base.csv", row.names=F)

setwd("./")
data <- read.csv("./Data/nate_news_base.csv")
head(data)

# --------------------------------------------------------------------------------# 
# 창석이 
library(stringr)
library(dplyr)
for(i in 1:5) {
  path  <- "https://news.nate.com/recent?cate=its&mid=n0105&type=c&date=20200409&page="
  url   <- paste0(path, i)
  b     <- readLines(url, encoding="EUC-KR")
  b2    <- b[str_detect(b, "<strong class=\"tit\">")]
  title <- str_extract(b2, ("(?<=<strong class=\"tit\">).*(?=</strong>)"))}

# --------------------------------------------------------------------------------# 
# 용
rm(list=ls(all=TRUE))

# 네이트뉴스 가져오기
# 인코딩 안될때 b3<-repair_encoding(b2)
install.packages('stringr')
library(stringr)
library(dplyr)


## -------------------------------------------------------------------- ##

final_data <- NULL # 초기화

for(i in 1:10) {
  path  <- "https://news.nate.com/recent?mid=n0100&type=c&date=20200409&page="
  url   <- paste0(path, i)
  b     <- readLines(url, encoding="EUC-KR")
  # str(source)
  length(source)
  # head(source, 10)
  

  # 게시판의 글 제목 우클릭-검사 하면 
  # <strong class="tit">'막말 제명'</strong>  
  b2    <- b[str_detect(b, "strong class=\"tit\"")]
  # str(b2)
  # b3<-repair_encoding(b2)
  head(b2, 10)
  title <- str_extract(b2, ("(?<=\">).*(?=</strong>)"))
  str(title)
}


# --------------------------------------------------------------------------------# 
