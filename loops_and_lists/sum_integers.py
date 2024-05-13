import numpy as np

import math as m

# n = (value of max integer)

n = int(input("Enter a positive integer: "))

i = 1 # this is the starting point of all sums.

sum_integers = 0
for i in range(1, n+1):
  sum_integers = sum_integers + i

print("The sum of all integers from 1 to", n, "is", sum_integers)

print("The Sum Formula (n(n+1)/2) is ", (n*(n+1)/2))
