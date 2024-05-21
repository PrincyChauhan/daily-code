# finding pair of highest product

# input: [5,3,1,4,3,7,6,9,2]
# output: maximum product pair is (7,9) and their product is 63

def max_product(arr):
    # Ensure the array has at least two elements
    if len(arr) < 2:
        print("No pair exists as the array has less than two elements.")
        return

    # Sort the array
    arr.sort()

    # Find the maximum product of the two largest numbers
    max_product = arr[-1] * arr[-2]
    print("Maximum product pair is:", (arr[-1], arr[-2]), "and their product is:", max_product)

# Read input from the user
try:
    arr = eval(input("Enter an array: "))
    if not isinstance(arr, list):
        raise ValueError("Input is not a list")
    print("Array:", arr)
    max_product(arr)
except (SyntaxError, ValueError):
    print("Invalid input. Please enter a valid array of integers.")

