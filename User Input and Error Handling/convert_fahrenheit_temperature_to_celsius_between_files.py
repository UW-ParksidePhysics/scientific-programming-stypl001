import numpy as np
import sys
import math as m

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
  return (9. / 5) * celsius_temperature + 32

def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
  return round((5. / 9) * (fahrenheit_temperature - 32),1)

temp_list = []

with open('input_and_error_handling/Test2.txt', 'r') as f:
  lines_after_3 = f.readlines()[3:]
  for line in lines_after_3:
    temp = line.split()
    z, y, temp1 = temp[0], temp[1], temp[2]
        
    print(f'{temp1} Fahrenheit converts to {convert_fahrenheit_temperature_to_celsius(float(temp1)):.1f} celsius')
    
    temp_list.append([float(temp1), convert_fahrenheit_temperature_to_celsius(float(temp1))])


outfile = open('input_and_error_handling/Temp_3.txt', 'w')
for row in temp_list:
  outfile.write(str(row) + '\n')
outfile.close()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
      test_all_functions()
