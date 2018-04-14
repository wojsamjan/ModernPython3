print(all([0, 1, 2, 3]))
print(any([0, 1, 2, 3]))


def is_all_strings(iterable_object):
    return all(isinstance(x, str) for x in iterable_object)
