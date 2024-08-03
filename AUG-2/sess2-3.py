import numpy as np
def longest_plateau(arr):
    arr = np.array(arr)
    mask = (arr[:-2] == arr[1:-1]) & (arr[1:-1] == arr[2:])
    if not mask.any():
        return -1, 0
    lengths = [np.sum(arr[start:] == arr[start]) for start in np.where(mask)[0] + 1]
    idx = np.where(mask)[0][np.argmax(lengths)]
    return idx, lengths[np.argmax(lengths)]
arr = [1, 2, 2, 2, 1, 4, 4, 4, 4, 3, 3]
print(longest_plateau(arr))
