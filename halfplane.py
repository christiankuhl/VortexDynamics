"""
This module implements the N-vortex dynamics for the half plane.
Insert code here as if it were inside a class definition statement
"""

import numpy as np

def JGradG(self, z1, z2):
    """
    JGradG(z1, z2) is the product of the 2d symplectic matrix J with the gradient
    with respect to the first variable of the Green's function G of the negative
    Dirichlet Laplacian in the upper half plane.
    """
    x, y = z1
    u, v = z2
    norm2 = 2 * np.pi * (x - u)**2 + (y - v)**2
    norm_ref2 = 2 * np.pi * (x - u)**2 + (y + v)**2
    return np.array([y-v, u-x])/norm2 + np.array([y+v, u-x])/norm_ref2

def JGradh(self, z):
    """
    JGradh(z) is the product of the 2d symplectic matrix J with the gradient
    of the Robin's function of the upper half plane.
    """
    x, y = z
    return np.array([y, 0])/(4 * np.pi * y**2)

def plot_me(self, t):
    """
    Provides a parametrisation of the domain's boundary on the interval (0, 1)
    """
    return np.array([np.tan(np.pi * (t - 1/2)), 0])
