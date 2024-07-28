def find_max_consecutive_ones(nums):
    max_consecutive = 0
    current_consecutive = 0
    
    for num in nums:
        if num == 1:
            current_consecutive += 1
        else:
            max_consecutive = max(max_consecutive, current_consecutive)
            current_consecutive = 0
    
    # Final check to account for the case when array ends with 1's
    max_consecutive = max(max_consecutive, current_consecutive)
    
    return max_consecutive

# Test Cases
print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1])) # Output: 3
print(find_max_consecutive_ones([1, 0, 1, 1]))