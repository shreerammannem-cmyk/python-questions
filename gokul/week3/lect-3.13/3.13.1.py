## write a code for the below test cases

# print until you find @ in the string, using break statement
# TestCase 1
INPUT="abcd@gmail.com"
# OUTPUT:
'''
a
b
c
d
'''
x="abcd@gmail.com"
for char in x:
    if char == '@':
        break
    print(char)
