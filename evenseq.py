user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]
for num in num_list:
    if num % 2 == 0:
        print(num)
