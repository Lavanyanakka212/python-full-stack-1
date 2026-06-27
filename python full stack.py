
"""
procedural language: this follow a step by step approach where code is structure into procedural such as function or routines.
eg:c lang.
oop's
python -----> is a popular programing language.and it is easy to use.

Guido van Rossum, and released in 1991.

eg:
1.interputer:line-by line processs.

tokens:
1.keywords--->there are reserved word in python.
eg:if,else,for,while.
2.identifier---->name give to variables,funnction,class
3.literals--->89,"hello",4.56
4.operator---->+,-,*,/,%.
5.punctuators----->{},(),[].

rules of variables:
A-Z,a-z,__
      eg:num_1=7
           num=8
            num_2=9
special character,number,space
$num=0
su@m=0
su am=0

comments:1.single line---># eg:#hello 
                  2.multi line---->''' ''',""" """.eg:'''juijioiorsswftsftftftaftrtrtfctstsftftfxtyyuiui'''

eg:num=9
if num%2==0: #checking a number is even or odd
print("even")
else:
print("odd")

boolean----->1.true
                        2.false 
eg:num=8
num_2=89
print((num))
print((num_2))

operator:

1.Arithmatic operator-->+, _, %, /, **//. for mathematical operation.
    eg:a=2                         a=2                   a=2                  a=2                  a=2                   a=2
         b=5                           b=5                 b=5                  b=5                  b=3                   b=3
          print(a ** b)             print(a+b)       print(a-b)        print(a/b)        print(a%b)         print(a//b)

2.Assignment  "-->=,+= increase,-= dec,*=,%=,=.
              eg:a=20                    a=20
                    a += 4                 a-=4
                    print(a)                 print(a)

3.comparision  "-->==, !=, <=, >==.
           eg:a=20                               eg:a=20                                        a=20               a=20
                 b=7                                     b=7                                          b=7                  b=7
                print(a==b)(false)              print(a!=b)(true)                    print(a>=b)      print(a<=b)
                
4.logical-->
eg:end-->return true if both true(&)
               a=20
                b=7
                 c=89
                print(a>=b end b>=c)


    or----->return true if any one is correct
                     a=20
                      b=7
                       c=89
                       print(a>=b or b>=c)

    not----->reverse the output
                     a=20
                     b=7
                     c=89
                      print(a>=b not b>=c)

5.identify       "-->is---> same object or not
a=20
b=20
print(a==b)
print(a is b)

is not------>
   a=20
    b=20
    print(a==b)
    print(a is not b)

6.membership  "-->in-----> Returns True if the value is present.

not in → Returns True if the value is not present.
                                 eg:a=[1,2,3,4,5]                      
                                        print(20 in a)
                      
                                 not in--->Returns True if the value is not present.
                                        eg:a=[1,2,3,4,5]
                                              print(20 not in a)

7.bitwise --> &, <<, >>, |, ^.

print(5&4)
print(5|4)
print(5<<4)
print(5>>4)

"""

                                          datatype:

int---->num=8(num is variable)

float------>num_2=7.89(numeric datatype)

string------->string is squence of char that enclosed in   "python",'',"",""" """.string is immutable
eg:"python"

concatination----------->her the(+)opertor act as to concatinate more than 2 strings..
so="python"
any_="is a language"
print(so+any_)
                       
index------------->this is used to access the particular char in the string by pass index positionvalue.
                   >index start from 0
                   >we have negative indexing to count position from last to first
so="python is a language".
print(so[12])
print(so[-2])


                methods:1.replace()----->this method is use to change any sudstring in that particular string.
                                       syntax----->variable_name.replace("old string","new string",count)

                                         eg:so="python  is a language"
                                                print(so.replace("python","java")
                                                print(so)
                                        eg:"python is a language"
                                        print(so.replace("a","A",2)

                                       
                        2.join()------>this method used to add new sub string after each char in the string.
                                              syntax------->"string".join(variable_name)

                                              eg:so="python is a language"
                                              print("-",.join(so))
                                              print("$",.join(so))
                        3.split()-------->this method can divide the string into different index into list,based on the string pass by us..

                                              syntax---->variable_name.split('substring')
                                              eg:so="python is a language"
                                              print(so.split("is"))
                        4.count()-------->used to count the substring in the particular string and also specify the index position.
                                              syntax:variable name.count("substring",start index,ending index)
                                        
                                              eg:so="python is a language"
                                              print(so.count("a"))



string bulit-in function------------->1.len()--->thia will find the length of the string,which is number char present in that string
                                           
                                        eg:so="python is a language"
                                        print(len(so))
                                              
                                      2.max()--------> will the max char in the string
                                              eg:so="python is a language"
                                                  print(max(so))
                                      3.min()--------->will get the min char in the string
                                                         eg:so="python is a language"
                                                          print(min(so))

















         















                                                 


