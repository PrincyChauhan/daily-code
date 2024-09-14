def diagonal_difference(matrix):
    n = len(matrix)
    
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]
    
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

difference = diagonal_difference(matrix)
print(difference)
