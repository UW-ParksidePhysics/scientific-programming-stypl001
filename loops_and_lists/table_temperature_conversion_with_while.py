import numpy as np

import math as m

fahrenheit = 0
superscript_o = '\u2070'

print("{:<8} {:<15}".format(superscript_o + "F", superscript_o +"C"))

while fahrenheit <= 100:
  celsius = (fahrenheit - 32) * 5/9
  print("{:<8} {:<15}".format(fahrenheit, round(celsius,2)))
  fahrenheit += 10
  

  
