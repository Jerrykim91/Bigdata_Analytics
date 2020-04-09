install.packages("tidyverse")
install.packages("multilinguer")
install.packages(c('hash','tau','sejong','RSQLite','devtools', type='binary')
install.packages("remotes")
remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts = c("--no-multiarch"))

install.packages("DBI")
install.packages("bit64")
install.packages("blob")


install.packages('stringr')
library(stringr)

#--------------
'''
https://news.nate.com/view/20200409n19748?mid=n0100
https://news.nate.com/view/20200409n19747?mid=n0100
https://news.nate.com/view/20200409n19746?mid=n0100
'''
#--------------
'https://news.nate.com/recent?mid=n0100  => recent  : 최신뉴스 
 https://news.nate.com/section?mid=n0200 => section : 그외 선택 
'
'https://news.nate.com/recent?mid=n0108 => https://news.nate.com/recent?mid=소주제 

<a href="/recent?cate=pol&amp;mid=n0201&amp;type=c&amp;date=20200409&amp;page=11" onclick="ndrclick('RML03');" class="next"><img src="//nimg.nate.com/ui/uidev/images/button/btn_pagenext.gif" width="16" height="13" alt="다음"></a>

'

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
