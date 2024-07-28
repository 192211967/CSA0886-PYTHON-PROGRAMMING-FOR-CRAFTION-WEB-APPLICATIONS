def hamming_distance(x, y):
    xor_result = x ^ y
    distance = 0
    while xor_result:
        distance += xor_result & 1
        xor_result >>= 1
    return distance
print(hamming_distance(1, 4))
print(hamming_distance(3, 1)) 