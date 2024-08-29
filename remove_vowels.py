def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    res=""
    for char in input_string:
        if char not in vowels:
            res+=char
    return res

input_string = input("Enter a string: ")
output_string = remove_vowels(input_string)
print(output_string)
            