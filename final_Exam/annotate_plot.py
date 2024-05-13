'''anotate_plot.py'''

'''i.stypla'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def annotate_plot(annotations, position, alignment, fontsize):
  '''This function will add annotations to a plot.'''

  plt.annotate(annotations,
               position[0],
               position[1],
               aligment[0],
               aligment[1],
               fontsize)




if __name__ == "__main__":
  word = 'Pb'
  pos_ition[] = [xy=(10, 10), xycorords='figure pixels']
  aligment = "horizontalalignment='left'"
  font_size = 40

  data = [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
  fit_curve = [np.linspace(-2, 2), np.linspace(-2,2)**2]
  data_points = plt.plot(data[0], data[1], 'bo', label='Data Points')
  fit_line = plt.plot(fit_curve[0], fit_curve[1], 'k-', label='Fit Line')
 
  plt.annotate('figure fraction',
  xy=(.025, .975), xycoords='figure fraction',
  horizontalalignment='left', verticalalignment='top',
  fontsize=20)

  #(word, pos_ition, aligment, font_size)
  plt.show()
