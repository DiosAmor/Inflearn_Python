# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대 경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

import sub.sub1.module1
sub.sub1.module1.mod1_test1()

from sub.sub2 import module2 as m2 # Alias
m2.mod2_test2()

from sub.sub1 import * # All
# __init__.py에서 __all__ 에 있는 것 확인함.
module1.mod1_test1()