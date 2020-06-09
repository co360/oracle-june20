# Get two numbers from the user
# Output the difference and tell if the difference is
# positive, negative or zero

# Input

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

# Process

res = a - b

# Output

print('-------------------------------')
print('DIFFERENCE: ', abs(a - b))
if(res > 0):
    print('The result was positive')
elif(res < 0):
    print('The result was negative')
else:
    print('The result was zero')
