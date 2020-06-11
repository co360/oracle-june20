import re
data = ['ab', 'abc', 'a5e', 'a6f', '123 a6c', 'a5b', 'a55b', 'a555b', 'a5555b',
        'a55555b', 'a555555b', 'a5xb', '1/4', '3+2=5', 'def ghi', 'abc ab']
for item in data:
	m = re.search(r'a55{4}b', item)
	if m:
		print (m.group() + ' matched in ' + '\'' + item + '\'')


'''
a.c
a[0-9][^0-9]
a.[abd-z]
[0-9]\+[0-9]
a[^c][^0-9]
bc|a6

a\D\D
...\s.

a6  vs ^a6
..c vs ..c$

ab\b
ab\B

a5555*
a5555+
a5?\D
a5{4}\D

a5{2,5}b
a5{2,}b
a5{,5}b
a5{4}b


'''
