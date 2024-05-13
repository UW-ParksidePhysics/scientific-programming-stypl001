'''Takes in a dat file and returns a 2D array of the data.'''

'''__i.stypla__'''

import numpy as np
import pandas as pd

def read_two_columns_text(filename):
  
  '''This will read in data from a file into a 2D array'''
  
  M = 0 #this is the number of data points in the table

  try:  
    #read table in and put headers x & y for the two cloumns
    data = pd.read_table(filename,header= None,names= ['x','y'])
    #find the number of records in the table
    M = data.shape[0]
    #print the table with the shapec of the table
    #print(f'{data=}, shape={data.shape}')
    
  except IOError:
    #if there is no file with the name in str then   print the error message
    print(f'File {filename} not found')

  return data, M

'''This is the test area'''

str = 'final_exam_review/volumes_energies.dat'
data, M = read_two_columns_text(str)

print(f'{data=}, shape={data.shape}')
if __name__ == "__main__":
  main()
