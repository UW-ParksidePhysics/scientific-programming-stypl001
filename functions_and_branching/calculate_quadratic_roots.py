import numpy as np

import math as m

def calculate_quadratic_roots(a,b,c):
  # calculating discriminant using formula
  dis = b * b - 4 * a * c 
  sqrt_val = m.sqrt(abs(dis)) 

  # checking condition for discriminant
  if dis > 0: 
      # real and different 
      if a == 1:
        print(f' x^2 + {b}x + {c} = 0: x = {(-b + sqrt_val)/(2 * a)}, {(-b - sqrt_val)/(2 * a)}; calculate_quadratic_roots(1, {b}, {c}) = {(-b + sqrt_val)/(2 * a)}, {(-b - sqrt_val)/(2 * a)}')
      else:
        print(f' {a}x^2 + {b}x + {c} = 0: x = {(-b + sqrt_val)/(2 * a)}, {(-b - sqrt_val)/(2 * a)};; calculate_quadratic_roots({a}, {b}, {c}) = {(-b + sqrt_val)/(2 * a)}, {(-b - sqrt_val)/(2 * a)}')
        
  elif dis == 0: 
      #single roots
      print("real and same roots") 
      if a == 1:
        print(f' x^2 + {b}x + {c} = 0: x = {(-b)/(2 * a)}; calculate_quadratic_roots(1, {b}, {c}) = {(-b)/(2 * a)}')
      else:
        print(f' {a}x^2 + {b}x + {c} = 0: x = {(-b)/(2 * a)}; calculate_quadratic_roots({a}, {b}, {c}) = {(-b )/(2 * a)}')

  # when discriminant is less than 0
  else:
      # Complex roots
      print("Complex Roots") 
      if a == 1:
        print(f' x^2 + {b}x + {c} = 0: x = i, -i ; calculate_quadratic_roots(1, {b}, {c}) = 1j, -1j')
      else:
        print(f' {a}x^2 + {b}x + {c} = 0: x = i, -i ; calculate_quadratic_roots({a}, {b}, {c}) = 1j, -1j')
      
   

# Test single root
a = 1
b = 0
c = 1
#print(f' {a} x^2 + {b} x + {c} = 0')
calculate_quadratic_roots(a,b,c)
calculate_quadratic_roots(1,-2,-3)
calculate_quadratic_roots(1,0,1)
