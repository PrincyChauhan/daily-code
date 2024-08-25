# Problem Statement –

# Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.

# Constrains-

# 1<=N<=100

# Example 1:

# Input :

# 10  -> Integer

# Output :

# 5    -> result- Integer

# Explanation:

# Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.

n=int(input())

binary_rep=bin(n)[2:]
print(binary_rep,"........binary_rep......")
flip_binary=''

for bit in binary_rep:
    if bit=='1':
        flip_binary+='0'
    else:
        flip_binary+='1'
result=int(flip_binary,2)
print(result)        