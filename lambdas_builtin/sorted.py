users = [
	{"name": "Stan", "age": 24},
	{"name": "Mari", "age": 22},
	{"name": "Mart", "age": 26}
]

sorted_users = sorted(users, key=lambda u: u["age"], reverse=True)

print(f"Users: {users}")
print(f"Sorted users: {sorted_users}")


nums = [1, 5, 3, 7, 0]
print(f"sorted(nums): {sorted(nums)}")
print(f"nums: {nums}")

nums.sort()
print(f"nums.sort(): {nums}")
print(f"nums: {nums}")
