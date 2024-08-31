# given an integer we need to find the sum of values of that table 

# input=10
# output=550
# explaination=1*10+2*10+3*10+4*10+5*10+6*10+7*10+8*10+9*10+10*10=550

n=int(input())
max_sum=0
for i in range(1,n+1):
    max_sum+=i*n
    print(max_sum,"---------max_sum------")
print(max_sum)    