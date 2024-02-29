import numpy as np


matrix = np.array([[2, 3], [7, 11]])
vector = np.array([[5], [13]])

print('A = (matrix)')

determinant = np.linalg.det(matrix)
print(f'det(A) = {determinant}')
inverse = np.linalg.inv(matrix)
print(f'A^-1 = {inverse}')

solution = np.linalg.solve(inverse, vector)
print(f'x = {solution}')

fast_solution = np.linalg.solve(matrix, vector)
print(f'x = {fast_solution}')