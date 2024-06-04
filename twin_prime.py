#twin_prime: diffrence between two prime numbers is 2

def isPrime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False 
    return True       


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if isPrime(num1) and isPrime(num2):
    if abs(num1-num2)==2:
        print("Twin Prime")
    else:
        print("Not a Twin Prime")
else:
    print("Not a Twin Prime")        
            