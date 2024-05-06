'''This plots the given raw data with the fitted curve.'''

'''__i.stypla__'''

import numpy as np
import matplotlib.pyplot as plt



def plot_data_and_fit(data, fit_curve, data_format = 'x', fit_format = '--'):
  
  '''This function plots the data and the fit curve.'''
  
  plt.figure()
  data_points = plt.plot(data[0], data[1], data_format, label='Data Points')
  fit_line = plt.plot(fit_curve[0], fit_curve[1], fit_format, label='Fit Line')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.legend()
  plt.show()
  next
  return data_points, fit_line
  
'''test'''

# Givin data the fit_curve
data = [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
fit_curve = [np.linspace(-2, 2), np.linspace(-2,2)**2]

# Plot the data and fit curve
combined_plot= plot_data_and_fit(data, fit_curve, data_format= 'x', fit_format='--')

print(combined_plot)

if __name__ == "__main__":
  main()
