# create a list of 20 random integers between 1 and 10, generated using random library, and sort the list
import random
x=[random.randint(1,10)for i in range(20)]
x.sort()
print(x)