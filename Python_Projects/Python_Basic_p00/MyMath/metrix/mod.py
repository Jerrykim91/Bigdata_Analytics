# 노출 할 코드만 
# 모듈 내부에는 변수, 함수, 클래스등이 여러개 존재 할 수 있다. 

# 변수
PI = 3.14
name = '17시 30분'

# 함수 
def add(a,b):
    return a + b

# 클래스
class A():
    def __init__(self):
        print('생성')
        
#  => 의도 하지 않은 코드가 작동 되는것을 방지 
# 은닉
if __name__ == '__main__':      
    # 테스트 
    print('본모듈의 개발자가 직접 구동시 작동 ')
    print(add(1,2))
    A()
    
else : 
    # 제 3자가 이모듈을 가져다가 사용할때 
    # __name__ => 파일명 => mod 
    # 'mod'== '__main__' => False가 되니 else 코드를 타게 된다. 
    # 선택적으로 카고 가게끔 코드를 작성 
    pass 