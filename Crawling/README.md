# Crawling


### 2020.01.13

실습 1 - http://ihongss.com/json/exam2.json
실습 2 - http://ihongss.com/json/exam3.json


<순서>
# 도커 설치 - 1

```bash

$ docker start oracle12c
$ docker stop oracl12c

$ docker-machine stop
$ docker-machine start

$ docker search mongo  <= 이미지 검색
$ docker pull mongo    <= 이미지 가져오기

$ docker images         <= 이미지 확인 

# 컨테이너 생성
# 인증을 통해 생성
$ docker run --name mongodb -d -p 32766:27017 mongo -auth   => 빼면 (-auth) 아무나 접속 가능 
$ docker run --name mongodb -d -p 32766:27017 mongo   
$ docker logs mongodb         <= 로그 확인 

$ docker stop mongodb
$ docker rm mongodb

# 인증없이 생성
$ docker run --name mongodb -d -p 32766:27017 mongo

```
## robomongo 접속 -2 
[robomongo접속](https://robomongo.org/download)
- Robo 3T 1.3 압축파일로 다운로드 (스튜디오x)
Connection setting 
192.168.99.100 :32766

``` py
# 라이브러리 생성 
pip install pymongo
```