# Docker Container

> 스터디 공유 사이트  - https://trello.com/

## 도커 이미지와 컨테이너는 다르다 명확한 구분이 필요 
### 이미지에서 컨테이너가 생성 
- 이미지는 설계도 컨테이너는 집 
- REPOSITORY 안에 eda
- 어떤 이미지를 가지고 어떤 컨테이너를 만드느냐  

###  파이썬 경로 찾기 
cmd 에서 
```where python```

# 커밋으 수시로 해줘야한다 


---

## numpy, pandas 설치
```pip install pandas numpy```
- 이렇게도 설치가 되는구나 오호 ?!


## 작업 진행 중 수시로
```bash

$ docker commit eda 나의도커아이디/eda

```
# 도커로 복사 
```
$ docker cp ./b.py eda:/home/vscode/notebooks/
```

---
## 강사님 자료 

```bash

# 이미지를 가지고 오그 그이미지를 기반으로 컨테이너 생성 
#도커 허브에 있는 이미지로 컨테이너 런 (최초 실행시) = > 강사님 도커 컨테이너 
docker run --rm --name eda -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes -v /C/Users/admin/Documents/eda:/home/vscode/notebooks/eda mrsono0/base_project:eda

# 권한 체크 
$ sudo -i # 루투 계정 전환
$ cd /home/vscode # vscode 계정 홈 디렉토리 이동
$ ls -al # 디렉토리 목록 확인 notebooks
$ chown -R vscode:vscode ./notebooks # 계정 오너 조정
$ ls -al # 디렉토리 오너가  vscode로 바뀐 것 확인

# 도커 풀 이미지 가지고 오기 
$ docker pull 이미지 이름 

# 도커 컨테이너 생성 =>  강사님 만든 도커 실행 
$ docker run --rm --name eda -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes -v /C/Bigdata_Analytics/Pandas/eda:/home/vscode/notebooks/eda mrsono0/base_project:eda


# 컨테이너 접속 로그 확인 
# 하위 로그 부터 체크 부여하는 토큰 값만 확인
$ docker logs --tail 30 eda
# 상위 로그 부터 체크 부여하는 토큰 값만 확인
$ docker logs --head 30 eda

```

---

## 내가 commit 한 이미지로 컨테이너 런 실행
```bash

# 내 도커 실행을 위한 런
$ docker run --rm --name eda -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes -v /C/Bigdata_Analytics/Pandas/eda:/home/vscode/notebooks/eda sun4131/eda

$ docker run --rm --name eda -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes 계정id/이미지 이름 

docker run --rm --name eda -itd -u vscode -p 8888-8889:8888-8889  -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes sun4131/eda

# 내 도커에 커밋
$ docker commit eda sun4131/eda

# 내가 commit한 이미지를 나의 도커 허브에 push 할때
$ docker push 나의도커아이디/eda
$ docker push sun4131/eda

```


---
### token 알아내서 => 실행한 웹에 토큰 추가 
### 샐행은 웹에서 
http://192.168.99.100:8888/


### 도커 가입 
### 도커에서 확인한 다음에 아이디 작성 

### 도커 로그인 
```bash
$ docker login
Username: 아이디 
Password: 비밀번호
```

---
### 도커 컨테이너, 이미지 정리 하기
```bash
# 1. 도커 컨테이너 확인
$ docker ps -a
# 2. 사용않하는 컨테이너 커밋
$ docker commit 컨테이너이름 도커아이디/이미지이름
# 3. 도커이미지 허브 사이트에 업로드
$ docker push 도커아이디/이미지이름
# 4. 사용 않하는 컨테이너 삭제
$ docker rm 컨테이너아이디
# 5. 사용 않하는 이미지 삭제
$ docker rm 이미지아이디

```


```bash
# 이동
$ cd ..
$ cd ..
$ dir 
$ pwd
$ cd c 
$ pwd
$ cd Bigdata_Analytics/
$ cd Pandas/
```
---




# 궁금한거 
- 파워쉘은 뭐야 