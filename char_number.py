# input: aaaabbbccd
# output: 4a3b2c1d   

str1="aaaabbbccd"
count=0
output=""
char=str1[0]

for ch in str1:
    if ch==char:
        count+=1
    else:
        output+=str(count)+char
        char=ch
        count=1
output+=str(count)+char
print(output)            