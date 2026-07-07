"""#Passing by value:
def some(a):#calling func
    for j in a:
        print(j)
some(["python","is"])
some([1,2,3])

def some(a):#calling func
    for j in a:
        print(j)
some(a)#refences

return keyword
--------------
------>in a function if a return is executed then it will exit from the function with certain returned values.
def myfunc_():
    return 5+b#hold the value
a=myfunc_(10)
c=myfunc_(20)
print(a)#display purpose

import builtins


builtin_functions=[
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"total built-in functions are {len(builtin_functions)}")

Recursive function
-------------------
------>recrusive function that calls itself repeatedly until a specified.
syntax:
def fun_name(parameter):
    if condition:base case
        return statements
    else
        return statements
print(func_name(argumrnts))

eg:"""(factorial form)
def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num-1)
num=5
print(func_name(num))

    




































