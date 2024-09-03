# Write a program to remove brackets from an algebraic expression. 
# input="a+((b-c)+d)"
# output="a+b-c+d"

def solve(s):
    res=""
    for c in s:
        if c=="(" or c ==")":
            continue
        res+=c
    return res

input_string=input()
print(solve(input_string))    
    