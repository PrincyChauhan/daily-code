# n=int(input("Enter a number: "))

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n * fact(n-1)

# result=fact(n)
# print(result)

def factorial(n):
    if n==0:
        return 1
    elif n<0:
        return -1
    else:
        return n * factorial(n-1)
    
print((factorial(5))) 
print((factorial(0)))
print((factorial(-5)))   