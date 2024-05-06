''' This will calculate the lowest eigenvectors of a matrix.'''

'''i.stypla'''

import numpy as np
import pandas as pd

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors = 3):
  '''this will calculate the lowest eigenvectors of a M x M matrix.'''
  
  eigenvectors = []
  eigenvalues = []
    
  eigenvectors = np.linalg.eigh(square_matrix)
  eigenvalues = np.linalg.eigvals(square_matrix)
   
  return eigenvalues, eigenvectors

'''Test'''
# matrix [2, -1], [-1, 2]
test_matrix = []  
test_matrix = [[2, -1], [-1, 2]]

print(calculate_lowest_eigenvectors(test_matrix, 2))

if __name__ == "__main__":
  main()
