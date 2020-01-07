# member/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

# 장고에서 제공하는 모델 
# => 원래는 그냥 호출 가능한데 로그인 로그아웃 함수가 아래에 생성되어 있음   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth1
from django.contrib.auth import login as login1
from django.contrib.auth import logout as logout1
# 모델 불러오기 
from .models import Table1
# 추가모델 => 계산 
from django.db.models import Sum, Max, Min, Count, Avg

# 변수
cursor = connection.cursor()

# Create your views here.



# 1. 테이블에 회원 20명을 추가하시오 
# 
# ex) 101 102 506 409

# urls.py
# exam_insert
@csrf_exempt
def exam_insert(request):
    # 니가 하는 일은 무엇이냐 => 성적을 입력 받는 일! 
    if request.method == 'GET': 
        return render(request,'member/exam_insert.html',{"cnt":range(10)}) 

    elif request.method == 'POST':
        name = request.POST.getlist('name[]')
        kor  = request.POST.getlist('kor[]')
        eng  = request.POST.getlist('eng[]')
        math = request.POST.getlist('math[]')
        classroom = request.POST.getlist('classroom[]')

        # 객체를 5개를 넣는다는 개념 => 한번에 5개 받을수 있는 기능

        objs = []
        for i in range(0, len(name), 1):
            obj = Table1()
            obj.name      = name[i]
            obj.kor       = kor[i]
            obj.eng       = eng[i]
            obj.math      = math[i]
            obj.classroom = classroom[i]
            objs.append(obj) 

        # 일괄 추가 
        Table1.objects.bulk_create(objs)
        print(objs)

        # # 객체를 불러와야지 
        # obj = Table1()
        # # 디비로부터 뭘 받아 오느냐 
        # obj.name      = request.POST['name']
        # obj.kor       = request.POST['kor']
        # obj.eng       = request.POST['eng']
        # obj.math      = request.POST['math']
        # obj.classroom = request.POST['classroom']
        # obj.save() 

        return redirect("/member/exam_select")

# 입력 받고 디비까지 올리는거    


# exam_update
@csrf_exempt
#  수정 = > 안됨 
def exam_update(request):
    # 
    if request.method == 'GET': 
        # 세션을 받아옴 => 왜 ?
        n = request.session['no']

        # 이해가 안됨 
        rows = Table1.objects.filter(no__in = n)
        return render(request, 'member/exam_update.html', {"list":rows})

    elif request.method == 'POST':
        # ng
        menu = request.POST['menu']
        if menu == '1':
            no = request.POST.getlist('chk[]')
            # 소멸 되기 때문에 세션으로 넘긴다.
            request.session['no'] = no
            print(no)
            return redirect("/member/exam_update")

        elif menu == '2':
            no        = request.POST.getlist('no[]')
            name      = request.POST.getlist('name[]')
            kor       = request.POST.getlist('kor[]')
            eng       = request.POST.getlist('eng[]')
            math      = request.POST.getlist('math[]')
            classroom = request.POST.getlist('classroom[]')

            objs = []
            for i in range(0, len(no), 1):
                # 하나는 괜찮은데 => 작업 도중 작업이 끊어지면  
                obj = Table1.objects.get(no=no[i])
                obj.name = name[i]
                obj.kor  = kor[i]
                obj.eng  = eng[i]
                obj.math = math[i]
                obj.classroom = classroom[i]

                objs.append(obj)

            Table1.objects.bulk_update( objs,["name","kor","eng","math", "classroom"])
            return redirect("/member/exam_select")

# exam_delete
@csrf_exempt
# 삭제  => 확인 
def exam_delete(request):
    if request.method == 'GET': 
        n = request.GET.get("no",0)
        row = Table1.objects.get(no=n)
        row.delete() # 삭제

        return redirect("/member/exam_select")
    

# exam_select
@csrf_exempt
#  목차 
def exam_select(request):
    if request.method == 'GET': 
        # no = request.GET.get("no",0)
        # 정보 출력 => insert 입력 받은 정보 
        rows = Table1.objects.all()
        print(rows)
        return render(request,'member/exam_select.html',{"list":rows}) 
# 반별 국영수 합계 



# ===== 2020.01.07 ==== exam_select ==== 실습 ===== 



# ==============================================

# 구조 
# def auth_anything(request):
#     if request.method =='GET' :
#         if not request.User.is_authenticated:
#             return redirect("member/auth_login")
#        
#         return render(request,'member/auth_anything.html')
#     elif request.method =='POST':
#         return redirect("member/auth_home")

# ==============================================      


# auth_pw
# 유심히 확인해 본 결과 템플릿을 구성하고 뷰로 돌아와서 구성을 맞추었음 
def auth_pw(request):
    if request.method =='GET' :
        if not request.User.is_authenticated:
            return redirect("member/auth_login")

        return render(request,'member/auth_pw.html')

    elif request.method =='POST':
        pw  = request.POST['pw'] # 기존 암호
        pw1 = request.POST['pw1'] # 바꿀 암호
        # 바꾸기 전에 인증
        obj = auth1(request, username=request.user, password=pw)

        if obj:
            obj.set_password(pw1) # pw1으로 암호변경 
            obj.save()
            return redirect("member/auth_index")

        return redirect("member/auth_pw")


# auth_edit
def auth_edit(request):
    # 타인의 접근을 제한하기 위해서,  보안상 두개 같이 ! 
    if request.method =='GET' :
        if not request.User.is_authenticated:
            return redirect("member/auth_login")
    
        obj = User.objects.get(username=request.user)
        return render(request,'member/auth_edit.html',{'obj':obj})
    
    elif request.method =='POST':
        id = request.POST['username']
        na = request.POST['first_name']
        em = request.POST['email']

        obj = User.objects.get(username=id)
        obj.first_name = na
        obj.email = em
        obj.save()
        return redirect("member/auth_index")



# auth_logout
def auth_logout(request):
    # 타인의 접근을 제한하기 위해서,  보안상 두개 같이 ! 
    if request.method =='GET' or request.method =='POST':
        logout1(request) # 세션 초기화 
        return redirect("member/auth_index")


# auth_login
def auth_login(request):
    if request.method =='GET':
        return render(request, 'member/auth_login.html')
    elif request.method == 'POST':
        id =  request.POST['username']
        pw =  request.POST['password']

        # 디비인증
        obj = auth1( request, username=id, password=pw ) 
        if obj is not None :
            login1(request,obj)# 세션추가 
            return redirect("/member/auth_index")
        return redirect("/member/auth_login")
        

# auth_join
def auth_join(request):
    if request.method =='GET':
        return render(request, 'member/auth_join.html')
    elif request.method == 'POST':
        id = request.POST['username']
        pw = request.POST['password']
        na = request.POST['first_name']
        em = request.POST['email']

        obj = User.objects.create_user(
            username = id,
            password = pw,
            first_name = na,
            email = em)
        obj.save()


# auth_index
def auth_index(request):
    if request.method =='GET':
        return render(request, 'member/auth_index.html')



# ==== 2020.01.07=== auth member 추가 ==== 


#join1 => 왜 만든거야 ? 
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
    

