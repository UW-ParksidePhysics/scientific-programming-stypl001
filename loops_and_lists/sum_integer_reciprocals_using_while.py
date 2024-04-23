import numpy as np

import math as m

summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index <= maximum_index:
    summation += 1/index
    index += 1

print(f'(k = {starting_index}, {maximum_index}) 1/k = {summation}')


#indext is not within the loop, with this, it will cause an infinite loop.
#K(max) = 3 will return 1/1 + 1/2 + 1/3 = 1.8333333333333333
#k(max) = 100 will return 5.187377
