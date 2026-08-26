# find the factorial of a number using while loop, take number n as input
n = int(input("Enter a number: "))

fact = 1
i = 1


while i <= n:
    fact *= i  # fact = fact * i
    i += 1     # Move to next number

import math 
print(math.factorial(i))