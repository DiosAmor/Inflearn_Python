# Parallelism with Multiprocessing - Pipe

# 프로세스 통신 구현 - Pipe
# 자식 부모간의 1대1인 경우가 많다.

from multiprocessing import Process, Pipe, current_process
import time
import os

# 실행 함수
def worker(id,baseNum, pipe):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    # 계산
    for i in range(baseNum):
        sub_total += 1

    # Produce
    pipe.send(sub_total)
    pipe.close()

    # 정보 출력
    print(f"Process ID: {process_id}, Process Name: {process_name} ID: {id}")
    print(f"Result : {sub_total}")

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"Parent process ID {parent_process_id}")

    # Pipe 선언
    parent_pipe, child_pipe = Pipe()

    # 시작 시간
    start_time = time.time()

    # 프로세스 생성 및 실행
    t = Process(target=worker,args=(1,1000000,child_pipe))
    t.start()
    t.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    print()
    print("Main-Processing Total_count={}".format(parent_pipe.recv()))
    print("Main-Processing Done!")

if __name__ == '__main__':
    main()