# 클로저
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근 (액세스) 기능

def closure_ex1():
    # Free variable
    series = []
    # Closure
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series,len(series)))
        return sum(series)/len(series)
    return averager

avg_closure1 = closure_ex1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print()
print()


# Nonlocal -> Free variable, list는 문제 없지만 (mutable) immutable 변수는 아니다.
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

print()
print()