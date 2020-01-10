# api/urls.py

from django.urls import path
from . import views 


urlpatterns = [
     
     # api 서버 생성 실습  
     path('select4', views.select4, name = 'select4'),
     # 용 오빠 코드
     path('select3', views.select3, name = 'select3'),
     # 강의 코드 
     path('select2', views.select2, name = 'select2'),
     path('select1', views.select1, name = 'select1'),
     path('insert1', views.insert1, name = 'insert1'),

]