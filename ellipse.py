"""
This module implements the N-vortex dynamics for an ellipse.
Insert code here as if it were inside a class definition statement.
"""

import numpy as np
import math

def __init__(self, a):
    """
    Instantiates an ellipse with half axes a and 1.
    """
    self.a = a
    self.xlim = (-a, a)
    self.ylim = (-1, 1)

def JGradG(self, z1, z2):
    return np.array([0, 0])

def JGradh(self, z):
    return np.array([0, 0])

def plot_me(self, t):
    return np.array([self.a*math.cos(2*math.pi*t), math.sin(2*math.pi*t)])
