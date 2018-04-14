import sys


list_comp = sys.getsizeof([x * x for x in range(1000)])
gen_exp = sys.getsizeof(x * x for x in range(1000))

print(f"List comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")
