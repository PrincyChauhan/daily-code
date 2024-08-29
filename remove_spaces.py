def remove_spaces(input_string):
    res=""
    for char in input_string:
        if char != " ":
            res+=char
    return res

input_string = input("Enter a string: ")
output_string=remove_spaces(input_string)
print(output_string)        