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
    
    # 자바스크립트 추가
    path('js_index', views.js_index, name = 'js_index'),


    # 성적 관리 시스템 
    path('exam_select', views.exam_select, name = 'exam_select'),
    path('exam_delete', views.exam_delete, name = 'exam_delete'),
    path('exam_update', views.exam_update, name = 'exam_update'),
    path('exam_insert', views.exam_insert, name = 'exam_insert'),


    # auth_member (내장 디비 사용 )
    path('auth_pw', views.auth_pw, name = 'auth_pw'),
    path('auth_edit', views.auth_edit, name = 'auth_edit'),
    path('auth_logout', views.auth_logout, name = 'auth_logout'),
    path('auth_login', views.auth_login, name = 'auth_login'),
    path('auth_join', views.auth_join, name = 'auth_join'),
    path('auth_index', views.auth_index, name = 'auth_index'),


    # 경로 생성 => 함수형 뷰를 호출 => member/views.py로 부터 
    # html을 생성 할때 마다 경로 생성 
    path('delete', views.delete, name = 'delete'),
    path('join1', views.join1, name = 'join1'),
    path('edit', views.edit, name = 'edit'),
    path('list', views.list, name = 'list'),
    path('join1', views.logout,name = 'logout'),
    path('login', views.login, name = 'login'),
    path('join' , views.join,  name = 'join'),
    path('index', views.index, name = 'index')

    
]




