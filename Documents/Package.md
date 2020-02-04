# Package.md 
---

# requirements.txt를 이용해 버전 일괄 인스톨하기 
    => 주로 가상환경을 생성하고 환경을 일괄적으로 맞출때 많이 사용한다.  

1. 메모장을 이용해 requirements.txt 파일을 만든다 
2. 생성한 파일을 열고 아래와 같이 기술한다. 

> 예시 
``` bash
    \---------------------------------------------
    # 프로젝트에서 사용하는 패키지를 기술한다. 

​    requests==2.18.4

​    beautifulsoup4==4.6.0

​    pandas==0.23.0

​    numpy==1.14.3

   \---------------------------------------------
   
```
3. 그리고 터미널을 열고 가상화면이면 그곳의 위치에서 오픈한다. 
    requirements.txt 파일 위치까지 경로를 이동한다.

#### pandas 폴더안에 

   $ cd 프로젝트위치(requirements.txt 위치)

    - 설치하기 전 가상환경에 설치된 패키지 확인  
        가상환경내에 설치된 패키지 목록 보기      
    ```(pandas)$ conda list or pip list```     
    - conda 와 pip는 약간의 목록이 차이는 존재      

4. **프로젝트에 필요한 패키지 설치**

   (pandas)$ pip install -r requirements.txt

   or

   (pandas)$ conda install --file requirements.txt


---
# **패키지, 라이브러리**
---
### \#Matplotlib

----

- 그래프를 그리는 모듈  -> 줄여서 plt 로 사용 

```python
 matplotlib import pyplot as plt
```

#### 선언

- 그래프의 결과를 출력세션에 나타나게 하는 설정 

```python
import matplotlib.pyplot as plt
%matplotlib inline
```



### \#Selenium

---

- Selenium은 web-application 을 위한 Testing DataFrame

  직접적으로 웹사이트에 접근할수 있게 해줌 

  - 자동화 테스트를 위해 여러가지 기능을 지원

- Selenium을 사용하기 위해서는  Web Driver 필요하다

**설치**

```bash
$pip install Selenium
```

**실행**

```python
from Selenium import webdriver

path = 'webdriver의 경로를 입력합니다.'
driver = webdriver.Chrome(path)

driver.get('web address')

```



### \#Urllib

---

- urllib는 url작업을 위한 모듈 팩이다 
  - url을 열고 읽기 - urllib.request
  - url.request에 의해 발생하는 예외를 포함하는 urllib.error
  - URL 구문을 분석하는 - urllib.parse
  - robots.txt파일을 구문 분석하기위한 urllib.robotparser

---

### **모듈, 패키지, 라이브러리**

>  & C:/Users/sun41/AppData/Local/Continuum/anaconda3/python.exe c:/Users/sun41/Desktop/Py_POO/ml/service/run.py



<< 모듈 >>

#### sys  	

  명령행으로 프로그램  인자값(Arguments Value)받음

  - 변수와 함수를 직접 제어 할수 있게 해주는 모듈 

  sys.argv 

  배열, sys.argv[0]에는 기본적으로 python 실행파일의 경로가 담겨있음  

  - 배열의 길이는 기본적으로 1 

#### os

  환경 변수나 디렉터리 ,파일등의 os 자원을 제어할수 있게 해주는 모델 

  - 환경 변수를 알고 싶을때 - os.environ
  - 위치 돌려받기 - os.getcwd
  - 위치 변경하기  - os.chdir
  - 명령어 호출하기  - os. system
  - 시스템 명령어 돌려받기 - os.popen
  - 디렉터리 생성 - os. mkdir
  - 디렉터리 삭제 - os. rmdir
    - 단 , 비어 있어야 가능함
  - 파일을 지운다  - os.unlink
  - src 파일을 dst로 바꿈 -  os.rename(src,dst)

---

###  정의

- module모듈
  - 각종 변수, 함수, 클래스를 담고 있는 파일
  - 특정 기능을 .py 파일 단위로 작성한 것

- package 패키지
  - 여러 모듈을 묶은 것
  - 특정 기능과 관련된 여러 모듈을 묶은 것

- Library 라이브러리
  - 기본으로 설치된 모듈과 패키지, 내장 함수를 묶어서 파이썬 표준 라이브러리라고함

---

**참조서적**

- [잔재미 코딩](https://www.fun-coding.org/crawl_basic2.html)
- [코딩도장](https://dojang.io/mod/page/view.php?id=2441)
- ​[python]('https://docs.python.org/ko/3/library/index.html')
  ---