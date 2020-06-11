Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> m = re.search(r"\d+\.\d+", "The floating value is 24.1632 units")
>>> m
<re.Match object; span=(22, 29), match='24.1632'>
>>> m.span()
(22, 29)
>>> m.group()
'24.1632'
>>> m = re.search(r"(\d+)\.(\d+)", "The floating value is 24.1632 units")
>>> m
<re.Match object; span=(22, 29), match='24.1632'>
>>> m.start()
22
>>> m.end()
29
>>> m.span()
(22, 29)
>>> m.group()
'24.1632'
>>> m.group(1)
'24'
>>> m.group(2)
'1632'
>>> m.groups()
('24', '1632')
>>> m.groupdict()
{}
>>> m = re.search(r"(?P<first>\d+)\.(?P<second>\d+)", "The floating value is 24.1632 units")
>>> m.group()
'24.1632'
>>> m.groups()
('24', '1632')
>>> m.groupdict()
{'first': '24', 'second': '1632'}
>>> 
