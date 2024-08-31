# given two ingteger , find sum of cubes all number in the range of two given number.

# input n=4 m=9
# output 1989

m,n =map(int,input().split())

def find_cube_sum(m,n):
    sum=0
    for i in range(m,n+1):
        sum+=i**3
    print(sum)  
find_cube_sum(m,n)      