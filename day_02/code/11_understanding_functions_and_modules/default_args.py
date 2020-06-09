def message(name, mess = "Have a great day!"):
    print('Hi' + name + ' ' + mess)

message(mess="Take care!", name="Kiran" )

def average( *n ):
    print(n)
    return sum(n)/len(n)

print(average(5, 6, 7))

print(average(9, 3, 5, 6, 7))

def func(L, D, S):
    print(L)
    print(D)
    print(S)

func([1,2,3], {'name':'anil'}, {'a', 'b', 'c'})


def fun():
    pass
