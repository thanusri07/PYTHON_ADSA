'''Inheritance --> one class can inhrit properties of another class
1. Super class/Base class / parent class: properties
2.sub class / derived class / Child class: 
  types:5
     1.single  Inheritance: one child with one parent 
     dia:
        one parent
              |
              |
              one child
ex:
class Parent:   #one parent
    
     2.multilevel  Inheitance:
      dia:
      one grandparent
          |
          |
    one  parent
         |
         |
    one child

     3.mutiple
       dia:
        two or more parent
            |
            |
        one child
     4.Hierarchical
        dia:
           one parent
               |
               |
            one or more child
     5,Hybrid
      
class Parent:
    def display(self):
        print("This is a Parent Class")   #one parent
class child(Parent):
    def display2(self):
        print("This is a Child  class")    #one child
c=child()
c.display2()
c.display()
class Grand:
    def c7(self):
        print("This is a Grand Parent")
class Parent(Grand):
    def sound(self):
        print("This is a parent")
class child(Parent):
    def study(self):
        print("This is a child class")
c1=child()
c1.c7()
c1.sound()
c1.study()

class Parent():
    def Car(self):
        print("This is a parent")
class child1(Parent):
    def study1(self):
        print("This is a 1st child")
class child2(Parent):
    def study2(self):
        print("This is a 2nd child")
a=child1()
b=child2()
a.Car()
a.study1()
b.Car()
b.study2()

class Father:
    def land(self):
        print("Father's land")
class Mother:
    def Car(self):
        print("Mother's Car")
class child(Father, Mother):
    def Property(self):
        print("Child Property")
c=child()
c.land()
c.Car()

class Father:
    def land(self):
        print("Father's land")
class Mother:
    def land(self):
        print("Mother's Car")
class child(Father, Mother):
    def Property(self):
        print("Child Property")
c=child()
c.land()

MRO-->Method Resolution Order  ---> which methods executes first
super() --> accesss parent class method
'''
