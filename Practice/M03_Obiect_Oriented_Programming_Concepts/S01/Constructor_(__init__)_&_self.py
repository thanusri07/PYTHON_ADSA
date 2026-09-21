'''
__init__():It is a special kind of method
self --> Represent the Current Object
class Empl:
    def __int__():
        pass
emp=Empl()
emp1=__init__()#wrong

class Student:
    def display(self):

s1.Student()
s2.Student() 

def add(a,b):
    return a+b
res=add(10,20)
print(res)

class Add:
    def add(self,a,b):
        return a+b
res1=Add()
print(res1.add(10,20))
res2=Add()
print(res2.add(30,40))
'''
# write a simple program to find the area and primeter of a circle
class Circle:
    def display(self,radius):
        self.radius=radius
    def area(self,radius):
        res=(3.14*self.radius*self.radius)
        print(res)
    def perimeter(self,radius):
        res=(2*3.14*self.radius)
        print(res)
c=Circle()
c.display(5)
c.area(5)
c.perimeter(5)

#leet code:1603
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        '''
        self.big = big
        self.medium = medium
        self.small = small
        '''
        self.spaces=[0,big,medium,small]
    def addCar(self, carType: int) -> bool:
        if self.spaces[carType]>=1:
            self.spaces[carType]-=1
            return True
        return False
        '''
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
        else:
            return False
        '''
        



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)