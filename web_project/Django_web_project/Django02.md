# Django DB 연동

```bash
$ cd C:\Users\ihong\Documents\python1  <= 폴더 이동(예시 _ 자기 폴더 위치 C에 생성하시오=> 빠르고 편함)
$ conda install django  <= 모듈 설치(모듈이 없다면 설치)
$ django-admin startproject project1  <= project1생성(원하는 이름의 폴더를 생성)
$ cd project1 <= 생성한 프로젝트 폴더로 이동
$ django-admin startapp member <= member 앱 생성
$ django-admin startapp board <= board 앱 생성(여러개 생성 가능)
$ python manage.py runserver <= django 서버 구동(http://127.0.0.1:8000/)

```

---

Django web project
    ㄴ Web01 => 공통으로 통제하기 수월함
        ㄴ urls.py () 
        ㄴ setting.py ()
    ㄴ manage.py
    ㄴ Member
        ㄴ views.py (함수형 뷰)
        ㄴ urls.py  (함수형 뷰 호출 => member/views.py로부터)
    ㄴ Static (CSS)
        ㄴ CSS
    ㄴ Templates(HTML)
        ㄴ member
            ㄴ index.html
    ㄴ Board
    ㄴ Blog 


---
