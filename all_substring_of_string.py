str="hello"
n=len(str)
subs=[]

for i in range(0,n):
    for j in range(i+1,n+1):
        subs.append(str[i:j])
print(subs)        