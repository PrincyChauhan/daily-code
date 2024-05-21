# Write a python program to sort characters and numbers so that first alphabets and then numbers are displayed in the sorted order.
# Input: 'B4A1D3'
# Output: 'ABD134'

a=input("Enter the string: ")
alphabets=[]
numbers=[]

for ch in a:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)
print(sorted(alphabets))
print(sorted(numbers)) 

sorted_list=sorted(alphabets)+sorted(numbers)
print(sorted_list)

final_output=''.join(sorted_list)
print(final_output)

           