# 가상환경 설정 

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
ctrl+alt+t  => 터미널

# ubuntu terminal에서 작업
$ sudo apt update -y => 업데이트 실행 

$ sudo apt install net-tools  => 서버 주소 확인한다. 

$ ifconfig => 서버 ip 주소 -> ubunt ip 주소 확인한다. 
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
$ sudo apt install ssh -y  =>  ssh 프로그램 설치
  
$ sudo service ssh start    => ssh 구동

$ sudo ufw enable => 방화벽 활성화

$ sudo ufw allow 22 => 방화벽 열기 22

$ sudo ufw status => 방화벽 확인

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

$ hostname -> 확인 

$ sudo hostnamectl set-hostname 192.168.0.19 =>  호스트네임변경

$ sudo reboot => 리부팅  30초 후에 mobaxterm으로 다시 접속

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

$ tar -zxvf hadoop-3.1.3.tar.gz  => 압축풀기

$ ls

$ rm -rf 폴더명

$ nano ~/.bashrc  => 환경설정 파일

가장 밑으로 이동후 복사
export HADOOP_HOME=/home/user1/hadoop-3.1.3
export HADOOP_COMMON_HOME=/home/user1/hadoop-3.1.3
export HDFS_NAMENODE_USER="user1"
export HDFS_DATANODE_USER="user1"
export HDFS_SECONDARYNAMENODE_USER="user1"
export YARN_RESOURCEMANAGER_USER="user1"
export YARN_NODEMANAGER_USER="user1"
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$JAVA_HOME/bin

$ source ~/.bashrc  => 적용하기

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
$ rm -rf ~/anaconda3  => 아나콘다 삭제하기

$ source ~/.bashrc  
$ conda activate
$ conda deactivate
$ jupyter notebook # 오 실행되 !!! 

# 
$ jupyter notebook --generate-config => 주피터 환경설정파일 생성
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
    
$ sudo ufw allow 8888       => 방화벽 열기

$ mkdir ~/jupyter-workspace  => 폴더생성

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
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa  => 파일 생성 
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys => 파일 내용 복사
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

$ hdfs dfs -ls  => 없음
$ hdfs dfs -mkdir /test1  => 하둡 파일시스템에 폴더 생성 

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
$rm -rf ~/레지스트리 이름 

```
