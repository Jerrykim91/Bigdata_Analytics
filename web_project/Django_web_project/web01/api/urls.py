# api/urls.py

from django.urls import path
from . import views 


urlpatterns = [
     
     # 샘플 
     path('select1', views.select1, name = 'select1'),
]