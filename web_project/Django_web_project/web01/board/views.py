# board/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 
from django.shortcuts import render
from django.shortcuts import redirect
# HttpResponse : 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse
# URL의 변화여부가 필요하다면 Redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from base64 import b64encode
import pandas as pd
# byte 배열을 base64(이미지를 출력해주는 포멧)로 변경 
import os
# 렌더(render) 
# index에서 인자값으로 request을 받았어 
# 받았으니까 돌려줘야해 그때 render로 뭔가를 돌려주는데 
# 그게 html 페이지(위치값이랑 확장자명 빼먹지 말기 ) !!! 

# 변수
cursor = connection.cursor() #sql문 수행위한 cursor객체

# Create your views here.
# 함수형태로 생성, 기호에 따라 클래스로도 생성 가능 
# 뷰의 함수는 먼저 쓴 것을 아래로 마지막에 작성한것은 위로 가도록 작성하자 


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

