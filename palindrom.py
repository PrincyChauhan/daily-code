# stri = "TAKE U FORWARD"

# rev_str=stri[::-1]
# if stri == rev_str:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")    


def isPalindrom(s):
    start,end=0,len(s)-1
    while start<=end:
        if s[start]!=s[end]:
            return "Not a Palindrom"
        start+=1
        end-=1
    return "It is a Palindrom"

given_string=input()
print(isPalindrom(given_string))