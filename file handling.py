 -------------------file hanndling-----------------------

---->file handler is an object that gives more options like creating,updating.

Two waysto open the files:

1.open()
---------------
syntax:------->do=open('file_name','mode')

close()
------------------
ex:

do=open('abcdef.txt','r')
print(do.read())
do.close()

2.with (keyword)
-------------------
syntax:-->with open('file_name','mode')as do:

with open('demo.txt','r') as do:
    print(do.read())

modes
----------------
R------>used to read the file.incase if the file is not present it will raise error.

W------>the file is used to write the text inside the file and it will override the text inside file,incase if the file is not present it will create
        a new file with the same given..

with open('dem.txt','w') as do:
    print(do.write('we are use file handling'))

A------->this is used to add the text at last position inside the file...

with open('dem.txt','a') as do:
    print(do.write('we are use file handling'))
    
X------->USed to create a new by adding the inside the file,incase if the files is present it will raise an error....

with open('hello.txt','x') as do:
    print(do.write('we are use file handling'))

Write()
-------------
------> this function is used to add the text inside a file or update a file with new text....

with open('demo.txt','w') as do:
    print(do.write('we are use file handling'))

with open('demo.txt','a') as do:
    print(do.write('we are use file handling'))


Read()
-----------
------->used to read a file and this read() will read file chunk by chunk.
        we can also specify the size

with open('demo.txt','r') as do:
    print(do.read(10))

Readline()
---------------
------>this readline() function will read only one line ata a line..

with open('demo.txt','r') as do:
    print(do.readline())

Readlines()
----------------
------->this function will read whole file and give it in a list each line is one ind


with open('demo.txt','r') as do:
    print(do.readlines())


    
