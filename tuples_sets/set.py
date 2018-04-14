cities = ["Radom", "Gdańsk", "Warszawa", "Gdańsk", "Poznań", "Gdańsk"]
print(f"Cities list length: {len(cities)}, list: {cities}")

cities_set = set(cities)
print(f"Cities set length: {len(cities_set)}, set: {cities_set}")
print()

# add, remove, discard, copy, clear
brother = {"Maciek"}
friend = brother.copy()
print(friend == brother)
print(friend is brother)
print()

friend.add("Mandżo")
friend.remove("Maciek")
friend.discard("Edzio")
print(friend)
friend.clear()
print(friend)
print("==========")

# union, intersection
math_class = {"Stan", "Piotr", "Mich3l", "Semen", "Martin"}
php_class = {"Stan", "Piotr", "Mich3l", "Mateusz"}

union = math_class | php_class
intersection = math_class & php_class

print(f"Math class: {math_class}")
print(f"Php class: {php_class}")

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print()

# set comprehension
hello = {letter for letter in "hello"}
print(hello)
