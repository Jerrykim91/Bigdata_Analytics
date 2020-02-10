# Hadoop_for_win(setup).md
---



# Hadoop for Windows Version set it up
## 하둡 클러스터 구축을 위한 설정 
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

### HADOOP_HOME
- 환경변수 설정 (자바처럼 고급시스템에서 환경변수)
    - 1. 하둡 홈 설정 
        - HADOOP_HOME 
            => C:\Bigdata\hadoop-3.1.2
        - PATH 설정 
            1. bin 추가
                새로만들기 => C:\Bigdata\hadoop-3.1.2\bin  
                - %HADOOP_HOME%\bin
            2. sbin 추가 
                새로만들기 => C:\Bigdata\hadoop-3.1.2\sbin  
            - %HADOOP_HOME%\sbin

#### 확인하기 

```bash
# cmd => 새창열기 
$ set   #  all path can check  
>>> 등등등 .... 
>>> HADOOP_HOME=C:\Bigdata\hadoop-3.1.2
>>> 등등등 ....
>>> JAVA_HOME=C:\Program Files\Java\jdk1.8.0_211
>>> 등등등.... 

```


## 하둡에서 직접적으로 경로 설정 

### 1. hadoop-env.cmd
C:\Bigdata\hadoop-3.1.2\etc\hadoop\hadoop-env.cmd => VSCode에서 실행 

```bash

@rem Set Hadoop-specific environment variables here.

@rem The only required environment variable is JAVA_HOME.  All others are
@rem optional.  When running a distributed configuration it is best to
@rem set JAVA_HOME in this file, so that it is correctly defined on
@rem remote nodes.
@rem add __ used Compressed path if can not ues it = JAVA_HOME= C:\Program" "Files\Java\jdk1.8.0_211
@rem The java implementation to use.  Required.
set JAVA_HOME=%JAVA_HOME%
# 두가지 방법이 있음 
JAVA_HOME= C:\Program" "Files\Java\jdk1.8.0_211
# 압축 된 경로 
JAVA_HOME= C:\PROGRA~1\Java\jdk1.8.0_211

####

# 확인 
# cmd 창에서 
C:\Users\admin>cd \
C:\> dir /x
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: EC67-FFA4

 C:\ 디렉터리
>>> 등등등 
>>> 2020-02-10  오전 09:36    <DIR>          PROGRA~1     Program Files
>>> 등등등
# 확인 
# cmd 창에서 
C:\Users\admin>cd \
C:\> set
>>> 등등등
>USERNAME=admin
>>> 등등등


##### 
@rem The jsvc implementation to use. Jsvc is required to run secure datanodes.
@rem set JSVC_HOME=%JSVC_HOME%

@rem set HADOOP_CONF_DIR=

@rem Extra Java CLASSPATH elements.  Automatically insert capacity-scheduler.
if exist %HADOOP_HOME%\contrib\capacity-scheduler (
  if not defined HADOOP_CLASSPATH (
    set HADOOP_CLASSPATH=%HADOOP_HOME%\contrib\capacity-scheduler\*.jar
  ) else (
    set HADOOP_CLASSPATH=%HADOOP_CLASSPATH%;%HADOOP_HOME%\contrib\capacity-scheduler\*.jar
  )
)
...
...
...
@rem The directory where pid files are stored. /tmp by default.
@rem NOTE: this should be set to a directory that can only be written to by 
@rem       the user that will run the hadoop daemons.  Otherwise there is the
@rem       potential for a symlink attack.
set HADOOP_PID_DIR=%HADOOP_PID_DIR%
set HADOOP_SECURE_DN_PID_DIR=%HADOOP_PID_DIR%

@rem A string representing this instance of hadoop. %USERNAME% by default.
# 변경 => admin
set HADOOP_IDENT_STRING=admin

# 코드 추가 
set HADOOP_PREFIX = C:\Bigdata\hadoop-3.1.2
set HADOOP_CONF_DIR=%HADOOP_PREFIX%\etc\hadoop
set YARN_CONF_DIR=%HADOOP_CONF_DIR%
set PATH = %PATH%;%HADOOP_PREFIX%\bin;  %HADOOP_PREFIX%\sbin


```
---
### 2. core-site.xml 열어서 
C:\Bigdata\hadoop-3.1.2\etc\hadoop\core-site.xml => VSCode에서 실행 

```xml
<!-- Put site-specific property overrides in this file. -->

<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://0.0.0.0:9000</value>
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/c:/Bigdata\hadoop-3.1.2/tmp</value>
  </property>
</configuration>

```
---
### 3. hdfs-site.xml 열기 
C:\Bigdata\hadoop-3.1.2\etc\hadoop\ hdfs-site.xml  => VSCode에서 실행 

```xml
<!-- Put site-specific property overrides in this file. -->

<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.permissions</name>
        <value>false</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/C:/Bigdata/hadoop-3.1.2/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/C:/Bigdata/hadoop-3.1.2/datanode</value>
    </property>
</configuration>
```
---

### 4. 새 폴더 만들기 
이 경로(C:\Bigdata\hadoop-3.1.2)에 새 폴더 생성
1. tmp
2. namenode
3. datanode 
---

### 5. 하둡 버전확인 
```bash
C:\> hadoop version
Hadoop 3.1.2
Source code repository https://github.com/apache/hadoop.git -r 1019dde65bcf12e05ef48ac71e84550d589e5d9a
Compiled by sunilg on 2019-01-29T01:39Z
Compiled with protoc 2.5.0
From source with checksum 64b8bdd4ca6e77cce75a93eb09ab2a9
This command was run using /C:/Bigdata/hadoop-3.1.2/share/hadoop/common/hadoop-common-3.1.2.jar

``` 
---
### 6.mapred-site.xml 열기 
C:\Bigdata\hadoop-3.1.2\etc\hadoop\ mapred-site.xml => VSCode에서 실행 

```xml
<!-- Put site-specific property overrides in this file. -->

<configuration>
  <property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
  </property>
  <property>
  <name>mapred.job.tracker</name>
  <value>0.0.0.0:9001</value>
  </property>
</configuration>

```
---
### 7.yarn-site.xml 열기 
C:\Bigdata\hadoop-3.1.2\etc\hadoop\yarn-site.xml => VSCode에서 실행 

```xml
<configuration>

<!-- Site specific YARN configuration properties -->

  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  </property>
  <property>
    <name>yarn.log-aggregation-enable</name>
    <value>true</value>
  </property>
  <property>
    <name>yarn.nodemanager.pmem-check-enabled</name>
    <value>false</value>
  </property>
  <property>
    <name>yarn.nodemanager.vmem-check-enabled</name>
    <value>false</value>
  </property>

</configuration>

```
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