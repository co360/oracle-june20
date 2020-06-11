import shelve

myfile = shelve.open("mydata.db")

mylist = myfile['mylist']
mydict = myfile['mydict']
myset  = myfile['myset']

myfile.close()

print(mylist)
print(mydict)
print(myset)
