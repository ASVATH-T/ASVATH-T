def diagonal_difference(matrix):
    n = len(matrix)
    primary_diagonal = sum(matrix[i][i] for i in range(n))
    secondary_diagonal = sum(matrix[i][n-i-1] for i in range(n))
    return abs(primary_diagonal - secondary_diagonal)

if _name_ == "_main_":
    matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonal_difference(matrix))
