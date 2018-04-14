names = [
	{"name": "Stan", "age": 24},
	{"name": "Maci", "age": 24}
]

first_names = list(map(lambda x: x["name"], names))
print(first_names)
