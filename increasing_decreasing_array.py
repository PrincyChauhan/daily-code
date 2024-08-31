def solve(arr):
    arr.sort()
    n=len(arr)
    for i in range(n//2):
        print(arr[i],end=" ")
   
    for j in range(n-1,n//2-1,-1):
       print(arr[j],end=" ") 
       
arr=list(map(int,input().split()))
solve(arr)         
        