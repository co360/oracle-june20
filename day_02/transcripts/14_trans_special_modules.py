Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Date and Time
>>> 
>>> from datetime import datetime
>>> 
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 6, 10, 3, 22, 17, 673025)
>>> t.year
2020
>>> t.month
6
>>> t.day
10
>>> t.hour
3
>>> t.minute
22
>>> t.second
17
>>> f = "%A, %d-%B-%Y, %I:%M:%S %p"
>>> t.strftime(f)
'Wednesday, 10-June-2020, 03:22:17 AM'
>>> def randomize(n):
	L = []
	for i in range(n):
		L.append(i)

		
>>> import random
>>> def randomize(n):
	L = []
	for i in range(n):
		L.append(random.randint(1, 100))
	return L

>>> randomize(10)
[14, 35, 3, 97, 44, 74, 12, 24, 99, 29]
>>> randomize(100)
[56, 26, 49, 13, 48, 20, 46, 15, 98, 62, 99, 47, 13, 78, 15, 83, 8, 19, 16, 62, 30, 66, 79, 46, 89, 91, 46, 27, 26, 7, 22, 91, 26, 68, 81, 74, 14, 51, 47, 21, 79, 15, 50, 7, 90, 81, 74, 48, 29, 20, 52, 69, 49, 70, 81, 24, 49, 99, 7, 37, 2, 15, 12, 73, 39, 17, 4, 72, 16, 16, 4, 3, 67, 55, 32, 49, 95, 78, 46, 18, 90, 18, 46, 90, 23, 76, 17, 14, 93, 31, 85, 14, 71, 65, 74, 6, 74, 99, 91, 43]
>>> 
>>> 
>>> def profile():
	t1 = datetime.now()
	randomize(1000)
	t2 = datetime.now()
	return t2 - t1

>>> print(profile())
0:00:00.003004
>>> 
>>> def profile():
	t1 = datetime.now()
	for i in range(100):
		print('.', end='')
	t2 = datetime.now()
	return t2 - t1

>>> print(profile())
....................................................................................................0:00:00.728527
>>> 
>>> 
>>> 
>>> from itertools import permutatations, combinations
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    from itertools import permutatations, combinations
ImportError: cannot import name 'permutatations' from 'itertools' (unknown location)
>>> from itertools import permutatation, combination
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    from itertools import permutatation, combination
ImportError: cannot import name 'permutatation' from 'itertools' (unknown location)
>>> from itertools import permutation, combination
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    from itertools import permutation, combination
ImportError: cannot import name 'permutation' from 'itertools' (unknown location)
>>> from itertools import permutations, combinations
>>> s = 'ABCD'
>>> permutations(s, 3)
<itertools.permutations object at 0x0000020C6C92CCA8>
>>> list(permutations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(combinations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
>>> 
>>> 
>>> 
>>> from functools import reduce
>>> L = [1, 2, 3, 4, 5]
>>> reduce(lambda x, y + x + y, L)
SyntaxError: invalid syntax
>>> reduce(lambda x, y : x + y, L)
15
>>> N = ['p', 'e', 'r', 'l']
>>> reduce(lambda x, y : x + y, N)
'perl'
>>> 
>>> 
>>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
>>> s = 'perl'
>>> L = ['apples', 'bananas', 'cat', 'dog']
>>> 
>>> from operator import itemgetter
>>> itemgetter(1)(s)
'e'
>>> itemgetter(1)(L)
'bananas'
>>> itemgetter(-1)(inventory)
('orange', 1)
>>> 
>>> 
>>> L = ['apples', 'bananas', 'cat', 'dog']
>>> L.sort()
>>> L
['apples', 'bananas', 'cat', 'dog']
>>> f = itemgetter(1)
>>> type(f)
<class 'operator.itemgetter'>
>>> f(iventory)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    f(iventory)
NameError: name 'iventory' is not defined
>>> f(inventory)
('banana', 2)
>>> f('python')
'y'
>>> L.sort(key=f)
>>> L
['bananas', 'cat', 'dog', 'apples']
>>> 
