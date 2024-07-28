def add_binary(a: str, b: str):
    int_a = int(a, 2)
    int_b = int(b, 2)
    sum_int = int_a + int_b
    sum_bin = bin(sum_int)[2:]
    return sum_bin
print(add_binary("11", "1"))o
print(add_binary("1010", "1011")) 
