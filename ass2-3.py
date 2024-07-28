def swap_numbers(nums1, nums2):
    nums1, nums2 = nums2, nums1
    print(f"After swap: ")
    return nums1, nums2

nums1, nums2 = 5, 10
print(swap_numbers(nums1, nums2))

nums1, nums2 = -4, -9
print(swap_numbers(nums1, nums2))
