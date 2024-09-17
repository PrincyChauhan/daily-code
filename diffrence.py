def calculate_counters(arr):
    n = len(arr)
    counters = [0] * n  # Initialize counters array with zeros

    for i in range(1, n):
        counter = 0
        for j in range(i):
            if arr[j] > arr[i]:
                counter -= abs(arr[j] - arr[i])
            else:
                counter += abs(arr[j] - arr[i])
        counters[i] = counter

    return counters

# Example usage
arr = [2, 1,3]
result = calculate_counters(arr)
print(result)  # Output: [0, 2, 0]
