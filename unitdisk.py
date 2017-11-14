"""
This module implements the N-vortex dynamics for the unit disk.
Insert code here as if it were inside a class definition statement
"""

import numpy as np
from utils import vectorized

def JGradG(self, z1, z2):
    """
    JGradG(z1, z2) is the product of the 2d symplectic matrix J with the gradient
    with respect to the first variable of the Green's function G of the negative
    Dirichlet Laplacian in the unit disk.
    """
    x, y = z1
    u, v = z2
    xnorm = x**2 + y**2
    if u == 0 and v == 0 and 0 < xnorm < 1:
        return np.array([-y / (2 * np.pi * xnorm), x / (2 * np.pi * xnorm)])
    else:
        unorm = u**2 + v**2
        prod = x * u + y * v
        gx = (unorm - 1) * (unorm * x + (1 - 2 * v * y) * x + u * (-1 - x**2 + y**2))
        gy = (unorm - 1) * (unorm * y + (1 - 2 * u * x) * y + v * (-1 + x**2 - y**2))
        denominator = 2 * np.pi * (unorm + xnorm - 2 * prod) * (1 - 2 * prod + unorm * xnorm)
        return np.array([gy, -gx])/denominator

def JGradh(self, z):
    """
    JGradh(z) is the product of the 2d symplectic matrix J with the gradient
    of the Robin's function of the unit disk.
    """
    x, y = z
    if x == 0 and y == 0:
        return np.array([0, 0])
    else:
        xnorm = x**2 + y**2
        return np.array([y / (np.pi * (xnorm - 1)), -x / (np.pi * (xnorm - 1))])

def plot_me(self, t):
    """
    Provides a parametrisation of the domain's boundary on the interval [0, 1]
    """
    return np.array([np.cos(2*np.pi*t), np.sin(2*np.pi*t)])

@vectorized
def h(self, z):
    return 1/(2*np.pi)*np.log(1-np.abs(z)**2)
