n=int(input())
term=10

sum_of_multiple=0

for i in range(1,term+1):
    multiple = n * i
    print(multiple,"----multiple------")
    sum_of_multiple += multiple
print(sum_of_multiple,"----sum_of_multiples------")