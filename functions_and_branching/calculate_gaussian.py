import numpy as np

import math as m

def calculate_gaussian(x, mu, sigma):
    """
    Calculate the gaussian function.

    Parameters
    ----------
    x : float
        The value of x.
    mu : float
        The value of the mean.
    sigma : float
        The value of the standard deviation.

    Returns
    -------
    float
        The value of the gaussian function.

    """
    return 1 / (sigma * m.sqrt(2 * m.pi)) * m.exp(-(x - mu)**2 / (2 * sigma**2))

mu = 5
sigma = 2
n = 20
x = np.linspace(mu - 5*sigma, mu + 5*sigma , n)
print("{:<15} {:<15}".format("x", "f(x)"))
for i in range(len(x)):
  y = calculate_gaussian(x[i], mu, sigma)
  print("{:<15} {:<15}".format(f"{x[i]:.3f}", f"{y:.8f}"))
