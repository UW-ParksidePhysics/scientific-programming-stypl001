import numpy as np
import matplotlib.pyplot as plt
import math as m
import sys

# initialized variables
# velocity of the launched cannon ball
v = 50 # m/s
# angle of launched cannon ball
theta = m.pi/6 # this is 30 degrees
# height of cannon ball launched over the horizon
h = 10  # METERS 

# g is the acceleration due to gravity on each of the planets listed in the array 'planet'
g = [3.7, 
     8.87, 
     9.81, 
     3.711, 
     23.1, 
     9.0, 
     8.7, 
     11.0]

# planet is the name of each of the planets listed in the array 'planet'
planet = ["Mercury", 
          "Venus", 
          "Earth", 
          "Mars", 
          "Jupiter", 
          "Saturn", 
          "Uranus", 
          "Neptune"]


t = np.linspace(0, 40, num=500) # Set time as 'continous' parameter.

#This is for the graph of Height vs Disatance.
plt.figure(1)

for idx, grav_acc in enumerate(g): # Calculate trajectory for every plante
    x1 = []
    y1 = []
    for k in t:
        x = ((v*k)*np.cos(theta)) # this give the distance from the start.
        y = h + ((v*k)*np.sin(theta)) - ((0.5*grav_acc)*(k**2)) #this give how height the ball is at
        x1.append(x)
        y1.append(y)
    p = [i for i, j in enumerate(y1) if j < 0] # don't go below the x axis or floor
    for i in sorted(p, reverse = True):
        del x1[i]
        del y1[i]

    plt.plot(x1, y1, label=f"{planet[idx]}") # plot for every planet
    plt.title("Projectile Motion - Height vs Distance")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
plt.legend(loc = 2)

#This is for the graph of velocity vs time.
plt.figure(2)

for idx, grav_acc in enumerate(g): # calculate velocity for every plante
  x1 = []
  y1 = []

  t = int((v*np.sin(theta) + (v*np.sin(theta)**2 + 2*grav_acc*h)**0.5)/grav_acc)
  k = 0
  while k <= t:
      y = v*np.sin(theta) - (grav_acc*k) # this is the velocity at the time
      x = k # this is the time
      x1.append(x)
      y1.append(y)
      k += .01
  
  plt.plot(x1, y1, label=f"{planet[idx]}") # plot for every planet
  plt.title("Projectile Motion - Velocity vs Time")
  plt.xlabel("Time (sec)")
  plt.ylabel("Velocity (m/s)")
plt.legend(loc=2)

# This is to show the graph of Height vs Time.
plt.figure(3)

t = np.linspace(0,40,num=500) # set time as 'continous' parameter.

for idx, grav_acc in enumerate(g): # calculate trajectory for every plante
  x1 = []
  y1 = []
  for k in t:
      x = k
      y = h + ((v*k)*np.sin(theta))-((0.5*grav_acc)*(k**2)) #this gives the height of the ball at time k
      x1.append(x)
      y1.append(y)
  p = [i for i, j in enumerate(y1) if j < 0] # don't go below the x axis or floor
  for i in sorted(p, reverse = True):
      del x1[i]
      del y1[i]

  plt.plot(x1, y1, label=f"{planet[idx]}") # plot for every planet
  plt.title("Projectile Motion - Height vs Time")
  plt.xlabel("Time (sec)")
  plt.ylabel("Height (m)")
plt.legend(loc=2)
plt.show()


if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1] == 'test':
    test_all_functions()
