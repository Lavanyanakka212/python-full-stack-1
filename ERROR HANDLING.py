------------ERROR HANDLING:------------
------------------
syntax:
fo j in range(1,10:
    print(j)

o/p:---------- syntax Error
              
ex:
             
fo j in range(1,10):
    print(j)



----------indentataion error-------------
--------------------
ex:

    a=20
for j in range(a):
    print(j)
else:
print()

o/p:-----------IndentataionError

---------value error------------
------------------
num = int(input("enter a num:"))

o/p:--------ValueERROR


Try:
----------->the try block will test tje code for error
syntax:-----try:

except:
----------this except let us handle the errors in the code.
syntax:------except:

else:
---------->if the try block does not have any error than the else block will excute.
ex:

try:
    num = int(input("enter a num:"))
    num_2 = int(input("enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision error')
except ValueError:
    print('will get value error')

else:
    print('no error')

finally:
---------->the finally block will execute either code contain error or not.

try:
    num = int(input("enter a num:"))
    num_2 = int(input("enter a num:"))
    print(num / num_2)
except ZeroDivisionError:
    print('will get Zerodivision error')
except ValueError:
    print('will get value error')

else:
    print('no error')

finally:
    print('end')

ex:
try:
    print(num)
except:
    print('will get name error')

try:
    num = int(input("enter a num:"))
except NameError:
    print('will get name error')


try:
    num = int(input("enter a num:"))
except ValueError:
    print('will get name error')












    
    
    

              


