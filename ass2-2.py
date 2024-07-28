def find_number(lst, key):
    try:
        position = lst.index(key)
        return position
    except ValueError:
        return "The key is not available in the list"
lst1 = [1, 7, 12, 56, 77]
key1 = 7
print(find_number([1, 7, 12, 56, 77], 7))

lst2 = [1, 7, 12, 56, 77]
key2 = 77
print(find_number([1, 7, 12, 56,77], 77))
