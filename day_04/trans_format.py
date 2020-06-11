Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 6
>>> b = 8
>>> 
>>> print('Sum : ', a + b)
Sum :  14
>>> print('Sum : %d' % a + b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print('Sum : %d' % a + b)
TypeError: can only concatenate str (not "int") to str
>>> print('Sum : %d' % (a + b))
Sum : 14
>>> print('Sum : %d', (a + b))
Sum : %d 14
>>> print('Sum : %d' % (a + b))
Sum : 14
>>> 'Sum : {}'.format((a + b))
'Sum : 14'
>>> 'my name is {} and age is {}'.format('Anil', 35)
'my name is Anil and age is 35'
>>> template = 'my name is {} and age is {}
SyntaxError: EOL while scanning string literal
>>> template = 'my name is {} and age is {}'
>>> template.format('Anil', 35)
'my name is Anil and age is 35'
>>> d = {'anil':35, 'sunil':45, 'raj':55 }
>>> for key, value in d.items():
	print(template.format(key, value))

	
my name is anil and age is 35
my name is sunil and age is 45
my name is raj and age is 55
>>> template = 'my name is {0} and age is {1}'
>>> template.format('anil', 35)
'my name is anil and age is 35'
>>> 'my name is {1} and age is {0}'.format('anil', 35)
'my name is 35 and age is anil'
>>> 'my name is {name} and age is {age}'.format(name='anil', age=35)
'my name is anil and age is 35'
>>> 'my name is {name:10} and age is {age:5}'.format(name='anil', age=35)
'my name is anil       and age is    35'
>>> 'my name is {name:>10} and age is {age:<5}'.format(name='anil', age=35)
'my name is       anil and age is 35   '
>>> 'my name is {name:^10} and age is {age:^5}'.format(name='anil', age=35)
'my name is    anil    and age is  35  '
>>> template = 'my name is {name:^10} and age is {age:^5}'
>>> for key, value in d.items():
	print(template.format(name=key, age=value))
	\

	  
SyntaxError: invalid syntax
>>> for key, value in d.items():
	print(template.format(name=key, age=value))

	
my name is    anil    and age is  35  
my name is   sunil    and age is  45  
my name is    raj     and age is  55  
>>> 
