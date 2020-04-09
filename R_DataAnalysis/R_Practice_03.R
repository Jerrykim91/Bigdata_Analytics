# stringr 설치 & 임포트 
install.packages("stringr")
library(stringr)

final_data <- NULL # ? 왜 널값을 ???
i <-1
url <- paste0("https://www.clien.net/service/board/park?&od=T31&po=", i-1)
url

b <- readLines(url, encoding = "UTF-8")
# str(b)
length(b)
head(b)
tail(b)