# api/views.py

from django.shortcuts import render
# 파일 응답 
from django.http import HttpResponse
# 모델 호출 
from .models import Item
# select1
from .serializers import ItemSerializer
from rest_framework.renderers import JSONRenderer
import json


#  변수 




# Create your views here.



# 키를 변수에 담음 
KEYs = "ggg" 

# select4
def select4(request):
    key     = request.GET.get("key","")
    num     = int(request.GET.get("num", 1 )) 
    search  = str(request.GET.get("search", ""))

    # DB에서 확인 
    if key == KEYs :
        #obj = Item.objects.get(no=no)
        # 전부
        #obj = Item.objects.all()
        # 필터링 
        obj = Item.objects.filter( name__contains=search )[0:num]
        serializer = ItemSerializer( obj, many=True )
        print(serializer.data)
        data = JSONRenderer().render(serializer.data)

        return HttpResponse(data)
    else :
        data = json.dumps({"ret":'key error'})
        return HttpResponse( data )

# select2처럼 에러 코드를 변수에 담으니까 



# select3
def select3(request):
    if request.method == "GET":
        # 키값 선언 
        key    = request.GET.get('key', '')
        # 검색 선언 
        search = request.GET.get('search','')
        # 카운트 선언
        num    = int(request.GET.get('num', 1))
        
        # 만약 키가 KEYs = "abc"면   => 위에 키를 변수에 담음 
        if key == KEYs :
            # obj라는 변수안에 모델의 객체중 네임의 컨테이너를 필터링한다. 
            # => 그컨테이너들은 검색과 같아야한다. => 일부만 보여 주겠다.
            # 범위를 정해서 보여주는 동작을 해야한다. 그러려면 => slicing을 사용 
            # 카운드를 사용할수 없는 이유는 count = len() 즉, 길이 값만 보여주기 때문에 적절하지 않다.  
            obj = Item.objects.filter(name__contains=str(search))[0:num]
                # SELECT*FROM API_MEMBER 
                # WHERE ID LIKE  "%%'''+str(search)+'''%%" ORDER BY NO DESC
            # json 생성     
            serializer = ItemSerializer(obj, many=True)
            data = JSONRenderer().render(serializer.data)
            # 데이터를 출력 => 웹상에 뿌린다. 
            return HttpResponse(data)
        else:
            # 만약 키가 "abc" 가 아니면  => "ret":"key error"를 화면에 출력한다. 
            data = json.dumps({"ret":"key error"})
            return HttpResponse(data)



# select2 {"id":"a"} => 물품이 한개 
def select2(request):
    key = request.GET.get("key","")
    no = request.GET.get("no","1")
    # DB에서 확인 

    data = json.dumps({"ret":'key error'})
    if key == 'abc':
        obj = Item.objects.get(no=no)
        serializer = ItemSerializer(obj)
        print(serializer.data)
        data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(data)
    


# select1 [{"id":"a"},{"id":"b"}] => 물품이 여러개 
def select1(request):
    obj = Item.objects.all()
    serializer = ItemSerializer(obj, many=True)
    data = JSONRenderer().render(serializer.data)

    return HttpResponse(data)



##############################################
# 출력 => http://127.0.0.1:8000/api/select1?key=abc&no=1
# 출력되게 만들자 => http://127.0.0.1:8000/api/select3?key=abc&num=10&search=과
# num   => 갯수 
# search 
################################################



# insert1
def insert1(request):
    # for i in range(1, 31, 1):
    #     obj = Item()
    #     obj.name = '커피' + str(i)
    #     obj.price = 1500 + i 
    #     obj.save()

    return HttpResponse("insert1")



