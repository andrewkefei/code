N = 3

import numpy as np

matrix = [[0 for _ in range(N)] for _ in range(N)]
print(matrix)

row = 0
col = N // 2

matrix[row][col] = 1

for i in range(2, N ** 2 + 1):
    row = (row - 1) % N
    col = (col + 1) % N
    if matrix[row][col] != 0:
        row = (row + 2) % N
        col = (col - 1) % N
    matrix[row][col] = i

print(np.array(matrix))
