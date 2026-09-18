## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
# after sorting, print the smallest, second smallest, largest and second largest number in the list
x=[]
for i in range(10):
    import random
    x.append(random.randint(1,100))
print(x)
x.sort()
print(x)
print("Smallest number in the list is: ",x[0])                      
print("Second smallest number in the list is: ",x[1])
print("Largest number in the list is: ",x[-1])
print("Second largest number in the list is: ",x[-2])