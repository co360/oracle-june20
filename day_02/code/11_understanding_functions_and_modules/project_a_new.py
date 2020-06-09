# Project A
# Function based approach

# Program to determine if a number is prime or not

def checkprime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True


# ------------------------------

print("Name: ", __name__)

if __name__ == "__main__":
    
    n = int(input('Enter a number: '))

    prime = checkprime(n)

    if(prime == True):
        print('The number is prime')
    else:
        print('The number is not prime')

