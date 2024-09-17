def odd_even_transform(arr,n):
    if n % 2==0:
        return arr 
    transform_arr=[]
    for num in arr:
        if num % 2 ==0:
            transform_arr.append(num-3)
        else:
            transform_arr.append(num+3)
            
    return transform_arr

arr=[3,4,9]  
n=3          
print(odd_even_transform(arr,n))