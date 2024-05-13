''' This will calculate the lowest eigenvectors of a matrix.'''

'''i.stypla'''

import numpy as np
import pandas as pd
#from pandas.core.internals.managers import #create_block_manager_from_column_arrays

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors = 3):
  '''this will calculate the lowest eigenvectors of a M x M matrix.'''

  eigenvectors = []
  eigenvalues = []

  eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
  
  idx= eigenvalues.argsort()
  eigenvalues = eigenvalues[idx]
  eigenvectors = eigenvectors[:,idx]
  eigenvectors_t = np.transpose(eigenvectors)
  
  
  return eigenvalues[number_of_eigenvectors] , eigenvectors_t[number_of_eigenvectors]





'''Test'''
if __name__ == "__main__":
# matrix [2, -1], [-1, 2]
  test_matrix = []  
  test_matrix = [[2, 2, 4], [1, 3, 5],[2, 3,4]]
  
  print(f'Min',calculate_lowest_eigenvectors(test_matrix, 0))



