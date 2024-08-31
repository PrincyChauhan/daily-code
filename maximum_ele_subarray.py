# given an array and a integer k. we need to find maximum element in each of contiguous subarray of size k.

# input=2 4 7 1 6 3
# k=3
# output=7776

arr=list(map(int,input().split()))
k=int(input())
n=len(arr)

ans=[]
for i in range(n - k + 1):
    subarray=arr[i:i+k]
    max_element = max(subarray)
    ans.append(max_element)

# Convert the list to a string to print the output as required
output = ''.join(map(str, ans))
print(output)
