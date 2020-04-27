# 가상환경 설정

### 참조 교제 

- 빅데이터  하둡, 하이브로 시작하기 :< https://wikidocs.net/book/2203 >

```bash

### 시작

#############################
$ start-all.sh                           # 하둡 구동
# $ sudo service ssh start    => ssh 구동
$ start-master.sh                        # 마스터 구동 
$ start-slave.sh spark://127.0.0.1:7077  # 워커 구동
$ jps # 잘 열였는지 확인 
$ sudo ufw status   # 방화벽 확인
#############################

### 중지
#############################
# 중지
$ stop-all.sh
$ stop-master.sh
$ stop-slave.sh
#############################
# 모든 컨테이너 중지하기 
$ docker stop $(docker ps -a -q)
```

# 환결성정 - 1

## 우분투 설치 
1. 우분투 18.04 다운로드한다. 

우분투 18.04 다운로드 : <https://ubuntu.com/download/desktop/thank-you?version=18.04.4&architecture=amd64>


## virtualbox를 설치 
virtualbox 다운로드 : <https://www.virtualbox.org/wiki/Downloads>

### < 세팅 순서 > 

1. virtualbox를 연다.
2. 새로 만들기를 클릭한다.
3. 이름을 ubuntu로 입력하고 메모리를 4096(4GB)로 설정 한다. 
4. 하드디스크는 30GB로 설정한다. -> 내 컴퓨터에서 할당한다고 한다. 용량을 많이 잡으면 느려지는경향도 있다고 ... 
5. 그리고 계속 넥스트 !!!! 
6. 한국어 , 한글 타자로 설정하고 계속 패스 
7. 다 설치를 하고 바로 실행 하지말고 설정으로 진입(클릭)한다. 
8. 네트워크 -> 어뎁터에 브리치 -> 가상머신에 허용 
9. 저장소에서 디스크 추가해서 우븐투를 할당한다. 
10. 시작을 바로 클릭하지 말고 역 삼각형을 눌러 세부사항에서 일반시작 혹은 떼낼 수 있는 시작으로 구동한다. 

20. 아래의 모든과정을 진행후 사용중인 버추얼을 진행하여 버츄얼 박스에서 복제를 진행한다. 

---

## mobaxterm 터미널 프로그램 설치 
mobaxterm 다운로드 : <https://mobaxterm.mobatek.net/download-home-edition.html>

- mobaxterm이란? 
    - putty, xshell, SecureCRT와 비슷한 툴이다. 
    - SSH, telnet 등의 text 기반은 물론 RDP, X-window 등을 다 지원해 주는 한 방에 다 되는 터미널 프로그램이다. 


# 우분투 세팅 명령어  

## 기본 세팅 
1. 일단 Ubuntu에서 terminal을 연다.
    - plz Open ubuntu terminal 
    - `ctrl+alt+t `
---

```bash
# 우분투에서 터미널을 연다. 
ctrl+alt+t  # 터미널

# ubuntu terminal에서 작업
$ sudo apt update -y # 업데이트 실행 

$ sudo apt install net-tools  # 서버 주소 확인한다. 

$ ifconfig # 서버 ip 주소 -> ubunt ip 주소 확인한다. 
```

## 연결해주는 터미널 오픈 

- 작업을 시작하기 전 mobaxterm에서 작업 해줄 것이 있음 
1. ` MobaXterm_Personal_20.2.exe ` 클릭해서 mobaxterm 를 연다.
2. 오픈된 창에서 바로 보이는 네비바에서 Session을 클릭한다. 
3. SSH 클릭 Remote host에 내 우븐투 아이피 주소를 입력한다.  


### 여기서부터는 버추얼 박스.. 우븐투 작업을 열어 놓기만하고 추가적인 진행은 하지 않는다. 

```bash
# mobaxterm 에서 실행 -> 다른 서버에서 열 수 있게 환경설정 
###################################
$ sudo apt install ssh -y  #  ssh 프로그램 설치
  
$ sudo service ssh start   # ssh 구동

$ sudo ufw enable   # 방화벽 활성화

$ sudo ufw allow 22 # 방화벽 열기 22

$ sudo ufw status   # 방화벽 확인

###################################
```
---

## 최종 목표 

1. 하둡
2. 스파크 : 실시간, 빅데이터
3. 아나콘다 주피터
4. pyspark

---

```bash
# mobaxterm 에서 실행

$ hostname # 확인 

$ sudo hostnamectl set-hostname 192.168.0.19 # 호스트네임변경

$ sudo reboot # 리부팅  30초 후에 mobaxterm으로 다시 접속

# 자바 설치 
$ sudo apt install openjdk-8-jre-headless -y
$ sudo apt install openjdk-8-jdk-headless -y

# 자바 버전 확인 
$ java -version

```

## 하둡 파일 다운로드

#### 크롬에서 설치 : < http://apache.tt.co.kr/hadoop/common/hadoop-3.1.3/ >

```bash
# mobaxterm에서 하둡 다운로드 
$ wget http://apache.tt.co.kr/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz

$ tar -zxvf hadoop-3.1.3.tar.gz  # 압축풀기

$ ls

$ rm -rf 폴더명

# 자주 트러블 -> 수시로 확인 
$ nano ~/.bashrc  # 환경설정 파일

# 가장 밑으로 이동후 복사
export HADOOP_HOME=/home/user1/hadoop-3.1.3
export HADOOP_COMMON_HOME=/home/user1/hadoop-3.1.3
export HDFS_NAMENODE_USER="user1"
export HDFS_DATANODE_USER="user1"
export HDFS_SECONDARYNAMENODE_USER="user1"
export YARN_RESOURCEMANAGER_USER="user1"
export YARN_NODEMANAGER_USER="user1"
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$JAVA_HOME/bin

$ source ~/.bashrc  # 적용하기

```

## 아나콘다 설치 

```bash
# Anaconda3 다운로드 s
$ wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh


# 위에 나오는 설명은 전부 엔터 !!! 
# 그리고 나오는 거는 전부 yes  
Do you accept the license terms? [yes|no]
[no] >>>
Please answer 'yes' or 'no':'
>>> yes

Anaconda3 will now be installed into this location:
/home/user1/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/user1/anaconda3] >>> ENTER입력 
'
# 여기서도 yes 입력 
installation finished.
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[no] >>> yes 


# 재설치 할경우 삭제를 해야함 아래 코드를 입력 
$ rm -rf ~/anaconda3  # 아나콘다 삭제하기

$ source ~/.bashrc  
$ conda activate
$ conda deactivate
$ jupyter notebook   # 오 실행되 !!! 

# 
$ jupyter notebook --generate-config # 주피터 환경설정파일 생성
```

``` bash 
(base) user1@192:~$ jupyter notebook --generate-config
Writing default config to: /home/user1/.jupyter/jupyter_notebook_config.py
(base) user1@192:~$  ipython
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from notebook.auth import passwd

In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:663c62f255cd:2d3f91f82dbd9f7507a695aa2f97a225f2d60295'

#######################################################################

In [3]: from notebook.auth import passwd

In [4]: passwd()
Enter password:
Verify password:
Out[4]: 'sha1:d634556d507e:f0d3a56e2da3371e5eebe5663697cb570d2bab6e'

#######################################################################

# 1 
ctrl + -        => 번호 검색 
alt + shift + 3 => 라인 넘버 리스트화 

$ sudo apt install vim -y => 편집기 설치

$ nano ~/.jupyter/jupyter_notebook_config.py
# OR
$ vim ~/.jupyter/jupyter_notebook_config.py
    048라인 : c.NotebookApp.allow_origin = '*'  # 외부 접속 허용하기
    204라인 : c.NotebookApp.ip = '192.168.0.XXX'  #아이피 설정
    266라인 : c.NotebookApp.notebook_dir = u'/home/user1/jupyter-workspace' #작업경로 설정
    272라인 : c.NotebookApp.open_browser = False # 시작 시 서버PC에서 주피터 노트북 창이 열릴 필요 없음
    281라인 : c.NotebookApp.password = u'sha1로 시작하는 암호...' #비밀번호 설정
    292라인 : c.NotebookApp.port = 8888   #포트 설정
    
$ sudo ufw allow 8888        # 방화벽 열기

$ mkdir ~/jupyter-workspace  # 폴더생성

$ jupyter notebook --config ~/.jupyter/jupyter_notebook_config.py

# 주어진 주소로 접속하면 주피터노트북으로 이동 

```
`df -h ` => 용량확인 

```bash

# /hadoop-env.sh
$ nano ~/hadoop-3.1.3/etc/hadoop/hadoop-env.sh
    -> 54라인 export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 

# core-site
$ nano ~/hadoop-3.1.3/etc/hadoop/core-site.xml
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://192.168.0.XXX:9000</value>
    </property>
</configuration>

# hdfs-site.xml
$ nano ~/hadoop-3.1.3/etc/hadoop/hdfs-site.xml
<configuration>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/home/user1/hadoop-3.1.3/data/nameNode</value>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/home/user1/hadoop-3.1.3/data/dataNode</value>
    </property>

    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
# /mapred-site.xml
$ nano ~/hadoop-3.1.3/etc/hadoop/mapred-site.xml
<configuration>
    <property>
        <name>map.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>

# yarn-site.xml 
$ nano ~/hadoop-3.1.3/etc/hadoop/yarn-site.xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>

# 네임노드 데이터노드 디렉토리 생성
$ mkdir -p ~/hadoop-3.1.3/data/nameNode
$ mkdir -p ~/hadoop-3.1.3/data/dataNode

# 인증키 등록 
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa  # 파일 생성 
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys # 파일 내용 복사
# 0600으로 권한을 변경 
$ chmod 0600 ~/.ssh/authorized_keys

# 암호없이 접속되는지 확인
$ ssh localhost

# name노드 포멧
$ hdfs namenode -format

$ start-all.sh

$ jps

# 7377 NameNode
# 8537 Jps
# 8042 ResourceManager
# 7580 DataNode
# 7822 SecondaryNameNode
# 8222 NodeManager

$ sudo ufw allow 9000
$ sudo ufw allow 9870
$ sudo ufw allow 9864
$ sudo ufw allow 9866


# 크롬에서 192.168.0.XXX:9870

$ hdfs dfs -ls  # 없음
$ hdfs dfs -mkdir /test1  # 하둡 파일시스템에 폴더 생성 

****** 실패시 ***********************************
1. 프로세스 중지
$ stop-all.sh
2. jps로 확인
3. 환경설정 다시확인
4. 데이터노드 네임노드의 폴더안의 파일 지우기
$ rm -rf ~/hadoop-3.1.3/data/nameNode
$ rm -rf ~/hadoop-3.1.3/data/dataNode

$ mkdir -p ~/hadoop-3.1.3/data/nameNode
$ mkdir -p ~/hadoop-3.1.3/data/dataNode

name노드 포멧
$ hdfs namenode -format

$ start-all.sh

$ jps
7377 NameNode
8537 Jps
8042 ResourceManager
7580 DataNode
7822 SecondaryNameNode
8222 NodeManager

***************************************************

```

---

# VsCode 설치 

1. 설치        => ` sudo apt-get install curl` 
2. 경로를 복사 => `sudo sh -c 'curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg'` 
3. 경로 추가   => `sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'`
4. 패키지 목록 불러오기  =>  `sudo apt-get update`
5. vscode 설치          =>  `sudo apt-get install code`
6. 실행                 =>  `code`

만약에 깃 허브가 필요하면 깃을 설치해서 써야함 
깃 설치 `sudo apt-get install git`

```bash

# 레지스트리 다운로드 
동일하게 `git clone 레지스트리 경로.git`
# 레지스트리 삭제 
`rm -rf ~/레지스트리 이름 `

```
## 방화벽 

```bash
# UFW 활성화/비활성화
sudo ufw enable  # 활성화 
sudo ufw disable # 비활성화 
sudo ufw status verbose # UFW 상태 확인

# 기본 툴
- 들어오는 패킷에 대해서는 전부 거부(deny)
- 나가는 패킷에 대해서는 전부 허가(allow)

# 기본룰 확인 
sudo ufw show raw
sudo ufw default deny # 기본 정책 차단 
sudo ufw default allow # 기본 정책 허용 

# 포트 허용 
sudo ufw allow 22     # ssh 포트 22번 거부(tcp/udp 22번 포트를 모두 거부)
sudo ufw allow 22/tcp # tcp 22번 포트만을 거부
sudo ufw allow 22/udp # udp 22번 포트만을 거부

sudo ufw delete deny 22/tcp # UFW 룰의 삭제

# 로그기록 
sudo ufw logging on 
sudo ufw logging off

```

# 환경설정 - 2

```bash
 
$ start-all.sh # 하둡 구동 
$ sudo apt install scala -y # scala 설치 
$ wget http://apache.tt.co.kr/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz # 다운로드
$ tar -xzvf spark-2.4.5-bin-hadoop2.7.tgz  # 압축출기 

$ nano ~/.bashrc
# 가장 밑에 추가
export SPARK_HOME=/home/user1/spark-2.4.5-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# 리부팅하고 진행 

$ source ~/.bashrc

$ cd ~/spark-2.4.5-bin-hadoop2.7/conf

$ cp spark-env.sh.template spark-env.sh
$ cp spark-defaults.conf.template spark-defaults.conf

$ nano spark-env.sh
# **************** 맨 아래에 작성 *********************
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/home/user1/hadoop-3.1.3
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native
export SPARK_LOCAL_IP="192.168.0.XXX"  # => local ip
export PYSPARK_PYTHON=/home/user1/anaconda3/bin/python3
export PYSPARK_DRIVER_PYTHON=/home/user1/anaconda3/bin/python3
export SPARK_MASTER_HOST="192.168.0.XXX"  # => 원격 접속ip
export SPARK_WORKER_INSTANCES=1
export SPARK_WORKER_MEMORY=4096m
export SPARK_WORKER_CORES=8
export SPARK_MASTER_OPTS="-Dspark.deploy.defaultCores=5"
# ******************************************************

$ nano spark-defaults.conf
spark.master                spark://127.0.0.1:7077
spark.executor.instances    1
spark.executor.cores        3
spark.executor.memory       4g
spark.driver.cores          1
spark.driver.memory         4g

# 방화벽 열기 
$ sudo ufw allow 7077

$ start-master.sh       =>spark 마스트 구동

$ start-slave.sh spark://127.0.0.1:7077 =>spark 슬레이브 구동

$ jps
3009 SecondaryNameNode
4262 Master            => 추가 됨.
2727 DataNode
4314 Worker            => 추가 됨.
3434 NodeManager
2538 NameNode
3243 ResourceManager
4349 Jps

#############################
# 중지
$ stop-all.sh
$ stop-master.sh
$ stpp-slave.sh
#############################

$ pip install pyspark 
$ conda install -c conda-forge pyspark  # 위에꺼 안될시

# 터미널을 1개 추가로 접속

$ jupyter notebook

크롬에서 http://192.168.0.XXX:8888


```

### 다운로드하는 동안 도커 설치 


```bash

# 우분투에 docker설치
- Docker 설치 이미지 리포지토리 키 가져오기
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 리포지토리 추가하는 부분
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   
$ sudo apt install -y docker-ce docker-ce-cli containerd.io

# docker그룹에 추가
$ sudo usermod -aG docker user1

# 리부팅 해야하기 그다음 단계를 잘 진행가능 때문에 스파크 설치 이후에 진행 
# 설치가 다 되었으면 재부팅을 시작 mobaxterm,  역시 virtualbox 도 같이 리부팅 

$ docker -v # 확인 

$ docker search mariadb  # 파일 확인 

$ docker pull mariadb  # 마리아 디비 당겨오기 

$ docker run --name mariadb-01 -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 mariadb

$ docker container ls -a  # 구동 리스트 확인 

$ docker exec -it mariadb-01 bash # mariadb-01컨테이너로 진입

$ exit # 여기까지 도커 

```
## 주피터에서 파일 열어서 진행 

```py
# 주피터에서 파일 열어서 진행 

# 패키지 불러오기
from pyspark.sql import SparkSession
import pandas as pd

#파이썬 설치 위치 지정
import os
# 파일 경로를 지정 
os.environ['PYSPARK_PYTHON']='/home/user1/anaconda3/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON']='/home/user1/anaconda3/bin/python3'

#스파크 객체 생성 
spark = SparkSession.builder.master("local[*]") \
    .enableHiveSupport().appName("hive01") \
    .config("spark.sql.warehouse.dir","/user/hive/warehouse") \
    .config("spark.datasource.hive.metastore.uris","hdfs://192.168.0.19:9000") \
    .getOrCreate()

#테이터 프레임 생성
df1 = spark.createDataFrame([(1,'a',10),(2,'b',20),(3,'c',30)]).toDF("id","name","age")
df1.printSchema()
df1.show()

# 데이터 프레임을 df1_table로 만듬
df1.createOrReplaceTempView("table1")
spark.sql("SELECT id, name FROM table1").show()

# 데이터프레임을 pandas로 변경
pd1 = df1.select("*").toPandas()
print(type(pd1))

# 하둡 : DB 생성
spark.sql("create database db05") 

# 데이터 프레임으로 테이블 생성
spark.sql("create table db05.t01 as select * from table1")

# 데이터 추가하기
spark.sql("insert into db05.t01 values(4,'a1',40)")

# 테이블 내용 가져오기
spark.sql("select * from db05.t01").show()
# DELETE / UPDATE는 hadoop에서 지원하지 않음.

```
# 환경설정 - 3 

```bash

$ wget https://archive.apache.org/dist/kafka/2.2.0/kafka_2.11-2.2.0.tgz

$ tar -zxvf kafka_2.11-2.2.0.tgz # 압축풀기

$ nano ~/.bashrc  
# 마지막줄에 추가 
export KAFKA_HOME=/home/user1/kafka_2.11-2.2.0
export PATH=$PATH:$KAFKA_HOME/bin

$ source ~/.bashrc

# 방화벽열기
$ sudo ufw allow 2181  # zookeeper
$ sudo ufw allow 9092  # kafka

######################## zookeeper ################################

# 편집하기(확인)
$ nano ~/kafka_2.11-2.2.0/config/zookeeper.properties
    dataDir=/tmp/zookeeper
    clientPort=2181
    maxClientCnxns=0

# zookeeper 서버 구동 &를 마지막에 붙이면 백그라운드로 구동됨.-> 화면에 안뜸 
$ ~/kafka_2.11-2.2.0/bin/zookeeper-server-start.sh ~/kafka_2.11-2.2.0/config/zookeeper.properties &

# zookeeper 서버 구동 확인
$ jps
    16494 QuorumPeerMain

# [필요 시] zookeeper 서버 중지
$ ~/kafka_2.11-2.2.0/bin/zookeeper-server-stop.sh

######################## kafka ################################

# server.properties 환경설정 
$ nano ~/kafka_2.11-2.2.0/config/server.properties
    31 라인 : listeners=PLAINTEXT://0.0.0.0:9092
    36 라인 : advertised.listeners=PLAINTEXT://192.168.0.XXX:9092
    123 라인 : zookeeper.connect=127.0.0.1:2181
    가장마지막라인에 추가 : delete.topic.enable=true

# kafka 서버 구동
$ ~/kafka_2.11-2.2.0/bin/kafka-server-start.sh ~/kafka_2.11-2.2.0/config/server.properties &


# kafka 서버 구동 확인
$ jps
   >>> 16494 QuorumPeerMain
   >>> 1234 Kafka

# [필요시] kafka 서버 중지
$ ~/kafka_2.11-2.2.0/bin/kafka-server-stop.sh    

# 토픽 생성 => testTopic2  => '채널'
$ ~/kafka_2.11-2.2.0/bin/kafka-topics.sh --create --zookeeper 127.0.0.1:2181 --replication-factor 1 --partitions 1 --topic testTopic2

# 토픽 확인
$ ~/kafka_2.11-2.2.0/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181   

체크 >>>
# 실시간 데이터 확인 시 사용 -> 오호라

# Producer생성 -> 입력 
$ ~/kafka_2.11-2.2.0/bin/kafka-console-producer.sh --broker-list 192.168.0.70:9092 --topic testTopic2

# Consumer생성 -> 출력 
$ ~/kafka_2.11-2.2.0/bin/kafka-console-consumer.sh --bootstrap-server 192.168.0.70:9092 --topic testTopic2 --from-beginning

# [필요 시 : 토픽삭제]
$ ~/kafka_2.11-2.2.0/bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --delete --topic testTopic2

```

### 서버 안에서 - vscode에서 파일 열어서 진행 
```py
############################################
import time, threading, multiprocessing
from kafka import KafkaConsumer, KafkaProducer
#pip install kafka-python


class Abc(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        while not self.stop_event.is_set():
            print("A")
            time.sleep(3)

            if self.stop_event.is_set():
                break
            


class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        #auto_offset_reset => latest(마지막), earliest(처음부터)
        consumer = KafkaConsumer(bootstrap_servers='192.168.0.70',
            auto_offset_reset='latest', consumer_timeout_ms=1000)
        consumer.subscribe(['testTopic2'])    
        while not self.stop_event.is_set():
            for msg in consumer:
                str = (msg.value).decode('utf-8')
                print(str)

                if self.stop_event.is_set():
                    break
        consumer.close()


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self): 
        producer = KafkaProducer(bootstrap_servers='192.168.0.70:9092')

        while not self.stop_event.is_set():
            str = input('send msg : ')
            producer.send('testTopic2', str.encode()) #string to byte
            time.sleep(3)
            
        producer.close() 
        
        
def main():
    tasks = [Consumer(), Producer(), Abc()]
    
    for tmp in tasks:
        tmp.start()
    time.sleep(1000)    

    for tmp in tasks:
        tmp.stop()

    for tmp in tasks:
        tmp.join()    

if __name__ == '__main__':
    main()        


############################################
```
### 구동

```bash
$ start-all.sh          # hadoop 구동
$ start-master.sh       # spark 마스트 구동
$ start-slave.sh spark://127.0.0.1:7077 # spark 슬레이브 구동

# kafka필요 라이브러리 다운로드
$ wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.11/2.4.5/spark-sql-kafka-0-10_2.11-2.4.5.jar

$ wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.11.0.0/kafka-clients-0.11.0.0.jar

```

```py
##### kafka spark ##########################################
from pyspark.sql import SparkSession
import pandas as pd
import os
os.environ['PYSPARK_PYTHON']='/home/user1/anaconda3/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON']='/home/user1/anaconda3/bin/python3'

spark = SparkSession.builder.master("local[*]") \
    .appName("exam01") \
    .config('spark.driver.extraClassPath','/home/user1/spark-sql-kafka-0-10_2.11-2.4.5.jar' ) \
    .config('spark.driver.extraClassPath','/home/user1/kafka-clients-0.11.0.0.jar' ) \
    .config('spark.jars.packages','org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5' ) \
    .getOrCreate()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers","192.168.0.70:9092") \
    .option("subscribe", "testTopic2") \
    .option("startingOffsets", "latest") \
    .load()

# df의 값을 변경해서 df1에 보관
df1 = df.selectExpr("CAST (key AS STRING)", "CAST(value AS STRING)")

# df1의 실시간 값을 console에 출력함
df1.writeStream.outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .trigger(processingTime="10 seconds") \
    .start() \
    .awaitTermination()

```

# 환경설정 - 4 

```bash
######################################################
SERVER1, SERVER2, SERVER3에 hostname변경
$ sudo hostnamectl set-hostname 192.168.0.1X  => 완료
# 192.168.0.70
$ sudo hostnamectl set-hostname 192.168.0.2X  => 변경 후 리부팅
# 192.168.0.4
$ sudo hostnamectl set-hostname 192.168.0.3X  => 변경 후 리부팅
# 192.168.0.104

######################################################
SERVER1, SERVER2, SERVER3에 편집
$ sudo nano /etc/hosts
위쪽에 추가
192.168.0.1X  (탭)   hadoop1
192.168.0.2X  (탭)   hadoop2
192.168.0.3X  (탭)   hadoop3

$ sudo service networking restart  => 편집 적용



######################################################
SERVER1, SERVER2, SERVER3에 편집

$ nano ~/.bashrc  => 환경설정 파일
가장 밑으로 이동후 복사
export HADOOP_HOME=/home/user1/hadoop-3.1.3
export HADOOP_COMMON_HOME=/home/user1/hadoop-3.1.3
export HADOOP_MAPRED_HOME=${HADOOP_HOME}    => 추가
export HADOOP_HDFS_HOME=${HADOOP_HOME}      => 추가
export YARN_HOME=${HADOOP_HOME}             => 추가
export HDFS_NAMENODE_USER="user1"
export HDFS_DATANODE_USER="user1"
export HDFS_SECONDARYNAMENODE_USER="user1"
export YARN_RESOURCEMANAGER_USER="user1"
export YARN_NODEMANAGER_USER="user1"
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$JAVA_HOME/bin

$ source ~/.bashrc    => 환경설정 적용하기

######################################################
# 여기까지 완성 

SERVER1, SERVER2, SERVER3 편집

$ nano ~/hadoop-3.1.3/etc/hadoop/core-site.xml    => 변경할 것 없음
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://192.168.0.1:9000</value>
    </property>
</configuration>


$ nano ~/hadoop-3.1.3/etc/hadoop/hdfs-site.xml
<configuration>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/home/user1/hadoop-3.1.3/data/nameNode</value>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/home/user1/hadoop-3.1.3/data/dataNode</value>
    </property>

    <property>
        <name>dfs.replication</name>
        <value>3</value> <!-- 데이터 노드 개수만큼 -->
    </property>
</configuration>


$ nano ~/hadoop-3.1.3/etc/hadoop/mapred-site.xml   => 편집
<configuration>
    <property>
        <name>mapreduce.jobtracker.address</name>
        <value>192.168.0.1X:54311</value><!-- 첫번째 PC로 지정 -->
    </property>

    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>


$ nano ~/hadoop-3.1.3/etc/hadoop/yarn-site.xml  => 편집
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>

    <property>
       <name>yarn.resourcemanager.hostname</name>
       <value>192.168.0.1X</value><!-- 첫번째 PC로 지정 -->
    </property>
</configuration>


###################################################3
SERVER1에서 인증키 생성 
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys

SERVER2, SERVER3에 폴더생성 /home/user1/폴더 아래에 .ssh폴더가 있어야 함
$ mkdir ~/.ssh

SERVER1에서
$ scp ~/.ssh/authorized_keys 192.168.0.2:/home/user1/.ssh/authorized_keys
$ scp ~/.ssh/authorized_keys 192.168.0.3:/home/user1/.ssh/authorized_keys

* 192.168.0.1에서 192.168.0.2 으로 암호없이 접속가능해야함.
* 192.168.0.1에서 192.168.0.3 으로 암호없이 접속가능해야함.

*******이것만!!******************
SERVER1에서 암호없이 접속되는지 확인
$ ssh 192.168.0.2   exit
$ ssh 192.168.0.3   exit

####################################################
SERVER1에서만
$ sudo ufw allow 54311

$ nano ~/hadoop-3.1.3/etc/hadoop/masters
192.168.0.1

$ nano ~/hadoop-3.1.3/etc/hadoop/workers
192.168.0.1
192.168.0.2
192.168.0.3

#################################################

SERVER1, SERVER2, SERVER3에서 수행
$ rm -rf ~/hadoop-3.1.3/data/nameNode
$ rm -rf ~/hadoop-3.1.3/data/dataNode

$ mkdir -p ~/hadoop-3.1.3/data/nameNode
$ mkdir -p ~/hadoop-3.1.3/data/dataNode

name노드 포멧
$ hdfs namenode -format

#################################################

SERVER1에서 수행하면 SERVER2, SERVER3이 자동 구동됨
$ start-all.sh

SERVER1에서 jps
29555 Jps
28804 SecondaryNameNode
29205 NodeManager
29031 ResourceManager
28362 NameNode
28540 DataNode

SERVER2에서 jps
3394 NodeManager
3230 DataNode
3519 Jps

SERVER3에서 jps
3161 DataNode
3437 Jps
3325 NodeManager

#################################################

크롬에서 192.168.0.1:9870 수행했을때 datanode가 3개

##################################################

$ start-master.sh
$ start-slave.sh spark://127.0.0.1:7077
$ jps
```
```py
##################################################
# 데이터 프레임을 df1_table로 만듬
# df1.createOrReplaceTempView("df1_table")
from pyspark.sql import SparkSession
import pandas as pd

# 파이썬 설치 위치 지정
import os
os.environ['PYSPARK_PYTHON']='/home/user1/anaconda3/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON']='/home/user1/anaconda3/bin/python3'

# 스파크 객체 생성 
spark = SparkSession.builder.master("local[*]") \
    .enableHiveSupport().appName("hive01") \
    .config("spark.sql.warehouse.dir","/user/hive/warehouse") \
    .config("spark.datasource.hive.metastore.uris","hdfs://192.168.0.19:9000") \
    .getOrCreate()

# 테이터 프레임 생성
df1 = spark.createDataFrame([(1,'a',10),(2,'b',20),(3,'c',30)]).toDF("id","name","age")
df1.printSchema()
df1.show()

df1.createOrReplaceTempView("table1")  #데이터 프레임을 table1로 만듬
spark.sql("SELECT id, name FROM table1").show()

spark.sql("create database db06") # DB 생성

#데이터 프레임으로 테이블 생성
spark.sql("create table db06.t01 as select * from table1")

#테이블 내용 가져옴.
spark.sql("select * from db06.t01 where age>20").show()

######### graph ########################################################
```
`$ wget http://dl.bintray.com/spark-packages/maven/graphframes/graphframes/0.7.0-spark2.4-s_2.11/graphframes-0.7.0-spark2.4-s_2.11.jar`

```py
# 파일명 : graph01
from pyspark.sql import SparkSession

import os
os.environ['PYSPARK_PYTHON']='/home/user1/anaconda3/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON']='/home/user1/anaconda3/bin/python3'

spark = SparkSession.builder.master("local[*]").enableHiveSupport().appName("spark_app1") \
    .config('spark.driver.extraClassPath','/home/user1/graphframes-0.7.0-spark2.4-s_2.11.jar') \
    .config('spark.jars.packages', 'graphframes:graphframes:0.7.0-spark2.4-s_2.11').getOrCreate()

from graphframes import GraphFrame
from pyspark.sql.functions import desc     

# https://towardsdatascience.com/graphframes-in-jupyter-a-practical-guide-9b3b346cebc5
v1 = spark.createDataFrame([('1', 'Carter', 'Derrick', 50), 
                                  ('2', 'May', 'Derrick', 26),
                                 ('3', 'Mills', 'Jeff', 80),
                                  ('4', 'Hood', 'Robert', 65),
                                  ('5', 'Banks', 'Mike', 93),
                                 ('98', 'Berg', 'Tim', 28),
                                 ('99', 'Page', 'Allan', 16)],
                                 ['id', 'name', 'firstname', 'age'])
e1 = spark.createDataFrame([('1', '2', 'friend'), 
                               ('2', '1', 'friend'),
                              ('3', '1', 'friend'),
                              ('1', '3', 'friend'),
                               ('2', '3', 'follows'),
                               ('3', '4', 'friend'),
                               ('4', '3', 'friend'),
                               ('5', '3', 'friend'),
                               ('3', '5', 'friend'),
                               ('4', '5', 'follows'),
                              ('98', '99', 'friend'),
                              ('99', '98', 'friend')],
                              ['src', 'dst', 'type'])
                              
g = GraphFrame(v1, e1)
## Take a look at the DataFrames
#g.vertices.show()
print(g.vertices.count())
print(g.edges.count())

# g.edges.show()
## Check the number of edges of each vertex
g.degrees.show()     

g.bfs(fromExpr="id='1'", toExpr="id='4'", maxPathLength=30).show(truncate=False)


###################################################################33

```

## 우븐투에서 도커 설치 
- Docker 설치 이미지 리포지토리 키 가져오기

```bash
# 리포지토리 키 가져오기 
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 리포지토리 추가하는 부분 
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# 설치  
$ sudo apt install -y docker-ce docker-ce-cli containerd.io
# docker그룹에 추가
$ sudo usermod -aG docker user1

# 리부팅
$ sudo reboot 

################# tensorflow ##################

$ docker search tensorflow
# https://www.tensorflow.org/install/docker?hl=ko

$ docker pull tensorflow/tensorflow:latest-gpu-py3-jupyter

$ sudo ufw allow 8889

$ docker run -it --name tf01 -d -p 8889:8888 tensorflow/tensorflow:latest-gpu-py3-jupyter

$ docker logs tf01

# 컨테이너로 진입 
$ docker exec -it tf01 bash

    $ 컨테이너> jupyter notebook --generate-config # 주피터 환경설정파일 생성
    $ 컨테이너> ipython => 암호 만들기
        ln [1]: from notebook.auth import passwd
        ln [2]: passwd()
        Enter password: 1234  # 암호 입력
        Verify password: 1234 # 암호 재입력
        Out[2]: 'sha1:a1s2d3f4...' # 입력한 비밀번호 암호화
        In[3]: exit() 
    $ exit로 컨테이너를 빠져나옴 -> 괄호 빼고 

# 'sha1:ade7b07e630b:9a4d905bdc37f3a01cb7e6b95e46e4ae95975df2'

# 컨테이너 내부에 있는 파일을 우분투의 현재 폴더로 복사함
$ docker cp tf01:/root/.jupyter/jupyter_notebook_config.py /home/user1

# 편집함
$ nano /home/user1/jupyter_notebook_config.py
    281라인 : c.NotebookApp.password = u'sha1로 시작하는 암호...' # 비밀번호 설정

# 편집한 파일을 다시 컨테이너로 복사함.
# docker cp 원본파일 복사할파일
$ docker cp jupyter_notebook_config.py tf01:/root/.jupyter/jupyter_notebook_config.py

# 컨테이너 중지
$ docker stop tf01

# 컨테이너 다시 구동
$ docker start tf01

```

# 환경설정 - 5 

- 도커 컨테이너 실행해서 

```bash 
# 도커 컨테이너 열어서 

# 이미지 당겨오기
$ docker pull jupyter/pyspark-notebook

$ docker image

$ docker run -it --name spark01 -p 8889:8888 jupyter/pyspark-notebook

```
### 선택적 

```bash

# Docker 설치 이미지 리포지토리 키 가져오기
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 리포지토리 추가하는 부분
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   
$ sudo apt install -y docker-ce docker-ce-cli containerd.io

# vagrant(username)를 docker그룹에 추가
$ sudo usermod -aG docker vagrant

$ docker --version
   >>> Docker version 19.03.5, build 633a0ea838

# 재부팅 **********여기까지 Dockerfile*******************
##########################################################
```
### 도커에서 

```bash
# 수동으로 이미지 빌드
$ docker build --no-cache -t hadoop3 .

# 이미지 확인
$ docker images

# 컨테이너 생성
$ docker run --hostname=hadoop3 -p 8088:8088 -p 9870:9870 -p 9864:9864 -p 19888:19888 \
  -p 8042:8042 -p 8888:8888 --name hadoop3 -d hadoop3

# 컨테이너 확인
$ docker container ls

```
## 주피터에 작성 

```py
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType, DateType

spark = SparkSession.builder.enableHiveSupport() \
        .appName("pipeline_sample") \
        .master("local[*]") \
        .getOrCreate()
        
# 훈련용 데이터 (키, 몸무게, 나이, 성별)
df1 = spark.createDataFrame([
    (161.0, 69.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 58.32, 29, 0.0),
    (163.0, 70.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 60.32, 29, 0.0),
    (169.4, 75.3, 42, 0.0),
    (168.4, 76.3, 42, 0.0),
    (185.1, 85.0, 37, 1.0),
    (161.6, 61.2, 28, 1.0)
]).toDF("height", "weight", "age", "gender")  

df1.printSchema()
df1.show()

schema = StructType() \
    .add("height", DoubleType(), True) \
    .add("weight", DoubleType(), True) \
    .add("age", IntegerType(), True) \
    .add("gender", DoubleType(), True)

df2 = spark.createDataFrame([
    (161.0, 69.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 58.32, 29, 0.0),
    (163.0, 70.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 60.32, 29, 0.0),
    (169.4, 75.3, 42, 0.0),
    (168.4, 76.3, 42, 0.0),
    (185.1, 85.0, 37, 1.0),
    (161.6, 61.2, 28, 1.0)], schema) 
df2.printSchema()
df2.show()

#-------------------------------------------------------

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.pipeline import PipelineModel

assembler = VectorAssembler(inputCols=["height", "weight", "age"], outputCol="features")

# training 데이터에 features 컬럼 추가
# assembled_training = assembler.transform(df2)
# assembled_training.show(truncate=False)

# 모델 생성 알고리즘 (로지스틱 회귀 평가자)
lr = LogisticRegression(maxIter=10, regParam=0.01, labelCol="gender")

pipeline = Pipeline(stages=[assembler, lr]) # 파이프라인
pipelineModel = pipeline.fit(df2) # 파이프라인 모델 생성
pipelineModel.transform(df2).show(truncate=False) # 파이프라인 모델을 이용한 예측값 생성


```

### 우분투에서
```bash

$ sudo apt update -y
$ sudo apt install git -y

$ git clone https://github.com/bbonnin/docker-hadoop-3.git

# 다운받으면 docker-hadoop-3폴더가 생성됨.
$ cd docker-hadoop-3

# 폴더로 이동해서 Dockerfile을 연 다음 Dockerfile의 모든 내용 지우고 아래로 내용으로 변경
***** Dockerfile의 모든 내용 지우고 아래로 내용으로 변경 ******

FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
ENV HADOOP_HOME /opt/hadoop
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN apt-get update
RUN apt-get install -y --reinstall build-essential
RUN apt-get install -y ssh
RUN apt-get install -y rsync
RUN apt-get install -y vim
RUN apt-get install -y net-tools
RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y python2.7-dev
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libkrb5-dev
RUN apt-get install -y libffi-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y libldap2-dev
RUN apt-get install -y python-lxml
RUN apt-get install -y libxslt1-dev
RUN apt-get install -y libgmp3-dev
RUN apt-get install -y libsasl2-dev
RUN apt-get install -y libsqlite3-dev  
RUN apt-get install -y libmysqlclient-dev

RUN \
    if [ ! -e /usr/bin/python ]; then ln -s /usr/bin/python2.7 /usr/bin/python; fi

RUN \
    wget https://archive.apache.org/dist/hadoop/core/hadoop-3.1.1/hadoop-3.1.1.tar.gz && \
    tar -xzf hadoop-3.1.1.tar.gz && \
    mv hadoop-3.1.1 $HADOOP_HOME && \
    for user in hadoop hdfs yarn mapred; do \
         useradd -U -M -d /opt/hadoop/ --shell /bin/bash ${user}; \

    done && \
    for user in root hdfs yarn mapred; do \
         usermod -G hadoop ${user}; \
    done && \

    echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_DATANODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
#    echo "export HDFS_DATANODE_SECURE_USER=hdfs" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_NAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_SECONDARYNAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export YARN_RESOURCEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/yarn-env.sh && \
    echo "export YARN_NODEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/yarn-env.sh && \
    echo "PATH=$PATH:$HADOOP_HOME/bin" >> ~/.bashrc

RUN \
    ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

ADD *xml $HADOOP_HOME/etc/hadoop/

ADD ssh_config /root/.ssh/config

ADD start-all.sh start-all.sh

EXPOSE 8088 9870 9864 19888 8042 8888

CMD bash start-all.sh
ENV DEBIAN_FRONTEND teletype

********** 여기까지 Dockerfile *******************

```

## NOSQL 설치 

```bash
#-------------------------------------------------------
# NOSQL
$ docker pull mongo    # 이미지 가져오기

$ docker images        # 이미지 확인 

# 생성 + 구동
$ docker run --name mongodb -d -p 32766:27017 mongo
$ docker logs mongodb

# 구동
$ docker start mongodb

$ docker exec -it mongodb bash # 도커 컨테이너로 진입

#-----------------------------------------------------
https://nosqlbooster.com/downloads
>>> nosqlbooster4mongo-5.2.10.exe
#-----------------------------------------------------
# 컨테이너 내부에서 다운로드
$ docker exec -it mongodb bash

[필요시] $ mv 파일명 /home
$ apt update
$ apt install wget
$ cd /home
$ wget https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.11/2.4.1/mongo-spark-connector_2.11-2.4.1.jar
$ wget https://repo1.maven.org/maven2/org/mongodb/mongo-java-driver/3.9.1/mongo-java-driver-3.9.1.jar

EXIT로 컨테이너 탈출

# spark01  컨테이너 구동 후 주피터 실행
$ docker start spark01

$ docker logs spark01
```
### 주피터에서 
```py
from pyspark.sql import SparkSession
import os
#from pyspark.sql.functions import col, column, window
from pyspark.sql import functions as F


spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://192.168.99.100:32766/db1.table1") \
    .config("spark.mongodb.output.uri", "mongodb://192.168.99.100:32766/db1.table1") \
    .config('spark.driver.extraClassPath', './home/mongo-spark-connector_2.11-2.4.0.jar') \
    .config('spark.driver.extraClassPath', './home/mongo-java-driver-3.9.0.jar') \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.4.0') \
    .getOrCreate()

people = spark.createDataFrame([("Bilbo Baggins",  50), ("Gandalf", 1000), ("Thorin", 195), ("Balin", 178), ("Kili", 77),
   ("Dwalin", 169), ("Oin", 167), ("Gloin", 158), ("Fili", 82), ("Bombur", None)], ["name", "age"])

# DB에 추가
people.write.format("com.mongodb.spark.sql.DefaultSource").mode("overwrite").save()

# DB에서 가져오기
df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.show()

```
```py
#-------------------------------------------------------
import pandas as pd
data = {
    "juso" : ["서울시","인천시","부산시","대구시"],
    "name" : ["kim","lee","park","choi"],
    "age" : [20, 30 , 40, 50]}

# pandas 데이터 프레임
data = pd.DataFrame(data)

# spark 데이터 프레임
df2 = spark.createDataFrame(data)
df2.show()

# DB에 저장
df2.write.format("com.mongodb.spark.sql.DefaultSource") \
    .option("spark.mongodb.output.uri", "mongodb://192.168.99.100:32766/db1.table2") \
    .mode("overwrite").save()

# DB에서 읽기
df2 = spark.read.format("com.mongodb.spark.sql.DefaultSource") \
    .option("spark.mongodb.input.uri","mongodb://192.168.99.100:32766/db1.table2") \
    .load()

df2.createOrReplaceTempView("table2")
spark.sql("SELECT age, juso, name FROM table2").show()

#--------------------------------------------------------------------------------

import pymongo

conn = pymongo.MongoClient("192.168.99.100", 32766) #서버주소, 포트번호
db = conn.get_database("db1") #db선택
collection = db.get_collection("table3")
dic1 = {"id":"pyid", "pw":"aaa","name":'abc', "age":33} #딕셔너리 생성

# mongodb에 추가
collection.insert_one(dic1)

# mongodb에 값 가져오기
get_member = collection.find()

# 가져온 값 출력하기
for tmp in get_member:
    print(tmp['id'], tmp['pw'], tmp['name'], tmp['age'], end='\n')
    

```
