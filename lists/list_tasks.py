# List manipulation
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(l, command, location, value=0):
    if command is "remove":
        if location is "end":
            return l.pop()
        else:
            return l.pop(0)
    else:
        if location is "end":
            l.append(value)
            return l
        else:
            l.insert(0, value)
            return l


# Palindrome
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(word):
    letters = [letter for letter in word if letter is not " "]
    new_word = "".join(letters)
    return new_word == new_word[::-1]


# Frequency
'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(term_list, search_term):
    return term_list.count(search_term)


# Capitalize
'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(word):
    return "{}{}".format(word[0].upper(), word[1:])


# Callback
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(li, fn):
    truthy = [x for x in li if fn(x)]
    falsy = [x for x in li if not fn(x)]
    
    return [truthy, falsy]
