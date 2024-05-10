''' This is the final script for the final exam. '''

''' author - i.stypla '''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

'''Part 1 of the Final Exam'''

from read_two_columns_text import read_two_columns_text 
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from equations_of_state import fit_eos


#from final_exam_review import calculate_lowest_eigenvectors                
M= 0
hope = 0
q_fit = []  
data = [[], []]
curve_fit = [[], []]
filename = 'final_exam/Pb.Fm-3m.GGA-PBE.volumes_energies.dat'
display_graph = True



def parse_file_name(txt):
#This function will parse the file name and return
  pfn1 = txt.split("/",2) #this splits the str at the first /
  pfn2 = pfn1[1].split(".",3) #this splits the str after the first / at the first .
   
  return pfn2[0], pfn2[1], pfn2[2]

chemical, crystal, density = parse_file_name(filename)

data = []
# read in the data
data, M = read_two_columns_text(filename)

bivariate_stats =[]

stats = calculate_bivariate_statistics(data)

data_min_x = stats[2]
data_max_x = stats[3]

fit_x_value =[]
fit_x_value = np.linspace(data_min_x, data_max_x, num=50) 

quadratic_coefficients = []

curve_fit = calculate_quadratic_fit(data)


eos_fit_curve_y, eos_parameters = fit_eos(data['x'], data['y'], curve_fit)

#this adds the volumes to the energies comeing from 'fit_eos' values.
eos_fit_curve = pd.DataFrame({'volume': fit_x_value, 'energies': eos_fit_curve_y})

#this takes that table and moves it into a dataframe to use in plot.
efc1 = (np.transpose(np.array(eos_fit_curve['volume'])))
efc2 = (np.transpose(np.array(eos_fit_curve['energies'])))
efc3 = (efc1, efc2)

#this takes that table and moves it into a dataframe to use in plot.
data1 = (np.transpose(np.array(data['x'])))
data2 = (np.transpose(np.array(data['y'])))
data3 = (data1, data2)

plt.figure(1)

print('test')
data_points = plt.plot(data3[0], data3[1], 'bo', label='Data Points')
fit_line = plt.plot(efc3[0], efc3[1], 'k-', label='Fit Line')
# This will give an extra 10% of the range of the y valus to the graph.

y_min = min(data3[1]) - (max(data3[1]) - min(data3[1])) * 0.1
y_max = max(data3[1]) + (max(data3[1]) - min(data3[1])) * 0.1
x_min = min(data3[0]) - (max(data3[0]) - min(data3[0])) * 0.1
x_max = max(data3[0]) + (max(data3[0]) - min(data3[0])) * 0.1 

plt.xlabel(r"\mathrm{Volume}\ ($\AA^3$/atom)")
plt.ylabel(r"\mathrm{Energie}\ (eV/atom)")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#this signs the graph with the students name and ISO 8601 date.
iso_date = dt.now()
iso_date1 = iso_date.strftime("%Y-%m-%d")
plt.text(.75, .25,'Created by Isabelle Stypla {iso_date1}')

#this creates the title of the graph.
plt.title(f'Birch-Murnaghan Equation of State for {chemical} in DFT')
#this is the saved file name
savefile_name =(f'Stypla.{chemical}.{crystal}.Birch-MumaghanEquationOfState.png')

if display_graph == False:
  plt.savefig(savefile_name)
  
else:
  
  plt.show()



''' Part 2 of Final Exam'''

from generate_matrix import generate_matrix
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors

#when testing the 'generate_matrix' function, after the matrix was generated, there was a host of errors in the graphing.


dimension_number = 170
parameters = 4
x_range = [data_min_x,data_max_x]
potential_name = 'square'

g_matrix = generate_matrix(x_range[0], x_range[1], dimension_number, potential_name, parameters)


set_3= calculate_lowest_eigenvectors(g_matrix, 3)
set_4= calculate_lowest_eigenvectors(g_matrix, 4)
set_5= calculate_lowest_eigenvectors(g_matrix, 5)

spatial_pt = np.linspace(-10,10,(dimension_number)) # set time as 'continous' parameter.
spatial_pt = np.array(spatial_pt)

plt.figure(2)
plt.xlabel(r"x[a.u]")
plt.ylabel(r"\Psi\(x)[a.u.]")

plt.title(f'Seleceted Wavefunctions for a {potential_name}  Potential on a Spatial Grid of {dimension_number} Points')

savefile_name_2 =(f'Stypla.{chemical}.{potential_name}.png')

if display_graph == False:
  plt.savefig(savefile_name_2)
 
else:
 
  plt.show()
