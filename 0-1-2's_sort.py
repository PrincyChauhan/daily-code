n=int(input())
arr = list(map(int, input().split()))

zeros=[]
onces=[]
twos=[]

for i in range(len(arr)):
    if arr[i]==0:
        zeros.append(arr[i])
    elif arr[i]==1:
        onces.append(arr[i])
    else:
        twos.append(arr[i])
print(zeros+onces+twos)        
