# Write a python code for complement of number
# input:5
# output:2

n=int(input())
binary_num=bin(n)
print("Binary number is:",binary_num)

binary_num=binary_num[2:]
print("After removing 0b:",binary_num)


flipped_binary=""
for bit in binary_num:
    if bit=="1":
        flipped_binary+="0"
    else:
        flipped_binary+="1"    


# Convert the flipped binary string back to a decimal integer
flipped_decimal = int(flipped_binary, 2)
print(flipped_decimal)