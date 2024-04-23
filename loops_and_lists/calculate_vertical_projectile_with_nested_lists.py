import numpy as np

import math as m

#time_positions = [0]
#time_positions = [1]
# y(t) = v*t-0.5*g*t**2

# for the last point,  t = 2*v/g, y=0
v = 10.00 # the initial velocity is 10 m/s
n = 7 # the number of intervals
#g1 = 9.81 # this is the gravity on earth

g1 = 9.81


time_positions = []

# t = [0, 2*v/g]
tt1 = (2*v/g1) #total time in air for g1


t1 = tt1/(n+1) # time interval for g1



# y(t) = v*t-0.5*g*t**2

print(f'For initial velovity of {v} m/s:')

print(f'Gliese 667 Cb (g = {g1} m/s/s) ')

print("{:<8} {:<8}".format("t(s)", "y(m)"))

print('using a for loop:')
s1 = 0

for i in range(n+2):
  time_positions.append([])
  for j in range(4):
    s1 = round(t1 * i, 2)
    y1 = round(v*(t1*i)-0.5*g1*(t1 *i)**2,2)
    time_positions[i].append([s1, y1])
    
for item in time_positions:
  print("{:<8} {:<8}".format(item[0][0], item[0][1]))
  
