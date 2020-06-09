Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> 
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'p', 'i', 'm', 's'}
>>> 
>>> 
>>> 
>>> # ----------------------------------
>>> 
>>> s1 = set('abcdefg')
>>> s1
{'a', 'f', 'g', 'e', 'd', 'c', 'b'}
>>> s2 = {'e', 'f', 'g', 'h', 'i', 'j' }
>>> 
>>> type(s1)
<class 'set'>
>>> s1 + s2
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> 
>>> 
>>> # -----------------------------------
>>> 
>>> s1 | s2
{'a', 'f', 'j', 'g', 'e', 'h', 'd', 'c', 'i', 'b'}
>>> s1 & s2
{'e', 'f', 'g'}
>>> s1 ^ s2
{'a', 'j', 'h', 'd', 'c', 'i', 'b'}
>>> 
>>> # ------------------------------------
>>> 
>>> s1
{'a', 'f', 'g', 'e', 'd', 'c', 'b'}
>>> s1.add('x')
>>> s1
{'a', 'f', 'g', 'x', 'e', 'd', 'c', 'b'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'a', 'f', 'z', 'g', 'x', 'y', 'e', 'd', 'c', 'b'}
>>> s1.remove('x')
>>> s1
{'a', 'f', 'z', 'g', 'y', 'e', 'd', 'c', 'b'}
>>> 
>>> 
>>> s1.intersection(s2)
{'e', 'f', 'g'}
>>> s1.union(s2)
{'a', 'f', 'z', 'g', 'j', 'b', 'e', 'h', 'd', 'y', 'i', 'c'}
>>> 
>>> # -------------------------------
>>> 
>>> L = ['red', 'green', 'blue', 'red']
>>> 
>>> newL = []
>>> for item in L:
	if(item not in newL):
		newL.append(item)

		
>>> newL
['red', 'green', 'blue']
>>> 
>>> 
>>> L
['red', 'green', 'blue', 'red']
>>> S = list(set(L))
>>> S
['red', 'green', 'blue']
>>> 
