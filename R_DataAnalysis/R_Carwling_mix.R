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
