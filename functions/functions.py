def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def make(x, y, fn=add):  # default parameter
	return fn(x, y)


result = make(x=4, y=2)  # keyword arguments
print(result)
