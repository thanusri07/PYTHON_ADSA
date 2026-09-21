'''
OOPS--> Object Oriented Programming System

class --> A class is a blueprint/ Template for creating objects. 
      --> It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.
object --> An object is an instance of a class. It is a real-world entity that has state and behavior.


Example:

class C7:         #class creation
    pass
a = C7()#object creation  
b=C7()#object creation
c=C7()#object creation
# a is an object of class C7
Note: In Python, we can create multiple objects of a class. Each object will have its own state and behavior.

'''
'''
class Student:
    pass
s1 = Student()  # object creation
s2 = Student()  # object creation
s1.name="Thanu"
s1.rollno=100
s2.name="Priya"
s2.rollno=101
print(s1.name)
print(s1.rollno)
print(s2.name)
print(s2.rollno)

# what is the purpose of OOPs Concepts?
1.Code Reusability
2.Security
3.Easy to maintain

#Types of Variables in Pyth
3 types
1.Instance Variable---> Variables(inside the class)
2.Class Variable---> Variables(inside the class) but outside the methods
3.Static Variable--->Variables(inside the methods)

'''
class Student:
    x="Bhaskar"                 #class variable
    def display(name):
        name="C7"            #local variable
        print(name)
s1=Student()
s1.name="Thanu"              #instance variable
print(s1.name)
print(s1.x)
s1.display()