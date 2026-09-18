## write a python code to print the maximum element of the list, using for loop


l = [1, 44, 22, 11, 23, 36, 49, 28, 31, 8, 54, 54]

# Initialize the maximum tracker with the first element of the list
max_element = l[0]

# Loop through the list to compare each number
for i in l:
    if i > max_element:
        max_element = i

# Print the final result
print(max_element)
