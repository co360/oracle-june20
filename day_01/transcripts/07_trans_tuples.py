Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ('red', 'green' , 'blue')
>>> T1 = ('pink', 'yellow', 'maroon')
>>> type(T)
<class 'tuple'>
>>> 
>>> T + T1
('red', 'green', 'blue', 'pink', 'yellow', 'maroon')
>>> T
('red', 'green', 'blue')
>>> T1
('pink', 'yellow', 'maroon')
>>> 
>>> # -------------------
>>> 
>>> T[0]
'red'
>>> T[0] = 'cerulean'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    T[0] = 'cerulean'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> # --------------------
>>> 
>>> reversed(T)
<reversed object at 0x000001F8DD12FF98>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> 
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> sorted(T, reverse=True)
['red', 'green', 'blue']
>>> 
>>> T
('red', 'green', 'blue')
>>> 
>>> # ----------------------
>>> 
>>> 'red' in T
True
>>> T.index('red')
0
>>> T.count('red')
1
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T
>>> T
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    T
NameError: name 'T' is not defined
>>> 
>>> 
>>> # -------------------------
>>> 
>>> T = ('red', 'green' , 'blue')
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> # Note: The same thing is applicable to lists as well
>>> 
>>> r,g = T
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    r,g = T
ValueError: too many values to unpack (expected 2)
>>> r, *x = T
>>> r
'red'
>>> x
['green', 'blue']
>>> r,g,b,y = T
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    r,g,b,y = T
ValueError: not enough values to unpack (expected 4, got 3)
>>> r,g,b,y = T + (,)
SyntaxError: invalid syntax
>>> r,g,b,y = T + ()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    r,g,b,y = T + ()
ValueError: not enough values to unpack (expected 4, got 3)
>>> r,g,b,*y = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> y
[]
>>> # --------------------------------------------------
>>> 
>>> T
('red', 'green', 'blue')
>>> L = list(T)
>>> L
['red', 'green', 'blue']
>>> L.append('yellow')
>>> L.insert(1, 'pink')
>>> L
['red', 'pink', 'green', 'blue', 'yellow']
>>> T = tuple(L)
>>> 
>>> T
('red', 'pink', 'green', 'blue', 'yellow')
>>> 
