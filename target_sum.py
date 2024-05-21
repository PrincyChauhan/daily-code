# input
# nums=[2,7,11,15]
# target=9
# output=[0,1]


nums = list(map(int, input().split()))
target=int(input())
n=len(nums)
output=[]

for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target and len(output)==0:
            output.append(i)
            output.append(j)
print(output)            

