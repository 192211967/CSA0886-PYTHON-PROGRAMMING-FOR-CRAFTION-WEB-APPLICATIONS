def remove_consecutive_duplicates(sequence):
    if not sequence:
        return []

    result = [sequence[0]]
    for num in sequence[1:]:
        if num != result[-1]:
            result.append(num)

    return result


# Example usage
sequence = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2]
filtered_sequence = remove_consecutive_duplicates(sequence)
print(filtered_sequence)
