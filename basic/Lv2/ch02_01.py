class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # print()로 출력
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 객체 그대로 출력?
        return 'repr : {} - {}'.format(self._company, self._details)
    
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print()

print(car_list)

print()
print()

for x in car_list:
    print(repr(x)) # __repr__
    print(x) # __str__