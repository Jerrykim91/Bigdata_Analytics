# member/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

cursor = connection.cursor()

# Create your views here.

#join1
@csrf_exempt #?
def join1(request):
    if request.method == 'GET':
        return render(request, 'member/join1.html')

#list
def list(request):
    # ID기준으로 오름차순
    sql = "SELECT * FROM MEMBER ORDER BY ID ASC"
    cursor.execute(sql) # sql문 실행
    data = cursor.fetchall() # 결과값을 가져옴
    print(type(data)) #list
    print(data) #[(1,2,3,4,5), (   ), (   )]

    #list.html을 표시하기 전에
    #list변수에 data값을,  title변수에 "회원목록" 문자를
    return render(request, 'member/list.html', {"list":data, "title":"회원목록"})

# index
def index(request): # 함수형으로 생성
    #return HttpResponse("index page")
    return render(request, 'member/index.html') # 확장자 명 빼먹지 말기 


# login
@csrf_exempt
def login(request):
    # data => 회원정보
    if request.method == 'GET':
        return render(request, 'member/login.html')

    elif request.method == 'POST':
        ar = [request.POST['id'], request.POST['pw']]
        sql ="""
            SELECT ID, NAME FROM MEMBER
            WHERE ID=%s AND PW=%s
        """
        cursor.execute(sql,ar)
        data = cursor.fetchone()
        # 확인 작업 
        print(type(data))
        print(data)

        #
        if data: 
            request.session['userid'] = data[0]
            request.session['username'] = data[1]
            print('userid: ',request.session['userid'])
            print('username:', request.session['username'])
            return redirect('/member/index')

        return redirect('/member/index')

# edit
@csrf_exempt
def edit(request):
    # data => 회원정보
    if request.method == 'GET':
        ar = [ request.session['userid']]
        sql = """ 
            SELECT ID, NAME FROM MEMBER
            WHERE ID=%s
            """
        cursor.execute(sql,ar)
        data = cursor.fetchone()
        print(data)

        return render(request,'member/edit.html',{"one": data})
    elif request.method == 'POST':
        ar = [
            request.POST['id'],
            request.POST['name'],
            request.POST['age']
        ]
        # 업데이트 문 
        sql = """
        UPDATE MEMBER SET NAME=%s, AGE=%s
        WHERE ID=%s
        """
    cursor.execute(sql,ar)

    return redirect('/member/index')

#id 기본키 => 중복안되게 설정 해두었음

# logout
@csrf_exempt
def logout(request):
    # data => 회원정보
    if request.method == 'GET' or request.method =='POST':
        del request.session['userid']  
        del request.session['username'] 
        return render(request, '/member/index')

    #return redirect('/member/login')

# delete
@csrf_exempt
def delete(request):
    # data => 회원정보
    if request.method == 'GET' or request.method =='POST':
        # 이 구조를 이해해야 ar 대신 뭐를 변수 명으로 넣을지 선정할수 있을 것 같음 
        # 일단은 ar은 배열의 약자
        ar = [ request.session['userid'] ]
        # 업데이트 문 
        sql = """
        DELETE FROM MEMBER WHERE ID=%s
        """
        cursor.execute(sql,ar)

        return render(request, '/member/logout')

@csrf_exempt # post로 값을 전달 받는 것은 필수 
def join(request):
    # 만약에 get을 요청하면 요청받은 렌더링('member/join.html')을 리턴
    if request.method == 'GET':
        return render(request, 'member/join.html')
    # 만약에 post을 요청하면 새로운 경로를 송신 => '/member/index'
    elif request.method == 'POST':
        ID   = request.POST['id'] # html에서 넘어오는 값 
        PW   = request.POST['pw']
        # PW   = request.POST['pw']
        AGE  = request.POST['age']
        NAME = request.POST['name']
       
        # 왜 ar ?
        ar = [ID, PW, AGE, NAME]
        #ar = [ID, PW, AGE, NAME]
        print(ar)
        # DB에 추가 

        # MEMBER(id, pw, age, name, joindate) DB의 테이블 인덱스 네임과 같아야한다. 
        sql = """
        INSERT INTO MEMBER(id, pw, age, name, joindate)
        VALUES (%s,%s,%s,%s, sysdate)
        """
        # 실행  
        #cursor.execute(sql,[, parametwers]])
        cursor.execute(sql,ar)

        # 크롬에서 http://127.0.0.1:8000/member/index 엔터키를 자동화
        return redirect('/member/index')
    

