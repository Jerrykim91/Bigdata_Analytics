# api/urls.py

from django.urls import path
from . import views 


urlpatterns = [
     
     # api 서버 생성 실습  
     path('insert1', views.insert1, name = 'insert1'),
     path('select1', views.select1, name = 'select1'),
]