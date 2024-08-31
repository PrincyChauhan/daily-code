# find a subarray with given  sum in array .
# given integer array find sub aaray with given sum in it.

# input=arr=[3,4,-7,1,3,3,1,-4]
# target=7

# output=[3,1,3],[1,3,3],[3,4]


arr=list(map(int,input().split()))
n=len(arr)
target=int(input())

for i in range(n):
    curr_sum=0
    for j in range(i,n):
        curr_sum+=arr[j]
        if curr_sum==target:
            print(arr[i:j+1])
    