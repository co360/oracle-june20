Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Lamda functions
>>> 
>>> lambda x,y:x + y
<function <lambda> at 0x00000187E2102620>
>>> f = lambda x,y : x + y
>>> type(f)
<class 'function'>
>>> f(10, 17)
27
>>> f("Hellow ", "World")
'Hellow World'
>>> f([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> 
>>> L = ['zebra', 'goat', 'alpaca', 'giraffe' ,' donkey']
>>> L.sort()
>>> L
[' donkey', 'alpaca', 'giraffe', 'goat', 'zebra']
>>> L = ['zebra', 'goat', 'alpaca', 'giraffe' ,'donkey']
>>> L.sort()
>>> L
['alpaca', 'donkey', 'giraffe', 'goat', 'zebra']
>>> L.sort(key=lambda s:s[-1])
>>> L
['alpaca', 'zebra', 'giraffe', 'goat', 'donkey']
>>> 
>>> 
>>> # map()
>>> # filter()
>>> # zip()
>>> 
>>> C = [100, 34, 45, 56]
>>> F = []
>>> for temp in C:
	F.append(temp * 1.8 + 32)

	
>>> F
[212.0, 93.2, 113.0, 132.8]
>>> 
>>> f = map(lambda t : t * 1.8 + 32, C)
>>> f
<map object at 0x00000187E2062D30>
>>> list(f)
[212.0, 93.2, 113.0, 132.8]
>>> 
>>> 
>>> 
>>> 
>>> N = list(range(1, 101))
>>> o = []
>>> for n in N:
	if(n % 7 == 0 and n % 9 == 0):
		o.append(n)

		
>>> o
[63]
>>> filfunc = lambda n : (n % 7 == 0 and n % 9 == 0)
>>> N = list(range(1, 1001))
>>> o = filter(filfunc, N)
>>> o
<filter object at 0x00000187E21125F8>
>>> list(o)
[63, 126, 189, 252, 315, 378, 441, 504, 567, 630, 693, 756, 819, 882, 945]
>>> 
>>> 
>>> 
>>> t1 = ('anil', 'sunil', 'raj')
>>> t2 = ('London', 'Bangalore', 'California')
>>> list(zip(t1, t2))
[('anil', 'London'), ('sunil', 'Bangalore'), ('raj', 'California')]
>>> dict(zip(t1, t2))
{'anil': 'London', 'sunil': 'Bangalore', 'raj': 'California'}
>>> 
>>> 
>>> t = [('anil', 'London'), ('sunil', 'Bangalore'), ('raj', 'California')]
>>> list(zip(*t))
[('anil', 'sunil', 'raj'), ('London', 'Bangalore', 'California')]
>>> d = {'anil': 'London', 'sunil': 'Bangalore', 'raj': 'California'}
>>> list(zip(*d.items()))
[('anil', 'sunil', 'raj'), ('London', 'Bangalore', 'California')]
>>> 
>>> 
>>> # -------------------------- Comprehensions
>>> 
>>> L = ['apples', 'bananas', 'cauliflower', 'drunsticks']
>>> D = []
>>> for item in L:
	D.append((item, len(item)))

	
>>> D
[('apples', 6), ('bananas', 7), ('cauliflower', 11), ('drunsticks', 10)]
>>> D1 = [(item, len(item)) for item in L]
>>> D1
[('apples', 6), ('bananas', 7), ('cauliflower', 11), ('drunsticks', 10)]
>>> 
>>> 
>>> # Syntax: [<expr> <loop> <conditional>]
>>> 
>>> N = list(range(1, 1001))
>>> L1 = [x for x in N if x % 3 == 0 and x % 7 == 0]
>>> L1
[21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294, 315, 336, 357, 378, 399, 420, 441, 462, 483, 504, 525, 546, 567, 588, 609, 630, 651, 672, 693, 714, 735, 756, 777, 798, 819, 840, 861, 882, 903, 924, 945, 966, 987]
>>> 
>>> L2 = [(x, x**2, x**3) for x in range(1, 11)]
>>> L2
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> L = list(range(11, 100))
>>> L
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> L3 = [x for x in L if int(str(x)[1]) + int(str(x)[0]) <= 10]
>>> L3
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 64, 70, 71, 72, 73, 80, 81, 82, 90, 91]
>>> 
>>> 
>>> 
>>> s = "mississippi"
>>> d = {}
>>> for char in s:
	if(char in d.keys()):
		d[char] = d[char] + 1
	else:
		d[char] = 1

		
>>> d
{'m': 1, 'i': 4, 's': 4, 'p': 2}
>>> from collections import Counter
>>> z = Counter(s)
>>> z
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
>>> L = ['apples', 'bananas', 'cauliflower', 'drunsticks']
>>> d = { key:Counter(key) for key in L }
>>> d
{'apples': Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1, 's': 1}), 'bananas': Counter({'a': 3, 'n': 2, 'b': 1, 's': 1}), 'cauliflower': Counter({'l': 2, 'c': 1, 'a': 1, 'u': 1, 'i': 1, 'f': 1, 'o': 1, 'w': 1, 'e': 1, 'r': 1}), 'drunsticks': Counter({'s': 2, 'd': 1, 'r': 1, 'u': 1, 'n': 1, 't': 1, 'i': 1, 'c': 1, 'k': 1})}
>>> 
>>> 
>>> L = list(range(1, 11))
>>> l
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> N = (x**2 for x in L if x in [3, 6, 9])
>>> N
<generator object <genexpr> at 0x00000187E20E7A20>
>>> list(N)
[9, 36, 81]
>>> N = [x**2 if x in [3, 6, 9] else x for x in L]
>>> N
[1, 2, 9, 4, 5, 36, 7, 8, 81, 10]
>>> 
