# 코루틴(Coroutine)

# ex1
def coroutine1():
    print('>>> coroutine stated.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 제너레이터 선언
cr1 = coroutine1()

print(cr1,type(cr1))
next(cr1)
cr1.send(100)

# ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

print(cr3.send(15))
