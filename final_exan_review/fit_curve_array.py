'''This modual will give N points on a curve that corresponds to the'''
'''quadradic equation given by a, b & c value.'''

'''__i.stypla__'''

import numpy as np
import matplotlib.pyplot as plt
import sys as sys


def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points = 100):
  '''This module will give N points on a curve that corresponds to the'''
  '''quadradic equation given by a, b & c value and the min & max of the data set.'''
  
  a = quadratic_coefficients[2]
  b = quadratic_coefficients[1]
  c = quadratic_coefficients[0]
  
  print(minimum_x, maximum_x, number_of_points)
  
  # this will take the min & max of the data set and give N points on a curve
  try:
    
    t = np.linspace(minimum_x,maximum_x,num=number_of_points) 
    x1 = []
    y1 = []
    for k in t:
      x = k
      y = c + (b*x) + (a*(x**2))
      x1.append(x)
      y1.append(y)
    
    fit_curve = np.array([x1, y1])
    #plt.plot(fit_curve[0], fit_curve[1])
    #plt.show()
    #print(fitted_curve)
    return fit_curve
  
  except IOError:
    print("the min value is greater than the max value")

'''test'''
pass_data = [0,0,1]

test = fit_curve_array(pass_data, -2, 2)
print(test)

if __name__ == "__main__":
  main()
