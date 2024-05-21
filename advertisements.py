# An e-commerce site has a series of advertisements to display. Links to the ads are stored in a data structure and they are displayed or not based on the value at a bit position in a number. The sequence of ads being displayed at this time can be represented as a binary value, where 1 means the ad is displayed and 0 means it is hidden. The ads should rotate, so on the next page load, ads that are displayed now are hidden and vice versa.

# Given a base 10 integer representing the current display state of all ads, determine its binary representation. Starting from the position of its highest order 1 bit, negate that bit and all lower order bits from 0 to 1 or from 1 to 0. Return the base 10 representation of the result.

# Input
# The first line of input consists of a single integer n
#  the base 10 integer. (1≤n≤105)
# .

# Output
# The output should consist of a single integer −
#  the answer.

# Examples
# input
# 50 - binary 110010 that means in 1st page  ads 1,2,5 are displayed 
# and negate each bit in sequence to get 001101=13 that means in 2nd page ads 3,4,6 are displayed
# output
# 13
# input
# 100
# output
# 27



def change(num):
    # Convert the integer to its binary representation without the '0b' prefix
    binary_n = bin(num)[2:]

    # Flip the bits in the binary representation
    flipped_binary = ""
    for bit in binary_n:
        if bit == "1":
            flipped_binary += "0"
        else:
            flipped_binary += "1"

    # Convert the flipped binary string back to a decimal integer
    flipped_decimal = int(flipped_binary, 2)
    return flipped_decimal

# Read input
try:
    n = int(input().strip())
    # Get the flipped value
    result = change(n)
    # Print the result
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
