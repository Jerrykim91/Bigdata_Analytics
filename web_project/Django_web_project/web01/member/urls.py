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
    # html을 생성 할때 마다 경로 생성 
    path('index', views.index, name = 'index'),
    path('join' , views.join,  name = 'join'),
    path('login', views.login, name = 'login'),
    path('join1', views.logout,name = 'logout'),
    path('list', views.list, name = 'list'),
    path('edit', views.edit, name = 'edit'),
    path('join1', views.join1, name = 'join1'),
    path('delete', views.delete, name = 'delete')
    
]

#  수정 
# path('list', views.login, name = 'list'),
# path('join1', views.login, name = 'join1')
