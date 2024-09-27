def increasing_dec(arr):
    # Sort the array in increasing order
    arr.sort()
    print(arr, "-------arr--------")
    
    # Find the mid-point of the array
    mid = len(arr) // 2
    print(mid, "-----------mid-------")
    
    # Split the array into two halves
    first_half = arr[:mid]
    print(first_half, "-----------first_half-------")
        
    second_half = arr[mid:]
    print(second_half, "-----------second_half-------")
    
    # Reverse the second half for decreasing order
    rev_second_half = second_half[::-1]
    print(rev_second_half, "-----------rev_second_half-------")
    
    # Combine first half (increasing) and reversed second half (decreasing)
    result = first_half + rev_second_half
    print(result, "-----------result-------")
    return result
    
arr = [3, 1, 4, 7, 5, 2, 6]
print(increasing_dec(arr))
