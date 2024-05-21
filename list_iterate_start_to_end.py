#iterate through given a list from start to end 

# input
# list=[4,5,6,7,8,9]
# start=1
# end=4
# output=[5,6,7]


n = list(map(int, input().split()))
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

def iterate(n,start,end):
    if start<0 or start>=end:
        return
    print(n[start])
    iterate(n,start+1,end)  

iterate(n,start,end)