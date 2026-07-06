"""
so="lavanya"#ayanval
empty_=""
for j in so:
 empty_=j+empty_
print(empty_)#or print([::-1})not use
if empty_==so:
    print(f"{so} palindrom")
else:
    print(f"{so}is not palindrom")

num=0
num_2=1
limit_=int(input("enter a number:"))
print(num,num_2,end=" ")
for i in range(1,limit_+1):
    all_=num+num_2
    num_2=all_
    print(all_,end=" ")

#calculator
val_=int(input("enter number: "))
val_2=int(input("enter number: "))
user_in=int(input("enter\n1.add \n2.sub \n3.mul \n4.pow: "))
if user_in==1:
 print(val_+val_2)
elif user_in==2:
  print(val_ -val_2)
elif user_in==3:
  print(val_ *val_2)
elif user_in==4:
  print(val_ **val_2)

#tables----
table_= 19
for val in range(1,11):
    print(f"{table_} x {val}={table_*val}")

table_= int(input("enter a number:"))
for val in range(1,11):
    print(f"{table_} x {val}={table_*val}")

#perfect number------
num=int(input("enter a number: "))
sum_=0
for j in range(1,num):
    if num % j==0:
        sum_+=j
if sum_==num:
    print(f"{num} is a perfect num")
else:
    print(f" {num} not a perfect num")"""

































    






























  
    
                  
