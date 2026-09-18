# create a list of 20 random integers between 1 and 10, generated using random library
import random

random_list = [random.randint(1, 10) for _ in range(20)]
print(random_list)
