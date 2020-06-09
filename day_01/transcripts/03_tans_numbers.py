Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Welcome Oracle!')
Welcome Oracle!
>>> a = 5
>>> a
5
>>> print(a)
5
>>> type(a)
<class 'int'>
>>> a = 1.23
>>> type(a)
<class 'float'>
>>> a = 'Welcome Oracle!'
>>> type(a)
<class 'str'>
>>> # ---------------------------- Operators
>>> 
>>> # This is a comment
>>> 
>>> a = 5
>>> b = 2
>>> 
>>> # Arithmetic Operators
>>> 
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a ** b
25
>>> a % b
1
>>> a // b
2
>>> # Relational Operators
>>> 
>>> a > b  # Is a greater than b?  The answer is yes --> True
True
>>> a < b
False
>>> 
>>> # True and False are boolean values
>>> 
>>> a >= b
True
>>> a <= b
False
>>> a != b
True
>>> a == b
False
>>> a == ( b ** 2  + 1 )
True
>>> 
>>> 
>>> # Logcal Operator
>>> 
>>> a > b and b > 10
False
>>> a > b and a == (b *2 + 1)
True
>>> a > b or b > 10
True
>>> not(a > b or b > 10)
False
>>> 
>>> 
>>> # --------------------- In-built functions
>>> 
>>> a
5
>>> b
2
>>> a - b
3
>>> b - a
-3
>>> abs(a - b)
3
>>> abs(b - a )
3
>>> a = 100
>>> bin(a)
'0b1100100'
>>> '0b1100100'
'0b1100100'
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> 
>>> binvalue = '1101'
>>> type(binvalue)
<class 'str'>
>>> int(binvalue)
1101
>>> int(binvalue) + 25
1126
>>> int(binvalue, 2)
13
>>> bin(13)
'0b1101'
>>> bin(13) + 25
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    bin(13) + 25
TypeError: can only concatenate str (not "int") to str
>>> bin(binvalue)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    bin(binvalue)
TypeError: 'str' object cannot be interpreted as an integer
>>> bin(int(binvalue))
'0b10001001101'
>>> 
>>> 
>>> # --------------- Inputs from the user
>>> 
>>> input('Enter a number: ')
Enter a number: 12
'12'
>>> x = input('Enter a number: ')
Enter a number: 56
>>> x
'56'
>>> type(x)
<class 'str'>
>>> x + 45
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    x + 45
TypeError: can only concatenate str (not "int") to str
>>> x / 5
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    x / 5
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> int(x) + 45
101
>>> int(x) / 5
11.2
>>> float(x)
56.0
>>> int(x)
56
>>> x = input('Enter a number: ')
Enter a number: 12.345
>>> x
'12.345'
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '12.345'
>>> float(x)
12.345
>>> 
>>> 
>>> x = 100
>>> y = 'abc'
>>> y = x
>>> y
100
>>> 
>>> 
>>> x = input('Enter a number: ')
Enter a number: 345
>>> type(x)
<class 'str'>
>>> x = int(input('Enter a number: '))
Enter a number: 435
>>> type(x)
<class 'int'>
>>> x = int(input('Enter a number: '))
Enter a number: 34ij5k
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    x = int(input('Enter a number: '))
ValueError: invalid literal for int() with base 10: '34ij5k'
>>> x = int(input('Enter a number: '))
Enter a number: abc
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    x = int(input('Enter a number: '))
ValueError: invalid literal for int() with base 10: 'abc'
>>> x = int(input('Enter a number: '), 16)
Enter a number: abc
>>> x
2748
>>> hex(x)
'0xabc'
>>> 
>>> 
>>> # ------------------------- Built in Modules for working with numbers
>>> 
>>> 
>>> gcd(10, 5)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    gcd(10, 5)
NameError: name 'gcd' is not defined
>>> import math
>>> gcd(10, 5)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    gcd(10, 5)
NameError: name 'gcd' is not defined
>>> math.gcd(10, 5)
5
>>> math.sqrt(144)
12.0
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(math.radians(90))
1.0
>>> math.sin(90 * math.pi/180)
1.0
>>> 
>>> 
>>> import random
>>> random.randint(1, 100)
60
>>> random.randint(1, 100)
35
>>> random.randint(1, 100)
10
>>> random.randint(1, 100)
88
>>> random.randint(1, 100)
93
>>> random.randint(1, 100)
32
>>> random.randint(1, 100)
34
>>> random.randint(1, 100)
11
>>> random.randint(1, 100)
81
>>> 
