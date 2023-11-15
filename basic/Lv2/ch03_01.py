# Special Method (Magic Method)

class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {}, {}'.format(self._name, self._price)
    
    # 오버라이딩이 굉장히 쉬운 느낌
    def __add__(self,x):
        print('Called >> __add__')
        return self._price+x._price
    
    def __sub__(self,x):
        print('Called >> __sub__')
        return self._price - x._price
    
    def __le__(self,x):
        print('Called >> __le__')
        return self._price <= x._price
    
    def __ge__(self,x):
        print('Called >> __ge__')
        return self._price >= x._price

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1+s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)