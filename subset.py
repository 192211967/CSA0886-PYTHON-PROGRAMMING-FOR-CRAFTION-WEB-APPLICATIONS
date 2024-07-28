def subsets(nums):
    result = [[]]
    
    for num in nums:
        result += [curr + [num] for curr in result]
    
    return result

# Test Case 1
nums1 = [1, 2, 3]
print(subsets(nums1))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Test Case 2
nums2 = [0]
print(subsets(nums2))
# Output: [[], [0]]
