# member/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
# 검색 해봅시다.
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

# Create your views here.

# 함수형으로 생성
def index(request):
    #return HttpResponse("index page")
    return render(request, 'member/index.html') # 확장자 명 빼먹지 말기 



@csrf_exempt # post로 값을 전달 받는 것은 필수 
def join(request):
    # 만약에 get을 요청하면 요청받은 렌더링('member/join.html')을 리턴
    if request.method == 'GET':
        return render(request, 'member/join.html')
    # 만약에 post을 요청하면 새로운 경로를 송신 => '/member/index'
    elif request.method == 'POST':
        ID   = request.POST['id'] # html에서 넘어오는 값 
        PW   = request.POST['pw']
        AGE  = request.POST['age']
        NAME = request.POST['name']
       
        # 왜 ar ?
        ar = [ID, PW, AGE, NAME]
        print(ar)
        # DB에 추가 

        cursor = connection.cursor()
        # MEMBER(id, pw, age, name, joindate) DB의 테이블 인덱스 네임과 같아야한다. 
        sql = """
        INSERT INTO MEMBER(id, pw, age, name, joindate)
        VALUES (%s,%s,%s,%s, datetime())
        """
        # 실행  
        #cursor.execute(sql,[, parametwers]])
        cursor.execute(sql,ar)

    # 크롬에서 http://127.0.0.1:8000/member/index 엔터키를 자동화
        return redirect('/member/index')
    

def login(request):
    return HttpResponse("login page")
    