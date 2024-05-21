# repeat each character by the number specified immediately after it

# input=a3b4c2
# output=aaabbbbcc


n=input("Enter the string: ")
output=""

for char in n:
    if char.isalpha():
        var=char
    else:
        num=int(char)
        output+=(var*num) 
print(output)           
