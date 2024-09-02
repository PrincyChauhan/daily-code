def symmetric_pair(arr):
    symmetric_arr=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
           if arr[i][0]==arr[j][1] and arr[i][1]==arr[j][0]:
               symmetric_arr.append(arr[i])
    return symmetric_arr

arr = [(1, 2), (3, 4), (2, 1), (5, 6), (4, 3)]
print(symmetric_pair(arr))