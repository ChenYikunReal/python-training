dict1 = {'A': 'a', 'B': 'b', 'C': 'c'}
# {'a': 'A', 'b': 'B', 'c': 'C'}
dict2 = {y: x for x, y in dict1.items()}
print(dict2)
