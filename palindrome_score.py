# Coding Question:

# Given a string str, find the score of str as per the following rules 

# 1) For each palindrome of length 4 in str, add 5 to the score
# 2) For each palindrome of length 5 in str, add 10 to the score
# 3)Palindromes can overtap withing str but must not be circular(i.e they
#     may not wrap around the end of the string)

# Notes:
    
#        - The score is initially 0
#        - There are no whitespaces in the String

def is_palindron(s):
    return s==s[::-1]

def calculate_score(s):
    score=0
    n=len(s)
    for i in range(n-3):
        if is_palindron(s[i:i+4]):
            score+=5
    for i in range(n-4):
        if is_palindron(s[i:i+5]):
            score+=10
    return score                
s = "abccbaabcdeedcba"
print(calculate_score(s))