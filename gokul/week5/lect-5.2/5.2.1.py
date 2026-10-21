'''
create three functions that take a list as input 
1) to return the first element of the list
2) to return the last element of the list
3) to return the sum of values returned from the above two functions 
'''

def get_first(lst):
    return lst[0]
def get_last(lst):
    return lst[-1]
def sum_first_and_last(lst):
    return get_first(lst)and get_last(lst)


x=[5,20,10,15,20]
print(get_first(x))
print(get_last(x))
print(sum_first_and_last(x))