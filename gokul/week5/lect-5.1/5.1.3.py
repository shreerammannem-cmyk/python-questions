# create a function discount that takes two arguments cost and d 'discount percentage' as input,and it should return the cost after reducing the discounted price from the original price

# Test cases
# ip : discount(100,50)
# op : 50

# ip : discount(200,20)
# op: 160
def discount(cost, d):
    final_cost = cost - (cost * d / 100)
    return int(final_cost) if final_cost.is_integer() else final_cost


# Test cases
print(discount(100, 50))  # 50
print(discount(200, 20))  # 160
