# board\urls.py
# Board
# http://127.0.0.1:8000/board/

# import 
# 경로 설정 -> 장고의 urls -> path
from django.urls import path
# 현재 패키지 => view 모듈(views.py)에서 호출 
# => 행위(메소드)가 정의 되어있다. 
from . import views 

# 경로 생성 => 함수형 뷰를 호출 
# Board/views.py로 부터 => html을 생성 할때 마다 경로 생성 
# path('urls이름', views.urls이름, name = 'urls이름')
urlpatterns = [
     
     # 샘플 
     path('list_m', views.list_m, name = 'list_m'),

     # 게시판 생성
     path('list', views.list, name = 'list'),
     path('write', views.write, name = 'write'),
     path('content', views.content, name = 'content'),
     path('edit', views.edit, name = 'edit'),
     path('delete', views.delete, name = 'delete'),
     path('dataframe', views.dataframe, name = 'dataframe'),

     # 성적 등록 시스템 
     path('t2_update_all', views.t2_update_all, name = 't2_update_all'),
     path('t2_insert_all', views.t2_insert_all, name = 't2_insert_all'),
     path('t2_update', views.t2_update, name = 't2_update'),
     path('t2_delete', views.t2_delete, name = 't2_delete'),
     path('t2_list', views.t2_list, name = 't2_list'),
     path('t2_insert', views.t2_insert, name = 't2_insert')
    
]
