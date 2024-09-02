# Given an array that contains both negative and positive integer
# find the maximum product subarray


def maxProduct(nums):
    max_product=float('-inf')
    for i in range(len(nums)):
        product=1
        for j in range(i,len(nums)):
            product*=nums[j]
            max_product=max(max_product,product)
    return max_product

nums = [1,2,-3,0,-4,-5]
print(maxProduct(nums))