user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]
for num in num_list:
   maxi= max(num_list)
   mini= min(num_list)
print(maxi)
print(mini)
