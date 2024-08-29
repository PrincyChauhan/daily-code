def replace_zeros_with_ones(n):
    str_n=str(n)
    for char in str_n:
        if char=="0":
            str_n=str_n.replace(char,"1")
        else:
            continue 
    return int(str_n)        
    


n=int(input())
print(replace_zeros_with_ones(n))    