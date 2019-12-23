import test6

# 예외처리 
    # form 
    # try:
    #     pass
    # except expression as identifier:
    #     pass
    # else:
    #     pass
    # finally:
    #     pass

# 코드는 잠재적으로 오류를 가질 수 있다. 
# 이때, s/w를 다운되지 않게하고 , 혹은 그정보를 수집하고,
# 문제없이 다음단계로 진행시키게 하는 방법 

# case 01 : 예외 발생시 코드 진행 확인
    # print(0)
    # try:
    #     print(1)
    #     # 가장 간단한 예외사항 
    #     print(1/0)
    #     print(2)
    # # 모든 예외의 시작점 : 근본 
    # except Exception as e:
    #     print(3)
    # else:
    #     print(4)
    # finally:
    #     print(5)
    # print(6)



# case 01 - 1 : 예외 발생시 코드 진행 확인
    # print(0)
    # try: # 예외가 발생 할 만한 코드를 감싼다. 
    #     print(1)
    #     # 가장 간단한 예외사항 
    #     print(1/0)
    #     print(2)
    # # 모든 예외의 시작점 : 근본 
    # except Exception as e: # 예외가 발생하면 호출 
    #     print(3,e)
    # else: # 예외없이 정상적으로 코드가 진행되면 호출 
    #     print(4)
    # finally: # 무조건 수행 
    #     print(5)
    # print(6)




# case 02 : 
print(0)
try: # 예외가 발생 할 만한 코드를 감싼다. 
    print(1)
    # 가장 간단한 예외사항 
    #print(1/0)
    print(2)
# 모든 예외의 시작점 : 근본 
except Exception as e: # 예외가 발생하면 호출 
    print(3,e)
else: # 예외없이 정상적으로 코드가 진행되면 호출 
    print(4)
finally: # 무조건 수행 
    print(5)
print(6)s