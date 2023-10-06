class Car():
    """
    Car Class
    Author : Lee
    Data : 2023.10.06
    """

    # 클래스 변수 (클래스 공유)
    car_count = 0

    # 인스턴스 변수는 보통 _를 붙여서 구분.
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self): # print()로 출력
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 객체 그대로 출력?
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1
    
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 실행
car1.detail_info()
car2.detail_info()
Car.detail_info(car1)
Car.detail_info(car2)

# 에러
# Car.detail_info()
