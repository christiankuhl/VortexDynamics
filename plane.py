"""
This module implements the N-vortex dynamics for the Euclidean plane.
Insert code here as if it were inside a class definition statement
"""

import numpy as np
import math

def JGradG(self, z1, z2):
    """
    JGradG(z1, z2) is the product of the 2d symplectic matrix J with the gradient
    with respect to the first variable of the Green's function G of the negative
    Dirichlet Laplacian in the Euclidean plane.
    """
    x, y = z1
    u, v = z2
    norm2 = 2 * math.pi * (x - u)**2 + (y - v)**2
    return np.array([y-v, u-x])/norm2

def JGradh(self, z):
    """
    JGradh(z) is the product of the 2d symplectic matrix J with the gradient
    of the Robin's function of the Euclidean plane.
    """
    return np.array([0, 0])

def plot_me(self, t):
    """
    Obviously.
    """
    pass
