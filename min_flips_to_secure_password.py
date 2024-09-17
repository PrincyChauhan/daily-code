def min_flips_to_secure_password(pwd):
    n=len(pwd)
    if n%2!=0:
        return -1
    total_flips=0
    for i in range(0,n,2):
        first_char=pwd[i]
        print(first_char,"first_char......")
        second_char=pwd[i+1]
        print(second_char,"second_char......")
        
        if first_char!=second_char:
            total_flips+=1
    return total_flips

pwd="1110011000"    
print(min_flips_to_secure_password(pwd))   