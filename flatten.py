import numpy as np

def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return np.array(flat_list)

# Example usage
nested_list = [[1,2,3] ,[4, 5,6]]
flattened_list = flatten_list(nested_list)
print(flattened_list)  # Output: [1 2 3 4 5 6]
