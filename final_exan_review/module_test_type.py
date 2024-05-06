'''This tests the type of the module.'''

'''i.stypla'''

import numpy as np
import pandas as pd

modules = ['read_two_columns_text', 
           'calculate_bivariate_statistics', 
           'calculate_quadratic_fit', 
           'fit_curve_array', 
           'plot_data_with_fit', 
           'calculate_lowest_eigenvectors', 
           'annotate_plot']

for module in modules:
    with open(module+'.py') as module_file:
        exec(module_file.read())

if __name__ == "__main__":
  main()

