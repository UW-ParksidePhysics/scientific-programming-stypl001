'''Takes in a 2D array and returns a list of the coefficients of the quadratic fit.'''

'''__i.stypla__'''

import numpy as np

def calculate_quadratic_fit(data):
  '''This function takes in a 2D array and returns a list'''
  '''of the coefficients c, b, & a of the quadratic fit.'''
  x_values = data[0] # x values
  y_values = data[1] # y values
  quadratic_coefficients = []
  # create the x & y array for quadratic fitting
  x = np.array(x_values)
  y = np.array(y_values)
  # this does the best fitting of the data to a quadratic function
  a, b, c = np.polyfit(x, y, 2)
 
  quadratic_coefficients = [c, b, a]
  
  return quadratic_coefficients


'''test'''
pass_data = [np.linspace(-1, 1), np.linspace(-1, 1)**2]
pass_data = np.array(pass_data)
print(calculate_quadratic_fit(pass_data))



if __name__ == "__main__":
  main()
