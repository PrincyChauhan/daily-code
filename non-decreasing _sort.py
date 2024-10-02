#  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
#  integers m and n,
#  representing the number of elements in nums1 and nums2 respectively.
#  Merge nums1 andnums2into a single array sorted in non-decreasing order.
#  The final sorted array should not be returned by the function, but instead be stored inside the array
#  nums1. To
#  accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
#  that should be
#  merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#  Example 1:
#  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#  Output: [1,2,2,3,5,6]
#  Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1


def merge(num1,m,num2,n):
    combined=num1[:m]+num2[:n]
    print(num1[:m],"--------num1")
    print(num2[:n],"--------num2")
    print(combined,"--------combined")
    combined.sort()
    for i in range(len(combined)):
        num1[i]=combined[i]


nums1 = [1, 2, 3, 0, 0, 0]  # Original array with extra space for nums2
m = 3                       # Number of valid elements in nums1
nums2 = [2, 5, 6]          # Second array
n = 3                       # Number of valid elements in nums2

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]        