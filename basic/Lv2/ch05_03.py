# 데코레이터
import time

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간 
        st = time.perf_counter() 
        result = func(*args)
        # 함수 종료 시간 계산
        et = time.perf_counter() - st 
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수 
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result)) 
        return result 
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func')
print()
none_deco2(100, 150, 250, 300, 350)

print()
print()


# 데코레이터 사용
print('*' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print('*' * 40, 'Called Decorator -> sum_func')
print()
sum_func(100, 150, 250, 300, 350)
print()