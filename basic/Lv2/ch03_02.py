# Special Method (Magic Method)

class Vector(object):
    def __init__(self,*args):
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0,0
        else:
            self._x, self._y = args
    
    def __repr__(self):
        '''
        Return the vector information
        '''
        return 'Vector({}, {})'.format(self._x,self._y)
    
    def __add__(self,other):
        '''
        Return the vector addition of self and other
        '''
        return Vector(self._x+other._x, self._y+other._y)
    
    def __mul__(self,alpha):
        '''
        Return the scalar multiplication of self and alpha
        '''
        return Vector(self._x*alpha, self._y*alpha)
    
    def __bool__(self):
        '''
        Return the vector is (0,0) or not
        '''
        return bool(max(self._x, self._y))
    

# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))

print()
print()

# 참고 : 파이썬 바이트 코드 실행
import dis
dis.dis(v2.__add__)