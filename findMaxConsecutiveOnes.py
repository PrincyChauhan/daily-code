def findMaxConsecutiveOnes(nums):
    count=0
    maxi=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            count=0
        maxi=max(maxi,count)
    return maxi

nums=list(map(int,input().split()))
print(findMaxConsecutiveOnes(nums))           