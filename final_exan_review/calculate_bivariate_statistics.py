'''This file contains the function calculate_bivariate_statistics.'''

'''__i.stypla__'''

import numpy as np
import pandas as pd


def calculate_bivariate_statistics(data):
  '''This function takes in a 2D array and returns a list of the mean, '''
  '''standard deviation & min/max of both x & y variables.'''
  
  if data.shape[0] >= 2 and data.shape[1] > 1:
    print(data.shape)
    statistics = []
    mean_y = data['y'].mean()
    std_dev_y = data['y'].std()
    min_x = data['x'].min()
    max_x = data['x'].max()
    min_y = data['y'].min()
    max_y = data['y'].max()
  
    statistics = [mean_y, std_dev_y, min_x, max_x, min_y, max_y]
  else:
    print('Data file does not have the correct dimentions.')
  
  return statistics
    
'''Test'''
  
#Set x as 'continous' parameter between -10 and 10 with 21 intervalls.
k = np.linspace(-10, 10, num=21) 
x= []
y= []
for t in k:
  print(t, t**2)
  x.append(t)
  y.append(t**2)
data = np.array([x,y])


print(calculate_bivariate_statistics(data))

if __name__ == "__main__":
  main()
