# https://news.nate.com/recent?cate=pol&mid=n0201&type=c&date=20200409&page=11

# install.packages('stringr')
library(stringr)
page <- 1 
naver_movie <- NULL
# date = 20200409
movie_code = 186610 # 신문기자

# page = 1

url <- paste0("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=",movie_code,"&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=",page)
url

# 그 주소를 읽는다.
read_file <- readLines(url, encoding="utf-8") # -> 요소 검사 페이지 전부 스크래핑 
head(read_file, 12) # head확인 
# Fu_Element-> x
str(read_file)
length(read_file)

# 정확한 위치 찾기 
score_result <- read_file[which(str_detect(read_file, "div class=\"star_score\""))+2] # 더하는 숫자가 의미하는 바는 뭐 인가 ? 
# test <- read_file[which(str_detect(read_file,"star_score"))+2]
head(score_result)
score_result

# 일단 찾음 -> 일단은 정리가 필요 
raw_score <- str_extract(score_result, ("(?<=<em>).*(</em>)"))
raw_score

# 정리 -> 숫자만 추출 
star_score <- str_sub(str_extract(score_result, ("(?<=<em>).*(</em>)")), end=-6)
star_score
## -------------------------------------------------------------------------------- ##


# 나는 평점하고 뭔가를 매치 하고 싶다. -> score_reple
raw1_reple <- read_file[which(str_detect(read_file, "score_result"))] 
raw1_reple

# name <- str_extract(raw1_reple, ("(?<=<a>).*(</a>)"))
# name

# raw_reple <- raw1_reple[which(str_detect(raw1_reple, "(?<=<a>).*(</a>)"))] 
# raw_reple

# # str_extract(raw_reple, ("(?<=<em>).*(</em>)"))

# score_reple <- str_sub(str_extract(raw1_reple, ("(?<=<a>).*(</a>)")),)
# score_reple

## -------------------------------------------------------------------------------- ##

url <- paste0("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=",movie_code,"&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=",page)
url
b<-readLines(url,encoding="UTF-8")
head(b, 12)

b2<-b[which(str_detect(b,"star_score"))+2]
b2
str_extract(b2,("(?<=<em>).*(</em>)"))
str_sub(str_extract(b2,("(?<=<em>).*(</em>)")), end=-6)

score<-as.numeric(str_sub(str_extract(b2,("(?<=<em>).*(</em>)")),end=-6))
score

## -------------------------------------------------------------------------------- ##

# 갱신 가능한 데이터 수가 10개라서 -> 페이지 카우트 
for( page in 1:10){
    # 주소를 
    url <- paste0("https://news.nate.com/recent?cate=pol&mid=n0201&type=c&date=",date,'&page=',page)
    url
    # 그 주소를 읽는다.
    b <- readLines(url, encoding="UTF-8")
    str(b)
    length(b)
}
