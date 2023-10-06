# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

class Car():
    """
    Car Class
    Author : Lee
    Data : 2023.10.06
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 (클래스 공유)
    car_count = 0
    price_per_raise = 1.0

    # 인스턴스 변수는 보통 _를 붙여서 구분.
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self): # print()로 출력
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 객체 그대로 출력?
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def __del__(self):
        Car.car_count -= 1

    # Instance Method
    # self : 객체의 고유한 속성 값 사용

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # Class Method @classmethod, cls
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}.'.format(inst._company)
        print('Sorry. This car is not Bmw.')


car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})


# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.2

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
print()

# 가격 정보(인상 후 : 클래스메소드)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# Bmw 여부(스테이틱 메소드 사용)
print('Static : ', Car.is_bmw(car1))
print('Static : ', Car.is_bmw(car2))
print()

print('Static : ', car1.is_bmw(car1))
print('Static : ', car2.is_bmw(car2))