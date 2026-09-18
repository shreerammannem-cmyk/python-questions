## generate a list of 15 numbers random numbers from 1 to 15 and sort it
## print all the numbers from 1 to 15 , which are not in the generated list
import random

# Generate 15 random numbers from 1 to 15
numbers = []

for i in range(15):
    numbers.append(random.randint(1, 15))

# Sort the list
numbers.sort()

print("Generated list:")
print(numbers)

# Print numbers from 1 to 15 that are not in the list
print("Numbers not in the generated list:")

for i in range(1, 16):
    if i not in numbers:
        print(i)