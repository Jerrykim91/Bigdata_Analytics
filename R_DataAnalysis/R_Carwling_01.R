#--------------------------------------------------------------------#
# 클리앙의 모두의 공원 게시글을 수집하는 코드 
# 
# 크롤링은 html소스를 보고 진행하는것이 이해가 빠름 
# 긁고자 하는 사이트에서 오른쪽 마우스 클릭 -> 소스보기를 하면 소스를 볼 수 있다.
# 그 소스내에 내가원하는 정보가 있는 위치를 찾고, 규칙을 찾아 원하는 정보만 추출합니다. 
# 예를 들어 게시판의 제목이 <h2>제목</h2> 이렇게 만 나온다고한다면
# <h2>가 있는 line만 찾아서 뽑으면 될것입니다.


# 글 목록, 조회수, 글 본문 링크 정보 수집 
install.packages('stringr')
library(stringr)

i <- 1 
final_data <- NULL

for(i in 1:10){
    # 주소를 담아서 
    url <- paste0("https://www.clien.net/service/board/park?&od=T31&po=", i-1)
    url
    # 그주소를 읽는다.
    b <- readLines(url, encoding = "UTF-8")
    str(b) # b에 담긴 데이터를 확인한다. 
    length(b)
    head(b)
    tail(b)

    b2 <- b[str_detect(b, "subject_fixed")]
    str(b2)
    title <- str_extract(b2,("(?<=\">).*(?=</span>)")) # page로 시작하고 </a> 끝나는 가운데 것을 뽑아 낸다.
    str(title)

    # 
    b3 <- b[str_detect(b,"<span class=\"hit\">")] 
    str(b3) # <span class=\"hit\">769.9 k</span>" 

    hit <- str_extract(b3,("(?<=\">).*(?=</span>)"))[-1]
    b4 <- str_split(b3, "hit\">")
    str(b4)
    # hit <- str_sub(sapply(b4,function(x){x[2]}), end= -8) # 1951</span>" 끝에서 9번째 부터 
    hit <- str_sub(sapply(b4,function(x){x[2]}), end= -8) # 문제네 
    hit

    b[which(str_detect(b,"subject_fixed"))]
    b[(str_detect(b,"subject_fixed"))]
    b5 <- b[which(str_detect(b,"subject_fixed"))-2]
    str(b5)
    b6 <- str_sub(str_extract(b5, ("(?<=href=\").*(?=data-role)")), end=-4)
    str(b6)

    url <- paste0("https://www.clien.net", b6)
    url

    data <- cbind(title,hit,url)
    data

    final_data <- cbind(final_data,data)
    final_data
    length(title)
    length(hit)
    length(url)
    cat("\n", i)
}

# 데이터 확인 
dim(final_data)
head(final_data)
tail(final_data)

# 글 목록 수집 데이터에서 글 본문 링크로 글 본문 수집 
setwd("./")
write.csv(final_data, file = "./data/base_data.csv", row.names=F)
# 데이터 확인 
head(data)
# save(data, file ="./data/base_data.csv")
# load("./data/base_data.csv")

library(stringr)
url_list <- data[,3]

length(url_list) # 길이 
content <- c()
for(i in 1 : length(url_list)){
    b <- readLines(as.character(url_list[1]), encoding="UTF-8")
    if(class(try(b <- readLines(as.character(url_list[i]), encoding="UTF-8"))) == "try-error"){
        b6 <- ""
        content <- c(content, b6)
    }else {
        b2 <- b[which(str_detect(b, "post_content")):which(str_detect(b, "post_ccls"))]
        b3 <- paste(b2, collapse="")
        str(b3) 
        b4 <- gsub("<.*?>", "", b3)
        str(b4)
        b5 <- gsub("\t|&nbsp;", "", b4)
        str(b5)
        b6 <- str_trim(b5)
        content <- c(content, b6)
        cat("\n", i)
    }
}
# 데이터 확인 
head(content)

final_data < - cbind(data, content)
setwd("./")
write.csv(final_data, file = "./data/final_data.csv", row.names=F)

# 글 본문 데이터를 이용하여 형태소 분석 및 워드 클라우드 실행하는 실습 진행 
setwd("./")
final_data <- read.csv("./data/final_data.csv", encoding="EUC-KR", fileEncoding="EUC-KR")
head(data)

# 패키지_ 
install.packages("KoNLP")     # 형태소 분석
install.packages("wordcloud") # 워드클라우드 
install.packages ( "DBI")
install.packages ( "bit64")
install.packages ( "blob")

library(KoNLP) # 한글 형태소 분석기
library(dplyr) # 데이터프레임 다루는 라이브러리
# useNIADic()  # 사전 데이터
library(stringr) # 텍스 처리 라이브러리
library(RColorBrewer) # 칼라 팔레트
library(wordcloud) # 워드클라우드 라이브러리

# 시작 
txt <- str_replace_all(final_data[,4], "\\W", " ")
str(txt)
nouns <- extractNoun(txt)
head(nouns)
wordcount <- table(unlist(nouns))
wordcount
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
str(df_word)
df_word <- rename(df_word, word = Var1, freq = Freq)
str(df_word)
df_word <- filter(df_word, nchar(word) >= 2)
top_20 <- df_word %>% arrange(desc(freq)) %>% head(20)
top_20

?brewer.pal
pal <- brewer.pal(8, "Dark2")
set.seed(1234)


wordcloud(words = df_word$word, # 단어 
            freq = df_word$freq, # 빈도 
            min.freq = 2, # 최소 단어 빈도 
            max.words = 200, # 표현 단어 수 
            random.order = F, # 고빈도 단어 중앙 배치 
            rot.per = .1, # 회전 단어 비율 
            scale = c(4, 0.3), # 단어 크기 범위 
            colors = pal) # 색깔 목록


# KoNLP 설치
'''
각 개인 컴퓨터 R 패키지 경로에 KoNLP.zip 압축을 푼다.
예) C : \ Users \ admin \ Documents \ R \ win-library \ 3.6
압축 풀 압축 파일명을 폴더 명으로.
R KoNLP 실행 전 설치해야 할 패키지
install.packages ( "DBI")
install.packages ( "bit64")
install.packages ( "blob")
라이브러리 (KoNLP)
'''