
ODD = {
    1: 'one',
    3: 'three',
    5: 'five',
    7: 'seven',
    9: 'nine'
}

print("Keys:", ODD.keys())

print("Values:", ODD.values())

print("Items:", ODD.items())

print("Length of the dictionary:", len(ODD))

if 7 in ODD:
    print("7 is present in the dictionary")
else:
    print("7 is not present in the dictionary")

if 2 in ODD:
    print("2 is present in the dictionary")
else:
    print("2 is not present in the dictionary")

value = ODD.get(9, "Key not found")
print("Value corresponding to the key 9:", value)

if 9 in ODD:
    del ODD[9]
    print("Item with key 9 deleted")
else:
    print("Key 9 not found in the dictionary")
print("Dictionary after deleting the key 9:", ODD)
