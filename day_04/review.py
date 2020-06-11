Numbers - numerical values
Operators - arithmetic, relational, logical,
built-in functions - int(), float(), bin(), oct(), hex(), abs(),
modules - math, random

Strings - collection of characters - "", '', '''  '''
Operators - + * len in del
built-in functions -
case - upper(), lower(), capitalize()
querying - isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith()
searching - count(), find()
modifications - replace(), split(), join(), strip(), lstrip(), rstrip(), rjust(), ljust()
iteration -> for loop

Lists = ordered collection of objects - []
Operators + * len in del
accessability [start:end:skip] [0] [3:6] [1:10:2]
replace L[5] = Value/object
built-in functions
adding values append(), extend(), insert()
removing elements pop(), remove()
searching index(), count()
re-arranging sort(), reverse(), sorted(), reversed()
copying -> deepcopy()
iteration -> for loop


Tuples = ordered collection of objects - () -> immutable list
Operators + * len in del
accessability [start:end:skip] [0] [3:6] [1:10:2]
searching index(), count()
re-arranging sorted(), reversed()
copying -> deepcopy()
iteration -> for loop

Lists/Tuple    x,y,*z = ('red', 'green', 'yellow', 'blue')

Sets = unordered collection - {} -> immutable -> mathematical set theory
Operators | & ^
built-ins -> add(), update(), remove(), intersection(), union()
iteration -> for loop

Dictionaries = unordered collection -> { key:Value }
d[key] = value -> to add a new key value pair
d.setdefault()
d.remove()
d.update()
d.keys(), d.values(), d.items()
iteration -> for loop

# ---------------------------------------------

if <condition>:
    <statements>
elif <condition>:
    <statements>
..
..
else:
    <statements>

# ----------------------------------------------

for <var> in <iterable>:
    <statements>

while <condition>:
    <statement>

break statement

# ----------------------------------------------

def <fucntionname>(<arg1>, <arg2> ....):
    <logic>
    return <expr>

# ----------------------------------------------

modules.py -> module/package/library
    <collection of functions>
    def function()
        return <expr>

if __name__ == '__main__':

    <test code>

---------------------------------------

import module
module.function()

# ----------------------------------------------

Special functions: map(), filter(), zip()
Lambda function: fobj = lambda x,y : x + y
Special modules:
datetime -> now(), strftime(), t1 + t2, <format strings>
functools -> reduce()
itertools -> permutation(), combination()
collections -> Counter()
operator -> itemgetter()


# ----------------------------------------------

comprehensions -> [<expr> <loop> <condition>]

exception handling ->
try:
    <statements>
except:
    <statements>
else:
    <statements>
finally:
    <statements>

# ----------------------------------------------

OOP

classmodule.py

    class <classname1>(object):

        # data items

        # methods

    class <classname2>(object):

        # data items

        # methods
