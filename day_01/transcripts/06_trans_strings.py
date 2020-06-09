Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> type(s)
<class 'str'>
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[-1]
'n'
>>> 
>>> s[0]
'p'
>>> s[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> 
>>> # --------------------- Accessability
>>> # Subscripting
>>> # [index]
>>> # [startindex : endindex]
>>> # [startindex : endindex : skipindex]
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[3]
'h'
>>> s[6]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s[6]
IndexError: string index out of range
>>> s[-1]
'n'
>>> 
>>> 
>>> s[2:4]
'th'
>>> # [2:4] 2, 3
>>> 
>>> s[0:3]
'pyt'
>>> s[:3]
'pyt'
>>> s[2:6]
'thon'
>>> s[2:]
'thon'
>>> s[:]
'python'
>>> s[1:5:2] # 1 2 3 4 ---> 1 3
'yh'
>>> s[1:5:3]
'yo'
>>> s[::2]
'pto'
>>> s[::3]
'ph'
>>> s[::-1]
'nohtyp'
>>> s[::-2]
'nhy'
>>> 
>>> 
>>> # -------------------------- Operators
>>> 
>>> s1 = 'py'
>>> s2 = 'thon'
>>> 
>>> s1 + s2
'python'
>>> s1 * 3
'pypypy'
>>> 'th' in s1 + s2
True
>>> 'app' in s1 + s2
False
>>> len(s1 + s2)
6
>>> del s1
>>> del s2
>>> s1
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s1
NameError: name 's1' is not defined
>>> s2
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s2
NameError: name 's2' is not defined
>>> 
>>> # -------------------------- built-in functions for strings
>>> 
>>> # case of the string
>>> 
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s
'python'
>>> su = s.upper()
>>> s
'python'
>>> su
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> 
>>> 
>>> # querying functions
>>> 
>>> s1 = '123'
>>> s2 = 'asd'
>>> s3 = 'as43'
>>> s4 = ' '
>>> s5 = '$#%'
>>> 
>>> s1.isdigit() # Is the content of s1 all digits?
True
>>> s2.isdigit()
False
>>> s2.isalpha()
True
>>> s3.isalpha()
False
>>> s3.isalnum()
True
>>> s4.isspace()
True
>>> s5.isalnum()
False
>>> 
>>> 
>>> site = "www.oracle.com"
>>> site.startswith("https")
False
>>> site.endswith('com')
True
>>> 
>>> # Search
>>> 
>>> s
'python'
>>> s.find('h')
3
>>> s[3]
'h'
>>> s5 = 'mississippi'
>>> s5.count('s')
4
>>> s5.count('ss')
2
>>> 
>>> # Modifications of a string
>>> 
>>> text = '    this is some text   '
>>> text.strip()
'this is some text'
>>> text.lstrip()
'this is some text   '
>>> text.rstrip()
'    this is some text'
>>> text
'    this is some text   '
>>> 
>>> 
>>> text = "prometheus"
>>> text.rjust(20)
'          prometheus'
>>> text.ljust(20,'-')
'prometheus----------'
>>> 
>>> ip = '192-45-34-5'
>>> ip.replace('-', '.')
'192.45.34.5'
>>> ip
'192-45-34-5'
>>> correctedip = ip.replace('-', '.')
>>> correctedip
'192.45.34.5'
>>> 
>>> 
>>> # modifications: splitting and joining
>>> 
>>> text = "Long long ago in a galaxy far far away"
>>> text.split()
['Long', 'long', 'ago', 'in', 'a', 'galaxy', 'far', 'far', 'away']
>>> text.split('a')
['Long long ', 'go in ', ' g', 'l', 'xy f', 'r f', 'r ', 'w', 'y']
>>> L = ['Long long ', 'go in ', ' g', 'l', 'xy f', 'r f', 'r ', 'w', 'y']
>>> 'AA'.join(L)
'Long long AAgo in AA gAAlAAxy fAAr fAAr AAwAAy'
>>> 
