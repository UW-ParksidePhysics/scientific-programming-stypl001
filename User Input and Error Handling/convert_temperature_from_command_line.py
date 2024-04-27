import numpy as np
import sys 
import math as m

#I dont know how to get the command line to work in replit, so I just used the input function.

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
  return (9. / 5) * celsius_temperature + 32

def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
  return (5. / 9) * (fahrenheit_temperature - 32)

try:
    fahrenheit = float(input('Enter a temperature in Fahrenheit: '))
except ValueError:
    fahrenheit = float(input('You must enter a number!:'))
    print(f'{fahrenheit} Fahrenheit converts to {convert_fahrenheit_temperature_to_celsius(fahrenheit):.1f} celsius')

else:    
    print(f'{fahrenheit} Fahrenheit converts to {convert_fahrenheit_temperature_to_celsius(fahrenheit):.1f} celsius')

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
      test_all_functions()
