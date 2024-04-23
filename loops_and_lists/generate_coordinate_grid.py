import numpy as np

import math as m

# n = (value of max integer)
print('Enter 2 poitive integers')
a,b = int(input()),int(input())
n = int(input("Enter the number of intervals you want: "))

i = 1 # this is the starting point of all sums.

#list = [a,b]

h = round((b-a)/n,2)
n = n+1

print(f'For x  in [{a} , {b}] with {n} intervals, the interval length is h = {h}, and Using a for loop: ')
list_f = [a]

for i in range(1,n):
 list_f.append(a + round((i)*h,2))
  
print(list_f)

#This is the list comprehesion for the numbers.
print("Using list comprehension:")
list = [a+round(h*i,2) for i in range(n)]
print("x = ", list)

  # i = 0


