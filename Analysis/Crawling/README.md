# Crawling
---

<순서>
# 도커 설치 - 1
```bash
# 몽고 디비 구동 및 종료
$ docker start mongodb
$ docker stop mongodb

# 오라클 디비 구동 및 종료
$ docker start oracle12c
$ docker stop oracl12c

# 도커 구동 및 종료
$ docker-machine stop
$ docker-machine start
```
```bash
# 몽고 설치 과정 
$ docker search mongo  <= 이미지 검색
$ docker pull mongo    <= 이미지 가져오기

$ docker images         <= 이미지 확인 

# 컨테이너 생성
# 인증을 통해 생성 => 빼면 (-auth) 아무나 접속 가능 
$ docker run --name mongodb -d -p 32766:27017 mongo -auth   
$ docker run --name mongodb -d -p 32766:27017 mongo   
# 설치시 로그 확인 (수시로)
$ docker logs mongodb         

# 컨테이너 삭제
$ docker stop mongodb
$ docker rm mongodb

# 인증없이 생성
$ docker run --name mongodb -d -p 32766:27017 mongo

```

## robomongo 접속 -2  
[robomongo 접속 링크](https://robomongo.org/download)     
- Robo 3T 1.3 압축파일로 다운로드 (스튜디오x)     
- robomongo 초기 세팅 => 도커랑 연결하기 위한 주소     
**Connection setting**       
```192.168.99.100 ``` : ```32766```     


### pymongo 구동을 위한 라이버리 설치 

    ``` py
    # 라이브러리 생성 
    pip install pymongo
    ```

[JSONView 확장 팩 설치 ](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?utm_source=chrome-ntp-icon)



# 항공데이터 