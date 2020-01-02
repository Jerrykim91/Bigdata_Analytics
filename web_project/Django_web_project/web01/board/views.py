# board/views.py
# import => 임포트 하기전에 뭐가 구성될지 생각해보자 
from django.shortcuts import render
# HttpResponse : 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse
# URL의 변화여부가 필요하다면 Redirect

# 렌더(render) 
 # index에서 인자값으로 request을 받았어 
# 받았으니까 돌려줘야해 그때 render로 뭔가를 돌려주는데 
# #그게 html 페이지(위치값이랑 확장자명 빼먹지 말기 ) !!! 


# Create your views here.
# 함수형태로 생성, 기호에 따라 클래스로도 생성 가능  


# index 
def index(request):
    return HttpResponse(" 열었다 ")
    # index에서 인자값으로 request을 받았어 
    # 받았으니까 돌려줘야해 그때 렌더로 뭔가를돌려주는데 그게 html페이지 !!! 
    #return render(request,'board/index.html')

