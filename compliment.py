def find(num):
    length = num.bit_length()
    bitmask = (1 <<length) - 1
    print(bitmask)
    complement = num ^ bitmask
    return complement
print(find(5))  
print(find(1))  