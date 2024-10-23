def replace_below_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j] = 0
    return matrix

n = int(input("Enter the size of the matrix: "))
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = replace_below_diagonal(matrix)

for row in result:
    print(" ".join(map(str, row)))
