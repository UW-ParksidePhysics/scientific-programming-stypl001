from math import pi 

air_density = 1.2 # density of air in kg/m^3
a = 11  # radius of soccer ball in cm
ball_mass = .43 # mass of the soccer ball in KG
gravitational_acceleration = 9.81 # force of gravity m/s^2
drag_coefficient = .2  # drag coefficient
cross_area = pi * a**2
ball_velocity = 33.33 # m/s

drag_force = (1/2) * drag_coefficient * air_density  * cross_area * ball_velocity**2

gravitational_force = ball_mass * gravitational_acceleration

#print(f' The air denisty is {air_density} kg/m^3')
#print(f' The radius of the ball is {a} cm')
#print(f' The mass of the ball is {ball_mass} kg')
#print(f' The gravitational acceleration is {gravitational_acceleration} m/s^2')
#print(f' The drag coefficient is {drag_coefficient}')
#print(f' The cross area of the ball is {cross_area:.3f} cm^2')

print(f' The ball velocity is {ball_velocity} m/s')

print(f' The drag force is {drag_force:.2f} N')
print(f' The gravitational force is {gravitational_force:.2f} N')
print(f'  ')

ball_velocity = 2.78 # m/s

drag_force = (1/2) * drag_coefficient * air_density  * cross_area * ball_velocity**2

print(f' The ball velocity is {ball_velocity} m/s')

print(f' The drag force is {drag_force:.2f} N')
print(f' The gravitational force is {gravitational_force:.2f} N')
