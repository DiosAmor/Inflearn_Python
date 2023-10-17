"""
Chapter 2
Python Advanced(2) - Method Overriding
Keyword - Overriding, OOP, 다형성

"""
"""

메소드 오버라이딩 효과
1. 서브클래스에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용 가능
3. 부모클래스의 메소드 추상화 후 사용 가능(구조적 접근)
4. 확장 가능, 다형성(다양한 방식으로 동작)
5. 가독성 증가, 오류가능성 감소, 메소드 이름 절약, 유지보수성 증가 등

"""

# Ex1
# 기본 Overriding 예제
class ParentEx1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx1(ParentEx1):
    pass

class ChildEx2(ParentEx1):
    def get_value(self):
        return self.value * 10

c1 = ChildEx1()
c2 = ChildEx2()
p1 = ParentEx1()

# 부모클래스 메소드 호출
print('Child1 > ', c1.get_value())

# 자식 메소드 재정의 후 호출
print('Child2 > ', c2.get_value())

# c1 모든 속성 출력
print('Child1 (instance) > ', dir(c1))

# 부모 & 자식 모든 속성 출력
print('Parent 1 (class) > ', dir(ParentEx1))
print('Child 1 (class) > ', dir(ChildEx1))
print('Child 2 (class) > ', dir(ChildEx2))

print()

# 부모 & 자식 인스턴스 속성 출력 (인스턴스 생성될 때 부모에서 가져옴)
print('Parent 1 (instance) > ', ParentEx1.__dict__)
print('Child1 (instance) > ', ChildEx1.__dict__)
print('Child2 (instance) > ', ChildEx2.__dict__)



# Ex2
# Overriding 다형성 예제

import datetime

class Logger(object):
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now(), msg=msg)
        # super().log(message)
        super(TimestampLogger, self).log(message)

class DateLogger(Logger):
    def log(self, msg):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().strftime('%Y-%m-%d'), msg=msg)
        # super().log(message)
        super(DateLogger, self).log(message)

l = Logger()
t = TimestampLogger()
d = DateLogger()

# 메소드 재정의 실습
print('Ex3 > ', l.log('Called logger.'))
print('Ex3 > ', t.log('Called timestamp logger.'))
print('Ex3 > ', d.log('Called date logger.'))