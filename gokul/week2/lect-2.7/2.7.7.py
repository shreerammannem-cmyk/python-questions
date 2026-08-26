# write a python code where you will take an input number k and a string s.
# you have to move the string by k characters to the right

# TestCase 1
'''
INPUT:
    s='abcdefg'
    k=2

OUTPUT: 'cdefghi`
'''

# TestCase 2
'''
INPUT:
    s='chennai'
    k=20
OUTPUT:
    'wbyhhuc'
'''
# doubt


alpha="abcdefghijklmnopqrstuvwxyz"
s='abcdefg'

t=''
k=2
i=0
print(alpha.index(s[0]))
t=t+(alpha[(((alpha.index(s[i]))+k)%26)])
t=t+(alpha[(((alpha.index(s[i+1]))+k)%26)]) 
t=t+(alpha[(((alpha.index(s[i+2]))+k)%26)]) 
t=t+(alpha[(((alpha.index(s[i+3]))+k)%26)]) 
t=t+(alpha[(((alpha.index(s[i+4]))+k)%26)]) 
t=t+(alpha[(((alpha.index(s[i+5]))+k)%26)]) 
t=t+(alpha[(((alpha.index(s[i+6]))+k)%26)]) 
print(t)