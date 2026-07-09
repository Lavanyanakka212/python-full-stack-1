"""nums=[23,4,6,23,7,4]
empty_=[]
def removes_(nums,empty):
    for j in nums:
        if j not in empty_:
            empty_.append(j)
            print(empty_)
removes_(nums,empty_)


prime_=7
count=0
def prime_not(prime_,count):
    for i in range(1,prime_+1):
        if prime % j == 0:
            count+=1
            if count==2:
                print(f'(prime_) is a prime')
            else:
                print(f'(prime_)is not prime')
        
prime_not(prime_,count)

some="python is a programming language"
count=0
def counting(some,count):
 so=some.split(' ')
 for j in so:
     count += 1
     print(count)
counting(some,count)"""

some="Python is a proGraMming LanGuagE"
cap_count = 0
small_count = 0
space_count = 0
def cap_small(some,cap_count,small_count,space_count):
    for j in some:
        if j.isupper():
           cap_count += 1
       elif j.islower():,
           small_count += 1
        else:
           space_count += 1
    print(f'there total {cap_count} number cap')
    print(f'there total {small_count} number small')
    print(f'there total {space_count} number space')
cap_small(some,cap_count,small_count,space_count)
        
        

        






