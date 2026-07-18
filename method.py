"""l.method overloading:
--->method overloading means having multiple methods with the same name but different parameter.
ex:
class cal:
    def add(self,num,num_2=0):
        print(num + num_2)
        
    def add(self,num,num_2,num_3=0):
        print(num + num_2 + num_3)
        
    def add(self,num,num_2,num_3=0,num_4=0):
        print(num + num_2 + num_3 + num_4)

        
obj = cal() 
obj.add(34,45)
obj.add(23,46,91)
obj.add(1,2,3,4)

2.method overridding:
----->the method overriding occurs when a child class provides its own implements of a method already defined in its parents class..
ex:
class  animals:
    def sound(self):
        print("animals make sounds")
class dog(animals):
    def sound(self):
        print("dogs barks")
d=dog()
d.sound()

3.operation overloading:
-------->this allows operators(+,-,*) to work differently for user-defined object.

1.__add__(+)#built-in
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5.__eq__(==)
6.__it__(<)

ex:
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):#here inside operation will work,add means we can write +
        return self.marks + other.marks
s1 = student(56)
s2 = student(67)
print(s1 + s2)


DATA ABSTRACTION:#HIDDEN
----------------
--->data abstraction is the process of hiding implements datails and showing only the essential data to the user.

ex:
---ATM
---CAR
---APP

syntax:
from abc import ABC,abstractmethod
class parent:
    @absractmethod
    def display(self):
        pass

ex:"""
from abc import ABC,abstractmethod

class bank:
    
    def interest(self):
        raise NotImplementedError('subclass must implement interest()')
    
class SBI(bank):
    def interest(self):
        print('SBI interest Rate:5.5%')
        
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate:5.5%')
        
class ICIC(bank):
    def interest(self):
        print('ICIC interest Rate:6.9%')
        
banks = [SBI(),HDFC(),ICIC()]
for j in banks:
    j.interest()















