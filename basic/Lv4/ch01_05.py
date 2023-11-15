# Thread - ThreadPoolExecutor
"""

그룹스레드
(1).Python 3.2 이상 표준 라이브러리 사용
(2).concurrent.futures
(3).with사용으로 생성, 소멸 라이프사이클 관리 용이
(4).디버깅하기가 난해함(단점)
(5).대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화(캡슐화)

"""

import logging
from concurrent.futures import ThreadPoolExecutor

def task(name):
    logging.info("Sub-Thread %s: starting", name)

    result = 0
    for i in range(10001):
        result = result + i

    logging.info("Sub-Thread %s: finishing result: %d", name, result)

def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before creating thread")

    # with context 구문 사용
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['First', 'Second'])
        
        # 결과 확인
        # print(list(tasks))

    logging.info("Main-Thread : all done")

if __name__ == "__main__":
    main()