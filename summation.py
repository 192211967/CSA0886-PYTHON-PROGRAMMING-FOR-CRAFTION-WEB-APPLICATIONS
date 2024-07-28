file_path = 'C:/java/java/sum.txt'
total_sum = 0
with open(file_path, 'r') as file:
    for line in file:
        value = float(line.strip())
        total_sum += value
print(f"The total sum of values in the file is: {total_sum}")
