
# write a python script for the below test case,
# Note the input will be of 5 characters long,


# testcase 1
'''
INPUT : 'gokul'
OUTPUT : 'hplvm'
'''

# testcase 2
'''
INPUT: 'abcde'
OUTPUT: 'bcdef'
'''

# solution:
# doubt

alpha="abcdefghijklmnopqrstuvwxyz"
s='gokul'

t=''

i=0
print(alpha.index(s[0]))
t=t+(alpha[(((alpha.index(s[i]))+1)%26)])
t=t+(alpha[(((alpha.index(s[i+1]))+1)%26)]) 
t=t+(alpha[(((alpha.index(s[i+2]))+1)%26)]) 
t=t+(alpha[(((alpha.index(s[i+3]))+1)%26)]) 
t=t+(alpha[(((alpha.index(s[i+4]))+1)%26)]) 
print(t)