"""
Chapter 1
Python Advanced(1) - Context Manager(1) 
Keyword - Contextlib, __enter__, __exit__, exception

"""
"""
Context manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할

가장 대표적인 with 구문 이해
원하는 시점에 리소스 할당 및 회수
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)

"""

# Ex1

with open('./Lv3/testfile2.txt','w') as f:
    f.write('Context Manager Test2. \nContextlib Test2.')


# Ex2

class MyFileWriter():
    def __init__(self, file_name,method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name,method)

    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj
    
    def __exit__(self,exc_type,value,trace_back):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print(f'Logging exception {(exc_type,value,trace_back)}')
        self.file_obj.close()

with MyFileWriter('./Lv3/testfile3.txt','w') as f:
    f.write('Context Manager Test3.\nContextlib Test3.')

# Ex3
import time

class ExecuteTimer():
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print('{}: {} s'.format(self._msg, time.monotonic() - self._start))
        return True 

with ExecuteTimer("Start! job") as v:
    print('Received start monotonic1 : {}'.format(v))
    # Excute job.
    for i in range(10000000):
        pass
    # raise Exception("Raise! Exception.")


# Ex4
# Use decorator
import contextlib

@contextlib.contextmanager
def my_file_writer(file_name,method):
    f = open(file_name,method)
    yield f     # __enter__
    f.close()   # __exit__

with my_file_writer('./Lv3/testfile4.txt','w') as f:
    f.write('Context Manager Test4. \nContextlib Test4.')

# Ex5
# Use decorator

@contextlib.contextmanager
def ExecuteTimeDc(msg):
    start = time.monotonic()
    try:    # __enter__
        yield start
    except BaseException as e:
        print('Logging exception: {}: {}'.format(msg,e))
        raise
    else:   # __exit__
        print('{}: {} s'.format(msg, time.monotonic() - start))
    
with ExecuteTimeDc("Start! job") as v:
    print('Received start monotonic2 : {}'.format(v))
    #Execute job
    for i in range(10000000):
        pass
    # raise ValueError('occurred.')