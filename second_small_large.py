# input =[1,2,4,7,7,5]
# output= smallest :2, largest:7

arr=list(map(int,input().split()))
n=len(arr)
arr.sort()
if n<2:
    print("-1")
else:
    print(f"smallest:{arr[1]}, largest:{arr[n-2]}")