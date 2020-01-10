# api/views.py

from django.shortcuts import render
# 파일 응답 
from django.http import HttpResponse
# 모델 호출 
from .models import Item

#  변수 



# Create your views here.




# insert1
def insert1(request):
    # for i in range(1, 31, 1):
    #     obj = Item()
    #     obj.name = '커피' + str(i)
    #     obj.price = 1500 + i 
    #     obj.save()

    return HttpResponse("insert1")




# select1
def select1(request):
    pass 
    


     