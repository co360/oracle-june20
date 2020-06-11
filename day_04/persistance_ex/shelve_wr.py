import shelve

L = ['red', 'green', 'blue', 'yellow']
S = set('aeiou')
D = {'name':'anil', 'age':35, 'company':'oracle'}

shfile = shelve.open("mydata.db")
shfile['mylist'] = L
shfile['myset'] = S
shfile['mydict'] = D

shfile.sync()
shfile.close()
