"""
This module implements the N-vortex dynamics for an ellipse.
Insert code here as if it were inside a class definition statement.
"""

import numpy as np
import math
from scipy.special import ellipj, ellipk

def __init__(self, a):
    """
    Instantiates an ellipse with half axes a and 1.
    """
    self.a = a
    self.xlim = (-a, a)
    self.ylim = (-1, 1)
    self._k = self.solve_for_k()
    self._kprime = math.sqrt(1 - self._k**2)
    self._K = ellipk(self._k)

def JGradG(self, z1, z2):
    return np.array([0, 0])

def JGradh(self, z):
    return np.array([0, 0])

def plot_me(self, t):
    return np.array([self.a*math.cos(2*math.pi*t), math.sin(2*math.pi*t)])

# Main interface implemented above, lots of helper functions below this point

def solve_for_k(self):
    return 0

def W(self, z):
    return 2 * self._K / math.pi * np.arcsin(z / math.sqrt(a**2 - 1)))

def F(self, z):
    return math.sqrt(self._k) * self.elliptic_functions(z)[0]

def Fprime(self, z):
    _, cn, dn = self.elliptic_functions(z)
    return (2 * math.sqrt(self._k) * self._K / (math.pi * np.sqrt(a**2 - 1 - z**2))
            * cn * dn)

def elliptic_functions(self, z):
    # ellipj does not, in its original form, take complex arguments
    u, v = np.real(self.W(z)), np.imag(self.W(z))
    snu, cnu, dnu, _ = ellipj(u, self._k)
    snv, cnv, dnv, _ = ellipj(v, self._kprime)
    sn = (snu * dnv + 1.j * cnu * dnu * snv * cnv) / (1 - snu**2 * dnv**2)
    cn = (cnu * cnv - 1.j * snu * dnu * snv * dnv) / (1 - snu**2 * dnv**2)
    dn = (dnu * cnv * dnv - 1.j * self._k**2 * snu * cnu * snv) / (1 - snu**2 * dnv**2)
    return sn, cn, dn
