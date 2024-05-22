s="my23name43is"
# output="si23emna43ym"

x=list(s)
print("list:",x)

alpha_chars = [char for char in s if char.isalpha()]
print("alpha_chars:",alpha_chars)

alpha_chars.reverse()
print("reverse alpha_chars:",alpha_chars)

output=""
i=0
for char in s:
    if char.isalpha():
        output+=alpha_chars[i]
        i+=1
    else:
        output+=char
print("output:",output)


        