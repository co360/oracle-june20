Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # record --> 'Anil', 35, 100000, California, India'
>>> 
>>> s = {'Anil', 35, '100000', 'California', 'India'}
>>> type(s)
<class 'set'>
>>> <class 'set'>
SyntaxError: invalid syntax
>>> s
{35, 'India', 'California', '100000', 'Anil'}
>>> 
>>> T = ('Anil', 35, '100000', 'California', 'India')
>>> T
('Anil', 35, '100000', 'California', 'India')
>>> 
>>> L = ['Anil', 35, '100000', 'California', 'India']
>>> L
['Anil', 35, '100000', 'California', 'India']
>>> # 0 -> name 1 -> age...
>>> 
>>> 
>>> D = { 'name
      
SyntaxError: EOL while scanning string literal
>>> D = { 'name':'Anil', 'age':35, 'salary':'100000', 'workaddr':'California', 'homeaddr':'India' }
>>> D
{'name': 'Anil', 'age': 35, 'salary': '100000', 'workaddr': 'California', 'homeaddr': 'India'}
>>> D['name']
'Anil'
>>> D['age']
35
>>> D['salary']
'100000'
>>> 
>>> 
>>> # ---------------------------------------- Operations
>>> 
>>> D
{'name': 'Anil', 'age': 35, 'salary': '100000', 'workaddr': 'California', 'homeaddr': 'India'}
>>> 
>>> 
>>> D['dob']
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    D['dob']
KeyError: 'dob'
>>> D['dob'] = '13/06/1991'
>>> D
{'name': 'Anil', 'age': 35, 'salary': '100000', 'workaddr': 'California', 'homeaddr': 'India', 'dob': '13/06/1991'}
>>> D.setdefault('bloodgrp', 'b+')
'b+'
>>> D
{'name': 'Anil', 'age': 35, 'salary': '100000', 'workaddr': 'California', 'homeaddr': 'India', 'dob': '13/06/1991', 'bloodgrp': 'b+'}
>>> 
>>> D1 = {'tax':'5000', 'investments':'15000'}
>>> D.update(D1)
>>> D
{'name': 'Anil', 'age': 35, 'salary': '100000', 'workaddr': 'California', 'homeaddr': 'India', 'dob': '13/06/1991', 'bloodgrp': 'b+', 'tax': '5000', 'investments': '15000'}
>>> 
>>> 
>>> D.pop('age')
35
>>> D
{'name': 'Anil', 'salary': '100000', 'workaddr': 'California', 'homeaddr': 'India', 'dob': '13/06/1991', 'bloodgrp': 'b+', 'tax': '5000', 'investments': '15000'}
>>> # del D['key']
>>> 
>>> 
>>> # -----------------------------------------------------
>>> 
>>> D.keys()
dict_keys(['name', 'salary', 'workaddr', 'homeaddr', 'dob', 'bloodgrp', 'tax', 'investments'])
>>> D.values()
dict_values(['Anil', '100000', 'California', 'India', '13/06/1991', 'b+', '5000', '15000'])
>>> D.items()
dict_items([('name', 'Anil'), ('salary', '100000'), ('workaddr', 'California'), ('homeaddr', 'India'), ('dob', '13/06/1991'), ('bloodgrp', 'b+'), ('tax', '5000'), ('investments', '15000')])
>>> 
>>> 
>>> # ---------------------------------------------------
>>> 
>>> 
>>> # Mr. Ajay Nair
>>> 
>>> 
>>> emp1 = {'name': 'Anil', 'salary': '100000', 'workaddr': 'California'}
>>> emp2 = {'name': 'Sunil', 'salary': '200000', 'workaddr': 'New Jersy'}
>>> emp3 = {'name': 'Raj', 'salary': '300000', 'workaddr': 'Texas'}
>>> 
>>> team = { 'TM01':emp1, 'TM02':emp2, 'TM03':emp3 }
>>> team = { 'TM01':emp1, 'TM02':emp2, 'TM03':emp3 }
>>> team
{'TM01': {'name': 'Anil', 'salary': '100000', 'workaddr': 'California'}, 'TM02': {'name': 'Sunil', 'salary': '200000', 'workaddr': 'New Jersy'}, 'TM03': {'name': 'Raj', 'salary': '300000', 'workaddr': 'Texas'}}
>>> team['TM01
     
SyntaxError: EOL while scanning string literal
>>> team['TM01']['name']
'Anil'
>>> team.setdefault('TM04', {'name': 'John', 'salary': '400000', 'workaddr': 'Los Angeles'}}
SyntaxError: invalid syntax
>>> team.setdefault('TM04', {'name': 'John', 'salary': '400000', 'workaddr': 'Los Angeles'})
{'name': 'John', 'salary': '400000', 'workaddr': 'Los Angeles'}
>>> team
{'TM01': {'name': 'Anil', 'salary': '100000', 'workaddr': 'California'}, 'TM02': {'name': 'Sunil', 'salary': '200000', 'workaddr': 'New Jersy'}, 'TM03': {'name': 'Raj', 'salary': '300000', 'workaddr': 'Texas'}, 'TM04': {'name': 'John', 'salary': '400000', 'workaddr': 'Los Angeles'}}
>>> team['TM04']['workaddr']
'Los Angeles'
>>> 
>>> 
>>> D['age']
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    D['age']
KeyError: 'age'

>>> 
>>> 
>>> # Mr .Surya
>>> 
>>> 
>>> # int *i = [ [1,2,3], [4,5,6], [7,8,9] ]  --> 2D array
>>> 
>>> 
>>> data = input('Enter key value pair separated by space: ')
Enter key value pair separated by space: name surya
>>> data
'name surya'
>>> kv = data.split()
>>> kv
['name', 'surya']
>>> D = {}
>>> D.setdefault(kv[0], kv[1])
'surya'
>>> D
{'name': 'surya'}
>>> 
