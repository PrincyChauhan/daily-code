# Given an array and a integer K
# we need to find the maximum element in each of contigous subarray
# input 2 4 7 1 6 3
# k=3
# output 7 7 7 6


arr=list(map(int,input().split()))
k=int(input())

n=len(arr)

res=[]

for i in range(n-k+1):
    subarr=arr[i:i+k]
    print(subarr,"----subarr------")
    
    max_val=max(subarr)
    print(max_val,"----max_val------")
    
    res.append(max_val)
print(res,"----res------")