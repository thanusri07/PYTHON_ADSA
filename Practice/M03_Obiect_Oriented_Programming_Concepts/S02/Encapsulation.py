'''
oop-->4 types
1.Encapsulation : Bundling of data and methods.Ex: Tablet
Implementantion:
Access modifiers : Access variables
1.Public--> any one can access these var in entire code
2. Private --> only accessible within the same class
3.Protected -->(_)It can access  in a class from another class / accessible within the same class and its subclasses
class A:
    name="Thanu"    #public
    _name="anu"     #protected
    __name="manu"   #private
a=A()
print(a.name)
print(a._name)
print(a._A__name)
'''
# write a proram for BankAccount to check balance amount after adding 500 to my acc(1000)
'''
ATM-->Machine-->(Accountnumb, balance)
Hide --> Bank Data DB-> Methods(deposit(), withdraw(), checkbalance())
'''
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0:
             self.__balance += amount
    def display(self):
        return self.__balance
b=BankAccount(1000)
b.deposit(500)
print(b.display())