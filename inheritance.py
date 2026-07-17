"""inheritance
----------------------
----> inheritance it an oop concept where one class (child/dervied)acquird the properties and methods

class parents:
    pass
class child(parents):
    pass

1.single inheritance
------------------------
--->a child class inherits  from parents is single inheritance.

ex:
class animal:
    def sound(self):
        print('animal make sounds')
class dog(animal):
    def barks(self):
        print('dog barks')
d=dog()
d.sound()
d.barks()

ex:
class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        print('3bhk flat')
s=son()
s.land()
s.flat()

2.multiple inheritance
-------------------------
------>a child class inheritance more than one parents is called
ex:
class father:
    def skills(self):
        print('driving')
class mother:
    def talents(self):
        print('cooking')
class daughter(father,mother):
    def me(self):
        print('coding')
all = daughter()
all.skills()
all.talents()
all.me()

3. multi-level inheritance
------------------------
----->one child class become the parents for another class
ex:
class grandfather:
    def house(self):
        print('own house')
class father(grandfather):
    def flat(self):
        print('new 3bhk')
class daughter(father):
    def car(self):
        print('i have a car')
fam = daughter()
fam.house()
fam.flat()
fam.car()

4.hierachial inheritance:
-----------------
---->multiple childs inheritance from the same parents
ex:
class mother:
    def gold(self):
        print('10 kg of gold')
class pinky(mother):
    def show(self):
        print('will u get 5 kg only')
class lavi(mother):
    def show_2(self):
        print('remaining 5 kg gold')
child_1 = pinky()
child_2 = lavi()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()
ex:
class father:
    def land(self):
        print('15 arc of land')
class pinky(father):
    def show(self):
        print('5 arc of land')
class lavi(father):
    def show_2(self):
        print('5 arc of land')
class pandu(father):
    def show_3(self):
        print('5 arc of land')


        
child_1 = pinky()
child_2 = lavi()
child_3 = pandu()

child_1.land()
child_1.show()

child_2.land()
child_2.show_2()

child_3.land()
child_3.show_3()

5.hybrid inheritance
---------------------------
---->this is the combination of to or more types of inheritance
ex:multi+multi-level

ex:
class A:
    def methodA(self):
        print('class A')
class B(A):
    def methodB(self):
        print('class B')
class C(A):
    def methodC(self):
        print('class C')
class D(B,C):
    def methodD(self):
        print('class D')
so = D()
so.methodA()
so.methodB()
so.methodC()
so.methodD()

super() method\constructor
----------------
---->this super() function is used to access the parents class  methods or constructor in the child class. 

ex:
class parents:
    def show(self):#this is method program
        print('parents method')
class child(parents):
    def show(self):
        super().show()
        print('child class')
chi_ = child()
chi_.show()

ex:"""
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll


    def display(self):
        print(self.name)
        print(self.roll)
an = student('lavi',25)
an.display()

        































    
