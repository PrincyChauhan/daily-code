n = int(input("Enter the number of terms:"))

first = 0
second = 1

if n <= 0:
    print("Enter a positive number")
elif n == 1:
    print("Fibonacci series up to", n, ":")
    print(first) 
else:
    print("Fibonacci series:")
    for i in range(n):
        print(first)
        temp = first + second
        first = second
        second = temp
