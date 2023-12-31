# Parallelism with Multiprocessing - Queue

# 프로세스 통신 구현 - Queue

from multiprocessing import Process, Queue, current_process
import time
import os

# 실행 함수
def worker(id,baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    # 계산
    for i in range(baseNum):
        sub_total += 1

    # Produce
    q.put(sub_total)

    # 정보 출력
    print(f"Process ID: {process_id}, Process Name: {process_name} ID: {id}")
    print(f"Result : {sub_total}")

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f"Parent process ID {parent_process_id}")

    # 프로세스 리스트 선언
    processes = list()

    # 시작 시간
    start_time = time.time()

    # Queue
    q = Queue()

    # 프로세스 생성 및 실행
    for i in range(2):
        t = Process(name=str(i),target=worker,args=(i,1000000,q))

        processes.append(t)

        t.start()
    
    for process in processes:
        process.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    # 종료 플레그
    q.put('exit')

    total = 0

    # 대기
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp

    print()

    print("Main-Processing Total_count={}".format(total))
    print("Main-Processing Done!")

if __name__ == '__main__':
    main()