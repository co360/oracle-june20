Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = []
>>> type(L)
<class 'list'>
>>> L = ['red', 'green', 12, 45.6, True, False, ['a', 'b', 'c']]
>>> 
>>> # Accessability : subscripting
>>> 
>>> L[0]
'red'
>>> l[2]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l[2]
NameError: name 'l' is not defined
>>> L[2]
12
>>> L[-1]
['a', 'b', 'c']
>>> L[-1][1]
'b'
>>> L[2:5]
[12, 45.6, True]
>>> L[::-1]
[['a', 'b', 'c'], False, True, 45.6, 12, 'green', 'red']
>>> 
>>> 
>>> # Mutability aspect of lists
>>> 
>>> L = ['red', 'green', 'blue']
>>> L[0]
'red'
>>> L[0] = 'orange'
>>> L
['orange', 'green', 'blue']
>>> 
>>> L[0]
'orange'
>>> L[0][0]
'o'
>>> L[0][0] = 'R'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    L[0][0] = 'R'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> L
['orange', 'green', 'blue']
>>> L1 = ['white', 'black']
>>> L[1]
'green'
>>> L[1] = L1
>>> L
['orange', ['white', 'black'], 'blue']
>>> L = ['red', 'green', 'blue']
>>> L[1]
'green'
>>> L[1:2]
['green']
>>> L[1:2] = L1
>>> L
['red', 'white', 'black', 'blue']
>>> 
>>> 
>>> # Operators that work on lists
>>> 
>>> L
['red', 'white', 'black', 'blue']
>>> L2 = ['green', 'grey']
>>> L + L2
['red', 'white', 'black', 'blue', 'green', 'grey']
>>> L * 3
['red', 'white', 'black', 'blue', 'red', 'white', 'black', 'blue', 'red', 'white', 'black', 'blue']
>>> 'orange' in L
False
>>> len(L + L1)
6
>>> L
['red', 'white', 'black', 'blue']
>>> del L[-1]
>>> del
SyntaxError: invalid syntax
>>> L
['red', 'white', 'black']
>>> del
SyntaxError: invalid syntax
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> 
>>> # ----------------------------- Operations on lists
>>> 
>>> L
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> L = ['red', 'green', 'blue']
>>> 
>>> 
>>> # Add elements to the list
>>> 
>>> L.append('yellow')
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append('orange')
>>> L
['red', 'green', 'blue', 'yellow', 'orange']
>>> ['red', 'green', 'blue', 'yellow', 'orange']
['red', 'green', 'blue', 'yellow', 'orange']
>>> L.insert(2, 'pink')
>>> L
['red', 'green', 'pink', 'blue', 'yellow', 'orange']
>>> L1 = ['white', 'grey', 'black']
>>> L.extend(L1)
>>> L
['red', 'green', 'pink', 'blue', 'yellow', 'orange', 'white', 'grey', 'black']
>>> 
>>> 
>>> # Remove elements
>>> 
>>> # del L[2]
>>> 
>>> L.pop()
'black'
>>> L
['red', 'green', 'pink', 'blue', 'yellow', 'orange', 'white', 'grey']
>>> L.pop()
'grey'
>>> L.pop(2)
'pink'
>>> L.remove('blue')
>>> L
['red', 'green', 'yellow', 'orange', 'white']
>>> 
>>> 
>>> # Search
>>> 
>>> L.index('grey')
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    L.index('grey')
ValueError: 'grey' is not in list
>>> L.find('grey')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    L.find('grey')
AttributeError: 'list' object has no attribute 'find'
>>> L.count('red')
1
>>> L.append('red')
>>> L.count('red')
2
>>> L
['red', 'green', 'yellow', 'orange', 'white', 'red']
>>> L.index('green')
1
>>> L.index('red')
0
>>> 
>>> # Rearranging the values in the list
>>> 
>>> L
['red', 'green', 'yellow', 'orange', 'white', 'red']
>>> sorted(L)
['green', 'orange', 'red', 'red', 'white', 'yellow']
>>> L
['red', 'green', 'yellow', 'orange', 'white', 'red']
>>> sorted(L, reverse=True)
['yellow', 'white', 'red', 'red', 'orange', 'green']
>>> L.sort()
>>> L
['green', 'orange', 'red', 'red', 'white', 'yellow']
>>> L.sort(reverse=True)
>>> L
['yellow', 'white', 'red', 'red', 'orange', 'green']
>>> 
>>> L
['yellow', 'white', 'red', 'red', 'orange', 'green']
>>> L.reverse()
>>> L
['green', 'orange', 'red', 'red', 'white', 'yellow']
>>> reversed(L)
<list_reverseiterator object at 0x000002A77644F048>
>>> list(reversed(L))
['yellow', 'white', 'red', 'red', 'orange', 'green']
>>> 
>>> 
>>> # Copying
>>> 
>>> L
['green', 'orange', 'red', 'red', 'white', 'yellow']
>>> 
>>> L = ['red', 'white', 'yellow']
>>> L1 = L
>>> 
>>> L
['red', 'white', 'yellow']
>>> L1
['red', 'white', 'yellow']
>>> L1[1] = 'black'
>>> L1
['red', 'black', 'yellow']
>>> L
['red', 'black', 'yellow']
>>> 
>>> 
>>> from copy import deepcopy
>>> # import copy  ---> copy.deepcopy()
>>> 
>>> 
>>> L
['red', 'black', 'yellow']
>>> L2 = deepcopy(L)
>>> L
['red', 'black', 'yellow']
>>> L2
['red', 'black', 'yellow']
>>> L[1] = 'white'
>>> L
['red', 'white', 'yellow']
>>> L2
['red', 'black', 'yellow']
>>> L1
['red', 'white', 'yellow']
>>> 
>>> 
>>> # Iteration
>>> 
>>> L
['red', 'white', 'yellow']
>>> for item in L:
	print(item.upper())

	
RED
WHITE
YELLOW
>>> 
