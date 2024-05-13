
from math import pi  
from math import log

mass_s = 47 # Mass of a small egg in grams
mass_l = 67 # Mass of a large egg in grams
p = 1.038 # Density of eggs in g/cm^3
c = 3.7 # Specific heat of eggs in J/gK  
k = 0.0054  # Burning time constant in minutes W/(cm K)
Tw = 100 # Temperature of water in degrees C
Ty = 70 # Temperature of yolk in degrees C
Tf = 4 # Temperature of egg from a fridge in degrees C
Tr = 20 # Temperature of egg at room temp in degrees C

# this will do the small egg from the frigde 
t = ((mass_s**(2/3) * c * p**(1/3)) / (k * pi**2 * (4 * pi / 3)**(2/3)) ) *  log(.76 * (Tf - Tw) / (Ty - Tw))

print(f' Time for small egg from the frigde is {(t/60):3.2f} minutes')

# this will do the large egg from the frigde
t = ((mass_l**(2/3) * c * p**(1/3)) / (k * pi**2 * (4 * pi / 3)**(2/3)) ) *  log(.76 * (Tf - Tw) / (Ty - Tw))

print(f' Time for large egg from the frigde is {(t/60):3.2f} minutes')

# this will do the small egg from the room
t = ((mass_s**(2/3) * c * p**(1/3)) / (k * pi**2 * (4 * pi / 3)**(2/3)) ) *  log(.76 * (Tr - Tw) / (Ty - Tw))

print(f' Time for small egg from the room is {(t/60):3.2f} minutes')

# this will do the large egg from the room 
t = ((mass_l**(2/3) * c * p**(1/3)) / (k * pi**2 * (4 * pi / 3)**(2/3)) ) *  log(.76 * (Tr - Tw) / (Ty - Tw))

print(f' Time for small egg from room is {(t/60):3.2f} minutes')



                               
