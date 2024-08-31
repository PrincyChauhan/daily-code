def min(arr):
    minElement=float('inf')
    for i in range(len(arr)):
        if arr[i]<minElement:
            minElement=arr[i]
    return minElement

arr=[2,1,4,0,7]
res=min(arr)
print("minimum element in the array is:",res)        