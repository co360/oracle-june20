try:
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    d = {}
    c = a/b
    d['c'] = c
    print(d['d'])
except ValueError:
    print('The input should be a integer')
except ZeroDivisionError:
    print('The number cannot be divided by zero')
except Exception as E:
    print('Some other exception occured')
    print(E)
else:
    print('The division result is : ', d['c'])
    '''
    try:
        print('The division result is : ', d['d'])
    except:
        print('Keys not arranged properly')
    '''
finally:
    print('Thank you!')
