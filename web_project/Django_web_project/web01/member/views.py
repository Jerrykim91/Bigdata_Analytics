# member/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 함수형으로 생성
def index(request):
    #return HttpResponse("index page")
    return render(request, 'member/index.html') # 확장자 명 빼먹지 말기 

def join(request):
    return ""
    

def login(request):
    return ""
    