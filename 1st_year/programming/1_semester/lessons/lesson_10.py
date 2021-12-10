import numpy as np

# a = np.arange(1, 10).reshape(3, 3) ** 2
# a_inv = np.linalg.inv(a)

# print(np.dot(a, a_inv))

n = int(input())
matrix = np.zeros((n + 1) ** 2).reshape(n + 1, n + 1)
for i in range(n + 1):
    matrix[i][0] = 1
    for j in range(i):
        matrix[i][j + 1] = matrix[i][j] * (j - i) / (j + 1)

print(matrix)

