users = [
	{"name": "Piotr", "age": 29},
	{"name": "Wojtek", "age": 24}
]

users_over_25 = list(filter(lambda u: u["age"] > 25, users))
print(users_over_25)

names_over_25 = list(map(lambda u: u["name"], filter(lambda u: u["age"] > 25, users)))
print(names_over_25)

names_over_25 = [u["name"] for u in users if u["age"] > 25]
print(names_over_25)


'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(nums):
    return list(map(lambda x: x * 3, filter(lambda num: num % 4 == 0, nums)))
