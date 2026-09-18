# create a function named `sub` that takes three parameters as input and  returns their the minimum difference among the three 
def sub(a, b, c):
    nums = sorted([a, b, c])
    return min(nums[1] - nums[0], nums[2] - nums[1])

def sub(a,b,c):
    nums=sorted([a,b,c])
    return min(nums[1]-nums[0],nums[2]-nums[1])




