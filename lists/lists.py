# append, extend, insert
nums = [1, 2, 2, 3, 4, 5, 5, 6]

nums.append(6)
nums.extend([7, 8])
nums.insert(0, 0)  # where, what

print(nums)


# pop, remove, clear
nums.pop()
nums.pop(0)
nums.remove(2)
nums.remove(5)

print(nums)

nums.clear()

print(nums)


# index, count
names = ['Stan', 'DeePaQ', 'Yashi', 'Stan', 'Yashimoto']
stan_index = names.index('Stan')  # 0
print(f'names.index(\'Stan\'): {stan_index}')
stan_index = names.index('Stan', 1)  # 3
print(f'names.index(\'Stan, 1\'): {stan_index}')
# print(names.index('Stan', 1, 2))  # ValueError

stan_count = names.count('Stan')
print(f'Stan count: {stan_count}')


# sort, reverse, join
numbers = [6, 2, 4, 3]
numbers.sort()
numbers.reverse()

print(numbers)

names_string = ', '.join(names)
print(names_string)


# swapping values
stan = ['Stan', 'DeePaQ']
stan[0], stan[1] = stan[1], stan[0]
print(f'After swapping: {stan}')
