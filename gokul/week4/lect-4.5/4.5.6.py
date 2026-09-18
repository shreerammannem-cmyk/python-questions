# create a python code to sort the list using while loop
l = [9, 3, 7, 1, 6, 3, 4]
i = 0

while i < len(l) - 1:
    if l[i] > l[i + 1]:
        l[i], l[i + 1] = l[i + 1], l[i]
        i = 0  # Restart the loop from the beginning after a swap
    else:
        i += 1  # Move to the next item if already in order

print(l)
