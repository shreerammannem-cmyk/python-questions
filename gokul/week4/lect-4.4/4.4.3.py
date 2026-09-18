## Generate a list of 100 random numbers between 1 and 1000, and sort the list
##  create another list even, and add all the even numbers to this even list and print the list
## similarly create another list odd, and add all the odd numbers to this odd list and print the list
import random

# Generate 100 random numbers between 1 and 1000
numbers = []

for i in range(100):
    numbers.append(random.randint(1, 1000))

# Sort the list
numbers.sort()

print("Sorted list:")
print(numbers)

# Create even and odd lists
even = []
odd = []

# Separate even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

# Print lists
print("\nEven numbers:")
print(even)

print("\nOdd numbers:")
print(odd)