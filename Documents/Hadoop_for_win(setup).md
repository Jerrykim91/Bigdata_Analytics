# Hadoop_for_win(setup).md
---



# Hadoop for Windows Version set it up
---
## 다운로드 
```
하둡 홈페이지에서 다운로드 =>  https://hadoop.apache.org/releases.html

버전 3.1.2	=> binary (checksum signature) 클릭         
    => 자동으로 다운 안될 때 눌러서 다운  
    => http://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz 
```
---
## 자바 버전 확인 
```bash
# 버전 확인 명령어 
$ java -version
# jdk 버전 확인 
>>> java version "1.8.0_211"
```
- 자바가 없으면 자바 설치
- 설치 후
    - 환경변수 (고급시스템에서 환경변수)
        1. 자바 홈 설정 
        - JAVA_HOME 
            - C:\Program Files\Java\jdk1.8.0_211
        2.Path 
        - 새로만들기 
            - C:\Program Files\Java\jdk1.8.0_211\bin  
            - OR =>  %JAVA_HOME%\bin 
            
    ```bash
    C:\>where java # 이렇게 쳤을 때
    #>>> 아래와 같이 출력 되면 Good
    C:\Program Files\Java\jdk1.8.0_211\bin\java.exe
    C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe
    ```
- hadoop-3.1.2.tar 압축 풀기 
    - C:\Bigdata 새 폴더를 만든다 
    - 반디집을 관리자 권한으로 열어서 C:\Bigdata 위치에 압축을 품 

- hadoop-3.1.2_winutils 설치 
    - 압축을 풀면 bin 이라는 폴더 생김 
    - hadoop-3.1.2.tar 압축을 풀어 생긴 hadoop-3.1.2 열고 bin 폴더에 들어감    
    - hadoop-3.1.2_winutils(bin)을 빈을 열어 hadoop-3.1.2(bin)에 덮어 씀     


---

## 하둡 설정 파일 

|설정파일|설명|
|---------|---|
|conf/masters|세컨더리 네임노드가 동작하는 노드를 명시|
|conf/slaves|데이터노드와 태스크 트래커가 동작하는 노드를 명시|
|conf/hadoop-env.sh|하둡이 실행하는 모든 프로세스에 적용되는 시스템 환경 관련 스크립트|
|conf/core-site.xml|하둡 분산 파일 시스템과 하둡 맵리듀스 모두에 적용할 수 있는 스크립트|
|conf/hdfs-site.xml|하둡 분산 파일 시스템 설정 스크립트|
|conf/mapred-site.xml|하둡 맵리듀스 설정 스크립트|


---