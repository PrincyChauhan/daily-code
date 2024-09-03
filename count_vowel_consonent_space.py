def count_charater(s):
    space=0
    vowels=0
    consonants=0
    for char in s:
        if char.lower() in "aeiou":
            vowel+=1
        elif char.isalpha():
            consonants+=1
        elif char.isspace():
            space+=1
    return space,vowels,consonants

input_string=input("Enter a string: ")
space,vowels,consonants=count_charater(input_string)    
print("Space: ",space)
print("Vowels: ",vowels)
print("Consonants: ",consonants)            
            