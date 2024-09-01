# arr=[1,2,3,4,5]
# k=2
# output=[3,4,5,1,2]

def rotate_by_k(arr,k):
    n=len(arr)
    ans=[0]*n
    for i in range(n):
        ans[i]=arr[(i+k)%n]
    return (ans) 
   
arr=[1,2,3,4,5]
k=2 
print(rotate_by_k(arr,k))
