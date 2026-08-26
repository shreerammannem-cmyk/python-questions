# create an example while loop which will not terminate , and prints `hi` in each iteration
# and how will you stop the program manually?
n = int(input("Enter a number: "))

fact = 1
i = 1

# Multiply numbers from 1 up to n
while i <= n:
    fact *= i  # fact = fact * i
    i += 1     # Move to next number

print(f"The factorial of {n} is: {fact}")