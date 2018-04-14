numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
print(evens)

odds = [num for num in numbers if num % 2 == 1]
print(odds)


lc = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(lc)


nested = [['X' if num % 2 == 1 else 'O' for num in range(1, 4)] for val in range(1, 4)]
print(nested)
