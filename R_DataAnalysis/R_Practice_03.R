# https://news.nate.com/recent?cate=pol&mid=n0201&type=c&date=20200409&page=11

# install.packages('stringr')
library(stringr)
page <- 1 
final_data <- NULL
date = 20200409
# page = 1

url <- paste0("https://news.nate.com/recent?cate=pol&mid=n0201&type=c&date=",date,'&page=',page)
url
# 그 주소를 읽는다.
read_file <- readLines(url, encoding="UTF-8") # -> 요소 검사 페이지 전부 스크래핑 
# Fu_Element-> x
str(read_file)
length(read_file)

Fu_Element <- read_file[str_detect(read_file, "subject_fixed")]








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
