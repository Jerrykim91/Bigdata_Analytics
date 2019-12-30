# memeber/ urls.py

from django.urls import path 
# 현재 패키지 => views모듈 호출 
from . import views


# Member
# http://127.0.0.1:8000/member/index => 인덱스(index) 함수 동작 => views.py 에서 
# http://127.0.0.1:8000/member/join
# http://127.0.0.1:8000/member/login

# Board
# http://127.0.0.1:8000/member/login

urlpatterns = [
    # 경로 생성 => 함수형 뷰를 호출 => member/views.py로 부터 
    path('index', views.index, name = 'index'),
    path('join' , views.join,  name = 'join'),
    path('login', views.login, name = 'login')
]