#  create a function that returns the average of the elements present in the 
def average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)  