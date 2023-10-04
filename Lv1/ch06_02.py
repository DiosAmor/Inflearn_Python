# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y
    
def power(x, y):
    return x ** y
    

# __name__ 사용
# import 하지 않고 해당 파일을 직접 호출했을 때 아래가 실행 됨.
if __name__ == "__main__":
    print("Main!")


# 모듈 사용 실습

import sys

print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('C:/math')

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10, 3))