# The cost of a stock on each day is given in an array, arr. An investor wants to buy the stocks in triplets such that the sum of the cost for three days is divisible by d. The goal is to find the number of distinct triplets (i, i, k) such that i < j < k and the sum (a[0] + a[j] + a[k]) is divisible by d. 

 

# Example Let arr, prices of stock = [3, 3, 4, 7, 8] and d = 5

 

# Following are the triplets whose sum is divisible by d (1-based indexing):

#  Triplet with indices-(1, 2, 3), sum = 3+3+4 which is equal to 10

 

#  • Triplet with indices-(1, 3, 5), sum = 3+4+8 which is equal to 15

#  • Triplet with indices -(2, 3, 4), sum = 3+4+8 which is equal to 15


 

#    Hence the answer is 3. 

# input :

# arr = [2  3  1  6]

# d = 3

 

# output :

# 2

 

# explanation : 

# triplet index (1,2,3) , sum = 2+3+1 = 6

# triplet index (1,3,4), sum = 2+1+6  = 9 


# hence ans is 2



def count_divisible_triplets(arr, d):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triplet_sum = arr[i] + arr[j] + arr[k]
                if triplet_sum % d == 0:
                    count += 1
    
    return count

arr = [3, 3, 4, 7, 8]
d = 5
print(count_divisible_triplets(arr, d))  # Output should be 3
           


