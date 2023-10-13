# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행

# Generator Ex1
def generator_ex1():
    print('Start')
    yield 'A Point.'
    print('continue')
    yield 'B Point.'
    print('End')

temp = iter(generator_ex1())

print(next(temp))
print(next(temp))
print(next(temp))
