import numpy as np

import math as m

def compute_heaviside(x):
    """
    Compute the heaviside function.

    Parameters
    ----------
    x : float
        The value of x.

    Returns
    -------
    float
        The value of the heaviside function.

    """
    return 1 if x >= 0 else 0

# part b
print("{:<15} {:<15}".format("x","H(x)"))
print("{:<15} {:<15}".format("-10",compute_heaviside(-10)))
print("{:<15} {:<15}".format("-10-15", compute_heaviside(-10-15)))
print("{:<15} {:<15}".format("0", compute_heaviside(0)))
print("{:<15} {:<15}".format("10-15", compute_heaviside(10-15)))
print("{:<15} {:<15}".format("10", compute_heaviside(10)))
