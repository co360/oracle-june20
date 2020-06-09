# Project B

# Find all the prime numbers between a user
# given range

import project_a_new

# Inputs

start = int(input("Enter the start : "))
end = int(input("Enter the end : "))

# Process

primes = []
for num in range(start, end + 1):
    if(project_a_new.checkprime(num)):
        primes.append(num)

# Output

print('-'*40)
print("PRIMES:")
print(primes)
