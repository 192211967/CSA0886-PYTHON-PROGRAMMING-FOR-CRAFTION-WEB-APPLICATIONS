def print_sequence(sequence):
    numbers = sequence.split()
    for number in numbers:
        print(number, end=" ")
    print()
print(print_sequence("5 10 15 20 25"))
print(print_sequence("1 2 3"))

