even_odd_dict = {num: ("even" if num % 2 == 0 else "odd") for num in range(1,11)}
print(even_odd_dict)

stan = {"name": "Stan", "last_name": "DeePaQ", "city": "Gdańsk"}
big_stan = {(k.upper() if k is 'city' else k): v.upper() for k, v in stan.items()}
print(f"Stan: {stan}")
print(f"Big STAN: {big_stan}")


# Task 1: dict comprehension using 2 lists
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(3)}
print(answer)


# Task 2: 
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {el[0]: el[1] for el in person}
print(answer)


# Task 3:
answer = {}.fromkeys('aeiou', 0)
print(answer)


# Task 4:
answer = {i: chr(i) for i in range(65, 91)}
print(answer)


# Task 5:
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}
