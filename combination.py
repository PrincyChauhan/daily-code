# given an integer n and an integer k, return all possible combinations of k numbers out of 1 ... n.
# for exmaple: if n=3 and k=2


from itertools import combinations

def genrate_comination(n,k):
    numbers=range(1,n+1)
    result=list(combinations(numbers,k))
    return result

n=3
k=2
result=genrate_comination(n,k)
print(result)