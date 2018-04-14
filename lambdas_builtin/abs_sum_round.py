print(abs(-2.87))
print(sum((1, 2, 3)))
print(round(3.87))
print(round(3.87, 1))


# returns max abs
def max_magnitude(nums):
    abs_nums = [abs(num) for num in nums]
    return max(abs_nums)


'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values
def sum_even_values(*args):
    return sum([x for x in args if x % 2 == 0])


'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

def sum_floats(*args):
    return sum([x for x in args if type(x) == float])
