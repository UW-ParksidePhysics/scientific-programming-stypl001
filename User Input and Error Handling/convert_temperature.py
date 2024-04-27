import numpy as np
import sys
import math as m

def celsius_to_fahrenheit(celsius_temperature):
    return (9. / 5) * celsius_temperature + 32

def fahrenheit_to_celsius(fahrenheit_temperature):
    return (5. / 9) * (fahrenheit_temperature - 32)

def celsius_to_kelvin(celsius_temperature):
    return celsius_temperature + 273.15

def kelvin_to_celsius(kelvin_temperature):
    return kelvin_temperature - 273.15

def fahrenheit_to_kelvin(fahrenheit_temperature):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit_temperature))
  
def kelvin_to_fahrenheit(kelvin_temperature):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin_temperature))  

if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1] == 'test':
    test_all_functions()
