from math import pi
from math import exp

m = 0
s = 2
x = 1

f1 = (1/(s*(2*pi)**0.5)) * exp((-.5) * ((x-m)/s)**2)  

print(f' The mean is {m}' )
print(f' The standard deviation is {s}' )
print(f' The input value of x is {x}')
print(f' Output value of f(x) is {f1:.3f}')
