comments<-gsub("<.*?>","",review)

comments<-gsub("\t","",comments)

comments<-gsub("[][!#$%*,:;<=>@_`|‘~{}&★☆ㅋㅎ《》◈△▲▽▼○●◎◇◆□◁◀▷▶♤♠♡♥♧♣◉◈▣◐◑♨☏☎☜☞↖↘♭♩♪♬㈜]", " ",comments)

comments<-gsub("rdquo|gt|lt|nbsp|amp|quot|apos","",comments)

comments<-gsub("  "," ",comments)

comments<-gsub("\\^"," ",comments)

comments<-gsub("ㅠ|ㅜ|ㅡ"," ",comments)

comments<-gsub("\"|\n|+","",comments)

comments<-gsub("\\+","",comments)

comments<-gsub("/|!|\\*|\\+|\\@"," ",comments)

comments<-gsub("'","",comments)

comments<-gsub("\"","",comments)

comments<-gsub("\"","",comments)

comments<-gsub("=","",comments)

comments<-gsub("~|;|<|>","",comments)

comments<-gsub("\\?","",comments)

comments<-gsub("\\[.*?\\]","",comments)

comments<-gsub("\\(.*?\\)","",comments)

comments<-gsub("\\(|\\)"," ",comments)

comments<-gsub("\\]|\\[|\\(|\\)|:|-|\\,|\\."," ",comments)

comments<-gsub("\\!","",comments)

comments<-gsub("\"\"","",comments)


er<-c("","것","원","저","년","역","나","이","수","월","한","동","대","전","층","들","때",

      "개","분","적","후","점","시","별","보건증","곳","번","해서","쪽","데","말","시작","우리",

      "이번","중","지원","사러가기","명","주","기","소","률","판","판매목표","구","지금샵","co","kr","com","무단전재","저작권자",

      "일","or","드","뭐","백","천","듯","만","우","잭","거","애","등","두","타","to","the","copyrights","properties","var",

      "내","제","함","지","라","안","혜")