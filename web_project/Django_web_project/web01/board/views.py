# board/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 
from django.shortcuts import render
from django.shortcuts import redirect
# HttpResponse : 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse
# URL의 변화여부가 필요하다면 Redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


# 렌더(render) 
# index에서 인자값으로 request을 받았어 
# 받았으니까 돌려줘야해 그때 render로 뭔가를 돌려주는데 
# 그게 html 페이지(위치값이랑 확장자명 빼먹지 말기 ) !!! 

cursor = connection.cursor() #sql문 수행위한 cursor객체

# Create your views here.
# 함수형태로 생성, 기호에 따라 클래스로도 생성 가능 
# 뷰의 함수는 먼저 쓴 것을 아래로 마지막에 작성한것은 위로 가도록 작성하자 




# content
# http://127.0.0.1:8000/board/content?no=43
# http://127.0.0.1:8000/board/content => 오류 발생 => no를 못받아서 오류발생
@csrf_exempt
def content(request):
    if request.method == 'GET':
        # 몇번을 눌러서 페이지가 이동한건지 알려준다  => (/board/content?no=글번호)
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
        # 가져오기
        sql = """
        SELECT
            NO, TITLE, CONTENT, WRITER, 
            HIT,TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI')
        FROM
            BOARD_TABLE1
        WHERE
            NO = %s
        """
        cursor.execute( sql, [no] )
        data = cursor.fetchone()

        # DB에서 정보를 불러와야 한다.     
        print(no)
        # 무엇을 출력하는지 확인할것
        return render( request, 'board/content.html', {"one":data} )
    

# list
@csrf_exempt
def list(request):
    if request.method == 'GET':
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
        print(data) #[(),()]

        return render( request, 'board/list.html', {"abc":data} )
     

@csrf_exempt
def write(request):
    if request.method == 'GET':
        return render( request, 'board/write.html')
    elif request.method =='POST':
        img = request.FILES['img']#name값 img
        arr = [
            request.POST['title'],
            request.POST['content'],
            request.POST['writer'],
            # 이미지 리드 
            img.read()
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

