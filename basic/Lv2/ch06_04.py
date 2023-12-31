# Futures 동시성
# 비동기 작업 실행
# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중이 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 파이썬 특징
# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#       GIL (Global Interface Lock) 실행 , 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)

# GIL 우회하려면: 멀티프로세싱 사용, CPython


# concurrent.futures map

import os
import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 1000000]

# 동시성 합계 계산 메인함수
# 누적 합계 함수(제네레이터)

def sum_generator(n):
    return sum(n for n in range(1,n+1))

def main():
    # worker count
    worker = min(10,len(WORK_LIST))
    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    # futures.ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as excutor:
        result = excutor.map(sum_generator,WORK_LIST)

    # 종료 시간
    end_tm = time.time()-start_tm

    msg = '\n Result -> {} Time : {:.2f}s'
    print(msg.format(list(result),end_tm))

# 실행
if __name__ == '__main__':
    main()
