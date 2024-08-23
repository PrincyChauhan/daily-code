def largest_word_in_string(s):
    return max(s.split(), key=len)

s=(input("Enter a string: "))
print(largest_word_in_string(s))