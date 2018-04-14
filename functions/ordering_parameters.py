# parameters, *args, default parameters, **kwargs
def display_info(a, b, *args, name="Stan", **kwargs):
	return [a, b, args, name, kwargs]


# a - 1
# b - 2
# args - (3,)
# name - "Stan"
# kwargs - {"last_name": "DeePaQ", "age": 24}

print(display_info(1, 2, 3, last_name="DeePaQ", age=24))
