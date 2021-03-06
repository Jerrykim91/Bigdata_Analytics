# board/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 
from django.shortcuts import render, redirect
# HttpResponse : 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse
# URL의 변화여부가 필요하다면 Redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from base64 import b64encode
import pandas as pd
# byte 배열을 base64(이미지를 출력해주는 포멧)로 변경 
import os
# 모델을 불러 온다 => models.py 파일에서 table2 클래스를 불러옴 
from .models import Table2
from .models import Table1

# 렌더(render) 
# index에서 인자값으로 request을 받았어 
# 받았으니까 돌려줘야해 그때 render로 뭔가를 돌려주는데 
# 그게 html 페이지(위치값이랑 확장자명 빼먹지 말기 ) !!! 

# 변수
cursor = connection.cursor() #sql문 수행위한 cursor객체

# Create your views here.
# 함수형태로 생성, 기호에 따라 클래스로도 생성 가능 
# 뷰의 함수는 먼저 쓴 것을 아래로 마지막에 작성한것은 위로 가도록 작성하자 


# t2_update_all
@csrf_exempt 
def t2_update_all(request):
    if request.method == 'GET':
        # 세션에서 받아줌 
        n = request.session['no'] # n= [8, 5, 3]
        print(n)
        # SELECT * FROM BOARD_TABLE2 WHERE NO=8 OR NO=5 OR NO=3
        # SELECT * FROM BOARD_TABLE2 WHERE NO IN (8,5,3)
        #
        rows = Table2.objects.filter(no__in = n)
        return render(request, 'board/t2_update_all.html', {"list":rows})
        
    elif request.method == 'POST':
        menu = request.POST['menu']
        if menu == '1':
            no = request.POST.getlist('chk[]')
            # 소멸 되기 때문에 세션으로 넘긴다.
            request.session['no'] = no
            print(no)
            return redirect("/board/t2_update_all")

        elif menu == '2':
            no   = request.POST.getlist('no[]')
            name = request.POST.getlist('name[]')
            kor  = request.POST.getlist('kor[]')
            eng  = request.POST.getlist('eng[]')
            math = request.POST.getlist('math[]')

            objs = []
            for i in range(0, len(no), 1):
                # 하나는 괜찮은데 => 작업 도중 작업이 끊어지면  
                obj = Table2.objects.get(no=no[i])
                obj.name = name[i]
                obj.kor  = kor[i]
                obj.eng  = eng[i]
                obj.math = math[i]
                objs.append(obj)

            Table2.objects.bulk_update(objs,["name","kor","eng","math"])
            return redirect("/board/t2_list")



# t2_insert_all
@csrf_exempt 
def t2_insert_all(request):
    if request.method == 'GET':
        return render(request, 'board/t2_insert_all.html', {"cnt":range(5)})
       
    elif request.method == 'POST':
        na = request.POST.getlist('name[]') # 변수에 값 
        ko = request.POST.getlist('kor[]')
        en = request.POST.getlist('eng[]')
        ma = request.POST.getlist('math[]')

        # 객체를 5개를 넣는다는 개념 (개념이해연습 )
        objs = []
        for i in range(0, len(na), 1):
            # 하나는 괜찮은데 => 작업 도중 작업이 끊어지면  
            obj = Table2()
            obj.name = na[i]
            obj.kor  = ko[i]
            obj.eng  = en[i]
            obj.math = ma[i]
            objs.append(obj)

        # 일괄 추가 
        Table2.objects.bulk_create(objs)
        print(objs)

        return redirect("/board/t2_insert_all")
    

# t2_update
@csrf_exempt
def t2_update(request):
    if request.method == 'GET':
        n = request.GET.get("no",0)
        # SELECT * FROM BOARD_TABLE2 WHERE NO=%s
        row = Table2.objects.get(no=n) # where # 열전체를 보낸다
        return render(request,'board/t2_update.html', {"one": row})

    elif request.method =='POST':
        n = request.POST['no']

        obj = Table2.objects.get(no=n) #obj객체 생성 

        obj.name = request.POST['name'] # 변수에 값 
        obj.kor  = request.POST['kor']
        obj.eng  = request.POST['eng']
        obj.math = request.POST['math']
        obj.save() # 저장하기 수행  = 커킷
        # UPDATE BOARD_TABLE2 SET
        # NAME=%s, KOR=%s, ENG=%s, MATH=%s
        # WHERE NO= %s
        return redirect("/board/t2_list")

# t2_delete
@csrf_exempt
def t2_delete(request):
    if request.method == 'GET':
        # 
        n = request.GET.get("no",0)
        # SQL = SELECT * FROM BOARD_TABEL2  WHERE NO=%s
        row = Table2.objects.get(no=n) 
        row.delete() # 삭제

        return redirect("/board/t2_list")


# t2_list
@csrf_exempt
def t2_list(request):
    if request.method =='GET':
        # insert의 입력받은 혹은 저장된 정보 출력
        rows = Table2.objects.all() # SELECT ... 
        # SQL = SELECT * FROM BOARD_TABEL2
        # 확인
        print(rows)
        # 타입 확인 => class type
        print(type(rows))
        return render(request,'board/t2_list.html', {"list": rows}) # HTML 표시 

# t2_insert 
@csrf_exempt 
def t2_insert(request):
    if request.method == 'GET':
        return render(request, 'board/t2_insert.html')
        # 1번 => html 구조 짜고 
    elif request.method == 'POST':
        # 2번 => html 구보를 기반으로 메소드 생성  
        obj = Table2() #obj객체 생성 

        obj.name = request.POST['name'] # 변수에 값 
        obj.kor  = request.POST['kor']
        obj.eng  = request.POST['eng']
        obj.math = request.POST['math']
        obj.save() # 저장하기 수행 
        
    return redirect("/board/t2_insert")


# dataframe
def dataframe(request):
    if request.method == 'GET':
        df = pd.read_sql(
            """
            SELECT NO, WRITER, HIT, REGDATE
            FROM BOARD_TABLE1
            """, con = connection)
            # 판다스 때문에 선언한거  con = connection
        # print(df)
        print(df['NO'][:2])
        print(type(df))
        return render(request,'board/dataframe.html',{"df":df.to_html(classes="table")})

# edit
@csrf_exempt
def edit(request):
    if request.method == 'GET':
        no = request.GET.get( "no", 0 )
        sql =""" 
            SELECT NO, TITLE, CONTENT
            FROM BOARD_TABLE1
            WHERE NO = %s
        """
        cursor.execute( sql, [no] )
        data = cursor.fetchone()
        return render(request,'board/edit.html', {"one": data})

    elif request.method == 'POST':
        no = request.POST['no']
        ti = request.POST['title']
        co = request.POST['content']
        
        arr = [ ti, co, no ]
        sql = """
            UPDATE BOARD_TABLE1 SET TITLE=%s, 
            CONTENT=%s WHERE NO= %s
        """
        cursor.execute( sql, arr )
        return redirect("/board/content?no=" +no)

# delete
@csrf_exempt
def delete(request):
    if request.method == 'GET':
        #  no = request.GET["no"]
        # get(content/?no=0 )출력 할려고 작성  => 페이지가 없을 때
        no = request.GET.get( "no", 0 )
        sql =""" 
            DELETE FROM BOARD_TABLE1
            WHERE NO=%s
        """
        cursor.execute( sql, [no] )
        return redirect("/board/list")

# content
# http://127.0.0.1:8000/board/content?no=43
# http://127.0.0.1:8000/board/content => 오류 발생 => no를 못받아서 오류발생
@csrf_exempt
def content(request):
    if request.method == 'GET':
        # 몇번을 눌러서 페이지가 이동한건지 알려준다 => (/board/content?no=글번호)
        # no  = request.GET['no'] # 0은 디폴트값
        no = request.GET.get('no', 0 )
        if no == 0 :
            return redirect( "/board/list" )

        if request.session['hit'] == 1:
            # 조회수 1 증가 시킴    
            sql = """
                UPDATE BOARD_TABLE1 
                SET HIT = HIT+1
                WHERE NO = %s
            """
            cursor.execute( sql, [no] )
            request.session['hit'] = 0 

        # 이전글 번호 가져오기
        sql = """
                SELECT NVL(MAX(NO),0)
                FROM  BOARD_TABLE1
                WHERE NO < %s  
            """
        cursor.execute(sql, [no])
        prev = cursor.fetchone()
            
        # 다음글 번호 가져오기 
        # => prev랑 비교해서 널 값 안에 max()를 min()으로 선언하고 
        # => 쿼리문과 변수명도 수정 
        sql = """
                SELECT NVL(MIN(NO),0)
                FROM  BOARD_TABLE1
                WHERE NO > %s  
            """
        cursor.execute(sql, [no])
        nxt = cursor.fetchone()


        # 가져오기
        sql = """
        SELECT
            NO, TITLE, CONTENT, WRITER,
            HIT,TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI'),IMG
        FROM
            BOARD_TABLE1
        WHERE
            NO = %s
        """
        # 이안에 들어가는 [no] 는 뭐냐 
        cursor.execute( sql, [no] )
        # DB에서 정보를 불러와야 한다.   
        data = cursor.fetchone()
        print(data)# 디비에서 받은 데이터 확인 

        
        # DB에 이미지가 있는 경우 
        if data[6]: 
            img = data[6].read()  # 바이트배열을 이미지에 넣는다 
            img64 = b64encode(img).decode("utf-8")
        # DB에 이미지가 없는 경우
        else:
            # print( os.path.join(BASE_DIR) )
            file = open('./static/img/default.png' , 'rb')
            img = file.read()
            img64 = b64encode(img).decode("utf-8")

        #print(no)
        # 무엇을 출력하는지 확인할것 
        # => 이미지 단계) 위에 선언후 img를 dict에 담아 출력 
        # 추가 )  => 글 번호 전후 출력문  
        return render( request, 'board/content.html', {"one":data, "image":img64 , "prev":prev[0] , "next":nxt[0] } )
    
# list => 2020.01.08 추가
@csrf_exempt
def list_m(request):
    # 네이밍 + 써칭
    page = int(request.GET.get("page",1)) # 정수로 안치면 에러남 
    # "" == None ?  
    txt  = request.GET.get("txt","")
    # 1. 만약에 검색어가 없는 경우 
    
    if txt == "" :
        list = Table1.objects.all()[page*10-10:page*10]
        cnt = Table1.objects.all().count() 
        print(cnt)
        tot = (cnt-1)//10+1
    # 2. 만약 검색어가 존재하는 경우 
    else: # filter() => 뭔지 알아보기 
        # 걸러내서 이름에 맞는 컨텐츠를 불러오기 
        list = Table1.objects.filter(name__contains=txt)[page*10-10:page*10]
        # 불러온 이름에 맞는 컨텐츠의 개수를 센다 
        cnt = Table1.objects.filter(name__contains=txt).count()
        tot = (cnt-1)//10+1
    # 3개를 보내주면 3개를 써야지 
    return render( request, 'board/list_m.html', {"list":list,"txt":txt,"pages":range(1,tot+1,1)})


    # - 네이밍을 했고 
    # - 리스트에서 검색하는거 => 구현 
    # - 만약에 빈거면 페이지 네이션만하고 
    # - 비어있지 않으면 페이지 네이션을 포함해서 진행하는데 
    # - 검색어에 작성한 항목이 있는 아이들만 골라서 출력해야한다. 

    # => html 수정하기 
    
# list => 2020.01.08 추가
@csrf_exempt
def list(request):   
    if request.method == 'GET':
        # 너는 뭘위한 세션이냐 
        request.session['hit'] = 1 # 세션에 hit = 1 
        sql = """
        SELECT
            NO, TITLE, WRITER,
            HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI')
        FROM
            BOARD_TABLE1
        ORDER BY NO DESC
        """
        cursor.execute(sql)

        data = cursor.fetchall()
        print(type(data))
        print(data) #[(),()] => 튜플 

        return render( request, 'board/list.html', {"abc":data})
     
# write
@csrf_exempt
def write(request):
    if request.method == 'GET':
        return render( request, 'board/write.html')
    elif request.method =='POST':
        #img = request.FILES['img']#name값 img
        
        # 'img'는 사용자로부터 입력받은 이미지
        # 담는다 이미지 변수에 사용자 요청을  
        tmp = None
        if 'img' in request.FILES:
            img = request.FILES['img']
            tmp = img.read()

        arr = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer'],
            # 이미지 리드 
            # img.read(),
            tmp
        ]
        try:
            print(arr)
            sql = """
            INSERT INTO BOARD_TABLE1
            (TITLE, CONTENT, WRITER, IMG ,HIT, REGDATE)
            VALUES( %s, %s, %s, %s, 0, SYSDATE )
            """
            cursor.execute( sql, arr )
            
        except Exception as e:
            print(e)

        return redirect( "/board/list" )

