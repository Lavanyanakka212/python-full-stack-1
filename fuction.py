"""function----->
--->function is a block of code that can be reusable
----> function can aviod the repeated line of code.......

function are two types
----------->
1. built-in

eg:print(),max(),min(),sum()

2.user-define

------>this function starts with a keyword (def)

def func_name(parameters):
    ----------
    -----------
    ----------
func_name(arguments)

eg:

    
def add():
 print("hello!")
add()

types of arguments----
------------>
1.requared argument

------>we have to pass number arguments with defination of the function
    
def add(a,b):# we should use like this
 print(a)
add(2)

2.default
3.keyword
--------->we can pass as a pair like (variable=datatypes)
def add(a,b):
 print(a+b)
add(a=2,b=3)

def add(a,b):
 print(a+b)
add(b=2,a=3)

num=7
num_2=8
num_3=9
def add(a,b,c):
 print(a)
  print(b)
   print(c)
add(num,num_2,num_3)


4.variable length
------->can pass n number agruments and just use (*args) in the parameter,will receive tuple of arguments
                                                (**args)asterisk dictinory..
eg:
num=7
num_2=8
num_3=9
def add(*a):
 print(a)# or we can write print(a[0])
add(num,num_2,num_3)

def all_(**any):
    print(any['age'])
all_(name="lavanya",age=23)"""

eg:
num=9#global variable can be use through out the program..
def func_():
    print(num)
func_()

#local variable can't access out side the func_..
def func_():
    num=9
    print(num)
func_()
print(num)


num=9  
def func_():
    global num#to replace the  global by using keyword(global) that can changed complted inside,outsibe of the function
    num=89
    print(num)
func_()
print(num)
  


























