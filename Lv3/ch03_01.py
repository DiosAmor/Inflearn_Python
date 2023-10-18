"""
Chapter 3
Python Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class

"""
"""

메타클래스
1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스 커스텀
2. 프레임워크 작성 시 필수
3. 동적 생성(type함수), 커스텀 생성(type상속)
4. 커스텀 클래스 -> 검증 클래스 등
5. 엄격한 Class 사용 요구, 메소드 오버라이드 요구

"""

# Ex1
# type 예제

class SampleA(): # Class == Object
    pass

obj1 = SampleA() # 변수에 할당, 복사 가능, 새로운 속성, 함수의 인자로 넘기기 가능

# type을 이용하면 동적으로 만들어낼 수 있다.
# obj1 -> SampleA instance
# SampleA -> type meta class (type 클래스로부터 만들어짐)
# type -> type meta class (type은 본인)
print('Ex1 > ', obj1.__class__)
print('Ex1 > ', type(obj1))
print('Ex1 > ', obj1.__class__ is type(obj1))

print()

# Ex2
# type meta (Ex1 증명)

# int, dict 선언
n = 10
d = { 'a' : 10, 'b' : 20 }

class SampleB:
    pass

obj2 = SampleB()

for o in (n, d, obj2):
    print('Ex2 >  {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))


print()

# the type of any new-style class is type.
print(type(SampleB))
print(type(obj2))

print()

for t in int, float, dict, list, tuple:
    print('Ex2 > ', type(t))

print('Ex2 > ', type(type))