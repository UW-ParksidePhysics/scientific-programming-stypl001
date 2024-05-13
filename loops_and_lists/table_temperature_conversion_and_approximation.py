from types import ClassMethodDescriptorType
import numpy as np

import math as m

fahrenheit = 0
subscript_a = '\u2090'

print("{:<8} {:<15} {:<15}".format("T(F)", "T(C)","T(C)" + subscript_a))


while fahrenheit <= 100:
  celsius = (fahrenheit - 32) * 5/9
  celsius_aproximat = (fahrenheit - 30) /2
  print("{:<8} {:<15} {:<15}".format(fahrenheit, round(celsius,2),round(celsius_aproximat,2)))
  fahrenheit += 10
