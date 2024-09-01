# arr=[1,1,2,2,2,3,3]
# my_set=set(arr)
# s = list(my_set)
# a=len(s)
# print(a)

def solution(arr,N):
    unique=[]
    for i in range(N):
        if arr[i] not in unique:
            unique.append(arr[i])
    print(unique)  
arr=[4,4,1,1,3,3,2,2,2]
N=len(arr)
solution(arr,N)          