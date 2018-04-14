names = ["Stan", "DeePaQ", "Yashimoto"]

max_length = max(len(name) for name in names)
max_name = max(names, key=lambda n: len(n))

print(f"max_length: {max_length}")
print(f"max_name: {max_name}")
