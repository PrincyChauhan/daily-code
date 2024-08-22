def first_rec_char(s):
    seen=set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

s="pythonprincy"
res=first_rec_char(s)
print(res)    