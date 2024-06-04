# Converting String in Lowercase Without Using String Method 

str1="PrINcY"

upper_str=""

for ch in str1:
    asc=ord(ch)
    if asc>64 and asc<91:
        upper_str+=chr(asc+32)
    else:
        upper_str+=chr(asc)
print(upper_str)            