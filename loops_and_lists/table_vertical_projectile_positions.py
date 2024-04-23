import numpy as np

import math as m

# y(t) = v*t-0.5*g*t**2

# for the last point,  t = 2*v/g, y=0
v = 10.00 # the initial velocity is 10 m/s
n = 7 # the number of intervals
#g1 = 9.81 # this is the gravity on earth
#g2 = 3.711 # this is the gravity on mars
g1 = 9.81
g2 = 3.711  

# t = [0, 2*v/g]
tt1 = (2*v/g1) #total time in air for g1
tt2 = (2*v/g2) #total time in air for g2

t1 = tt1/(n+1) # time interval for g1
t2 = tt2/ (n+1)  #  time intervall for g2


# y(t) = v*t-0.5*g*t**2

print(f'For initial velovity of {v} m/s:')

print(f'Gliese 667 Cb (g = {g1} m/s/s) Cc (g = {g2} m/s/s)')

print("{:<8} {:<8} {:<8} {:<8} ".format("t(s)", "y(m)","t(s)","y(m)"))

print('using a for loop:')
s1 = 0
s2 = 0
for j in range(n+2):
  s1 = round(t1 * j, 3)
  s2 = round(t2 * j, 3)
  y1 = round(v*(t1*j)-0.5*g1*(t1 *j)**2,3)
  y2 = round(v*(t2*j)-0.5*g2*(t2 *j)**2,3)
  print("{:<8} {:<8} {:<8} {:<8} ".format(f"{s1}", f"{y1:.3f}", f"{s2}", f"{y2:.3f}"))
  
print('using a while loop:')

s1 = 0
s2 = 0
j = 0

while j < n+2:
  s1 = round(t1 * j, 3)
  s2 = round(t2 * j, 3)
  y1 = round(v*(t1*j)-0.5*g1*(t1 *j)**2,3)
  y2 = round(v*(t2*j)-0.5*g2*(t2 *j)**2,3)
  print("{:<8} {:<8} {:<8} {:<8} ".format(f"{s1}", f"{y1:.3f}", f"{s2}", f"{y2:.3f}"))
  j = j +1
