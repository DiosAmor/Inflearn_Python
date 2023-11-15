# 리스트 주의, 깊은 복사 / 얕은 복사
marks1 = [['~'] * 5 for n in range(5)]
marks2 = [['~'] * 5] * 5

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])


# unpacking 관련
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)


# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print( hash(t1))
# print(hash(t2)) # 예외 immutable

# Dict Setdefault 예제
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k : v for k , v in source}

print(new_dict3)


# 선언 최적화
from dis import dis

print('------')
print(dis('{10}'))

print('------')
print(dis('set([10])'))