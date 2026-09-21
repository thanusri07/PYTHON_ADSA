'''
polymorphism:

poly-->Many
Morphism-->Forms

same method name with different Behaviours
'''
#Method overriding:same method name with different Arguments
'''
class Animal:
    def sound(self):
        print("Animal makes sound")
class Cat:
    def sound(self):
        print("Cat makes sound")
class Dog:
    def sound(self):
        print("Dog makes sound")
c=Cat()
d=Dog()
c.sound()
d.sound()
a=[Cat(),Dog()]
for obj in a:
    obj.sound()
'''
#method loading:same method name with different arguments
'''
class Cal:
    def add(self,a,b,c=0):
        print(a+b+c)
obj1=add(10,20)
obj2=add(10,20,30)
'''
#Duck Typing: If it iss required to access the object's method then python allow you to use it, without its type
'''
class Dog:
    def  sound(self):
        print("Bow-Bow")
class Cat:
    def sound(self):
        print("Meow-Meow)
def make_sound(animal):
    animal.sound()
make_sound(Dog())
make_sound(Cat())
'''

#Inheritance in polymorphism:
class Vehicle:
    def horn(self):
        print("Vehicle gives sound")
class Car(Vehicle):
    def horn(self):
        print("Car gives sound")
class Bike(Vehicle):
    def horn(self):
        print("Bikes gives sound")
        super().horn() #Access the parent class method
for obj in [Car(),Bike()]:
    obj.horn()
