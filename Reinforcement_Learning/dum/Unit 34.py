
# 34.1 클래스 만들기

# 메서드는 동작 
# 속성은 능력치 

"""
class 클래스이름:
    def method(self): 
        code

"""

class Toy_Step0:
    
    def bear(self):
        print('Hey~')

# IceBear = Toy_Step0()
# IceBear.bear()


"""
# 참고 메서드 안에서 메서드 호출하기 
- 메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 한다. 
- ** self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다. 

"""

class Toy_Step01:

    # def __init__(self):
    #     pass
    
    def bear(self):
        print('Hey~')
    
    def say(self):
        self.bear() # self.메서드() 형식으로 클래스 안의 메서드를 호출 


# IceBear = Toy_Step01()
# IceBear.bear()
# IceBear.say() # bear함수에 있는 프린트를 출력 상속받는 거네!!!

"""
- isinstance는 주로 객체의 자료형을 판단할 때 사용합니다. 
- 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데, 실수와 음의 정수는 계산할 수 없습니다. 
- 이런 경우에 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있습니다.

---

def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)

"""

# 34.2 속성 사용하기
"""
# 속성은 __init__메서드 안에서 self.속성을 할당 -> 속성(attribute)을 만들 때

class 클래스이름:
    def __init__(self):
        self.속성 = 값

"""

class Toy_Step02():

    def __init__(self):
        self.say = 'Hello~'

    def bear(self):
        print(self.say)

IceBear = Toy_Step02()
IceBear.bear()  # Hello~


"""
__init__ 메서드는 IceBear = Toy_Step02()처럼 클래스에 ( )(괄호)를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드입니다. 
즉, __init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화합니다.

특히, 이렇게 앞 뒤로__(밑줄 두 개)가 붙은 메서드는 파이선이 자동으로 호출 해주는 메서드인데 스페셜 메서드special method) 또는 매직 메서드(magic method)


class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2

"""


class Person():

    def __init__(self, name, age, address):

        self.say = 'Hello~'
        self.name = name
        self.age = age
        self.address = address


    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.say, self.name))

IceBear = Person('아이스베어', 10, '샌프란시스코') # 인자 : (self), name, age, address
IceBear.greeting()


