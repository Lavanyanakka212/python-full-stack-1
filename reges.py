"""Regular expression:-
----->reg exp is an sequence of char that can be searching pattern.
----->to used regular expressions we have to import remodule
syntax:import re

1.function()
---------------------
----->it will find all the char that are in string
ex:
import re
txt = 'python is a language and also called dynamically typed'
print(re.findall('[a]',txt))

2.search()
---------------
----->this srearch will find the char,but it will give the first sequence that found in string.
ex:

import re
txt = 'python is a language and also called dynamically typed'
print(re.search(' ',txt))


3.split()
----------------
ex:
import re
txt = 'python is a language and also called dynamically typed'
print(re.split(' ',txt))

4.fullmatch()
----------------
import re
txt = 'python is a language and also called dynamically typed'
print(re.sub(' ','&',txt))

5.fullmatch()
-----------

metachar:
-----------
[]
-------------->
ex:

import re
txt = 'I have 100 Rupees'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))

^
---------------->it will taking only starting letters.
ex:

import re
txt = 'I have 100 Rupees'
print(re.findall('^I have',txt))
print(re.search('^I have',txt))

o/p:---['school']
       <re.Match object; span=(14, 20), match='school'>

$
------------->it will taking only ending letters.
ex:

import re
some = 'I am going to school'
print(re.findall('school$',some))
print(re.search('school$',some))

o/p:---['school']
       <re.Match object; span=(14, 20), match='school'>
.
--------------->one dot will take one letter.
ex:

import re
any_ = 'I am going to school'
print(re.findall('g...g',any_))
print(re.search('s.....',any_))

o/p:['going']
    <re.Match object; span=(14, 20), match='school'>

*
-------------------
ex:

import re
how= 'python module will going complete this week'
print(re.findall('p.*n',how))
print(re.findall('p.*ython',how))
print(re.findall('p.*',how))
print(re.search('p.*n',how))

o/p:['python module will goin']
['python']
['python module will going complete this week']
<re.Match object; span=(0, 23), match='python module will goin'>

+
----------------->will take atleast one character.
ex:

import re
now= 'python is a language'
print(re.findall('p.+thon',now))

o/p:['python']

{}
------------------->specific number on size.
ex:

import re
now= 'python is a language'
print(re.findall('p.{9}',now))
print(re.search('p.{18}',now))

o/p:['python is ']
<re.Match object; span=(0, 19), match='python is a languag'>"""

    
