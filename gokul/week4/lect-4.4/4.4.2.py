## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
## findout the index of number 21 in the generated list, if the number is not present in the list print -1
import random

x = []
for i in range(1000):
    x.append(random.randint(1,1000))
x.sort()

if 21 in x:
    index = x.index(21)
else:
    index = -1

print(index)

