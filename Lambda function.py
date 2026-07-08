"""Lambda function
---------------
------->this is also called as annonymous function.
------->a lambda function can take n number of arguments but having only one expression.
syntax:
lambda agruments:expression

eg:
some=lambda an : an + 5
print(some(10))

some=lambda an,so,how : an + so + how
print(some(10,5,4))

some=lambda an,a : an - 5 + a
print(some(10,3))


filter()
--------

------->the filter() function is a built - in function used to filter elements from an itterablessuch as list,tuple,and set bases on condition.
syntax:
------->this filter() function return filter object so we can convert that into list,set and tuple...

eg:
nums = [1,2,3,4,5]# only mathematical operation will work
rev = filter(lambda a: a%2 ==0,nums)
print(list(rev))

nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 !=0,nums)
print(set(rev))


List comprehension
-----------------
----->this offer a shorter syntax when we want to create a new list from the old

syntax:
variable_name = [expression loop condition]

old_=[1,2,3,4,5,6]
new_=[j for j in old_]
print(new_)

old_=[1,2,3,4,5,6]
new_=[j for j in old_ if j % 3 ==0]
print(new_)

Dictionary comprehension
--------------------
------->this offer a shorter syntax when we want to create a new dict from the old dict

syntax:

variable_name = [expression loop]
eg:
old_dict={1:2,3:4,5:6}#i is keys,j is value
new_dict={i:j for(i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)"""

old_dict={1:2,4:3,5:4}
new_dict={i:j for(i,j) in old_dict.items() if j % 3 == 0}
print(new_dict)
























