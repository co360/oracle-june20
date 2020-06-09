Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Loops
>>> 
>>> s = 'eagles'
>>> L = ['Iron Man', 'Thor', 'Hulk']
>>> T = ['Hotel California', 'Imagine', 'Wanted dead or alive!']
>>> T = ('Hotel California', 'Imagine', 'Wanted dead or alive!')
>>> S = {'Volvo
     
SyntaxError: EOL while scanning string literal
>>> S = {'volvo', 'mercedes', 'bmw', 'ford'}
>>> 
>>> D = {'name':'anil', 'age':35, 'blood':'b+', 'work':'London' }
>>> 
>>> 
>>> for char in s:
	print(char)

	
e
a
g
l
e
s
>>> for char in s:
	print(char, end=' ')

	
e a g l e s 
>>> for item in L + ['Black Widow', 'Hawkeye']:
	print(item.upper())

	
IRON MAN
THOR
HULK
BLACK WIDOW
HAWKEYE
>>> char
's'
>>> item
'Hawkeye'
>>> L + ['Black Widow', 'Hawkeye']
['Iron Man', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye']
>>> L + 'Hawkeye'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    L + 'Hawkeye'
TypeError: can only concatenate list (not "str") to list
>>> 
>>> 
>>> for entry in T:
	print(entry)
	\]
	
SyntaxError: unexpected character after line continuation character
for entry in T:
	print(entry)
	\]
>>> for entry in T:
	print(entry)

	
Hotel California
Imagine
Wanted dead or alive!
>>> D = {}
>>> for entry in T:
	name = entry
	value = len(entry)
	D.setdefault(name, value)

	
16
7
21
>>> D
{'Hotel California': 16, 'Imagine': 7, 'Wanted dead or alive!': 21}
>>> for entry in T:
	key = entry
	value = len(entry)
	D[key] = value

	
>>> D
{'Hotel California': 16, 'Imagine': 7, 'Wanted dead or alive!': 21}
>>> S
{'ford', 'bmw', 'mercedes', 'volvo'}
>>> L
['Iron Man', 'Thor', 'Hulk']
>>> L.append('Hawkeye')
>>> S
{'ford', 'bmw', 'mercedes', 'volvo'}
>>> L
['Iron Man', 'Thor', 'Hulk', 'Hawkeye']
>>> 
>>> av = {}
>>> for vehicle in S:
	print(vehicle)

	
ford
bmw
mercedes
volvo
>>> av
{}
>>> i = 0
>>> for vehicle in S:

	av.setdefault(L[i], vehicle)
	i += 0

	
'ford'
'ford'
'ford'
'ford'
>>> av
{'Iron Man': 'ford'}
>>> S
{'ford', 'bmw', 'mercedes', 'volvo'}
>>> for vehicle in S:
	av.setdefault(L[i], vehicle)
	i += 1

	
'ford'
'bmw'
'mercedes'
'volvo'
>>> av
{'Iron Man': 'ford', 'Thor': 'bmw', 'Hulk': 'mercedes', 'Hawkeye': 'volvo'}
>>> dictvar
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    dictvar
NameError: name 'dictvar' is not defined
>>> dictvar.setfault('nmae', 'anil')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    dictvar.setfault('nmae', 'anil')
NameError: name 'dictvar' is not defined
>>> dictvar.setdefault('nmae', 'anil')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dictvar.setdefault('nmae', 'anil')
NameError: name 'dictvar' is not defined
>>> dictvar = []
>>> dictvar.setdefault('nmae', 'anil')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dictvar.setdefault('nmae', 'anil')
AttributeError: 'list' object has no attribute 'setdefault'
>>> dictvar = {}
>>> dictvar.setdefault('nmae', 'anil')
'anil'
>>> dictvar
{'nmae': 'anil'}
>>> 
>>> 
>>> D = {'name':'anil', 'age':35, 'blood':'b+', 'work':'London' }
>>> 
>>> 
>>> for var in D:
	print(var)

	
name
age
blood
work
>>> for var in D.values():
	print(var)

	
anil
35
b+
London
>>> for var in D.items():
	print(var)

	
('name', 'anil')
('age', 35)
('blood', 'b+')
('work', 'London')
>>> 
\
>>> key, value = ('name', 'anil')
>>> key
'name'
>>> value
'anil'
>>> for key, value = D.items():
	
SyntaxError: invalid syntax
>>> for key, value in D.items():
	print(str(key) + ' ---> ' + str(value))

	
name ---> anil
age ---> 35
blood ---> b+
work ---> London
>>> newd = {}
>>> for key, value in D.items():
	newd.setdefault(value, key)

	
'name'
'age'
'blood'
'work'
>>> newd
{'anil': 'name', 35: 'age', 'b+': 'blood', 'London': 'work'}
>>> 
>>> 
>>> # ----------------------------------------------
>>> 
>>> # 5 X 1 = 5
>>> # 5 X 2 = 10
>>> L =[1, 2, 3, 4]
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]list(range(20, 30))
SyntaxError: invalid syntax
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(20, 50, 5))
[20, 25, 30, 35, 40, 45]
>>> 
>>> 
>>> print(str(5) + ' X ' + str(1) + ' = ' + str(5 * 1))
5 X 1 = 5
>>> for i in range(1, 11):
	print(str(5) + ' X ' + str(i) + ' = ' + str(5 * i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> print(5 + ' X ')
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    print(5 + ' X ')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(str(5) + ' X ')
5 X 
>>> 
>>> 
>>> i = 1
>>> while i <= 10:
	print(5 , ' X ', i , ' = ' , (5 * i))
	i += 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
