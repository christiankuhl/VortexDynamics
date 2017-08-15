"""
This module implements the N-vortex dynamics for an ellipse.
Insert code here as if it were inside a class definition statement.
"""

import numpy as np
import math
from scipy.special import ellipj, ellipk
from scipy.optimize import newton

def __init__(self, a):
    """
    Instantiates an ellipse with half axes a and 1.
    """
    self.a = a
    self.xlim = (-a, a)
    self.ylim = (-1, 1)
    self._k = self.solve_for_k()
    self._kprime = np.sqrt(1 - self._k**2)
    self._K = ellipk(self._k)

def JGradG(self, z1, z2):
    fz, fw, fprimez = self.F(z), self.F(w), self.Fprime(z)
    igradG = 1.j / (2 * math.pi) * (fprimez * np.conj(fw) * (1 - fz * np.conj(fw))
                                    / np.abs((1 - fz * np.conj(fw)))**2
                                    - (fprimez * (fz - fw)) / np.abs((fz - fw))**2)
    return np.array([np.real(igradG), np.imag(igradG)])

def JGradh(self, z):
    f, fprime, f2prime = self.F(z), self.Fprime(z), self.F2prime(z)
    hprime = -1.j / (2 * math.pi) * (2 * f * fprime / (1 - np.abs(f)**2)
                                     + fprime * f2prime / (np.abs(fprime)**2))
    return np.array([np.real(hprime), np.imag(hprime)])

def plot_me(self, t):
    return np.array([self.a*math.cos(2*math.pi*t), math.sin(2*math.pi*t)])

# Main interface implemented above, lots of helper functions below this point

def solve_for_k(self):
    def rhs(k):
        c = 2/math.pi * np.arcsinh(2 * self.a / (self.a**2 - 1))
        return ellipk(np.sqrt(1 - k**2)) / ellipk(k) - c
    self._k = newton(rhs, .5)

def W(self, z):
    return 2 * self._K / math.pi * np.arcsin(z / np.sqrt(a**2 - 1))

def F(self, z):
    return np.sqrt(self._k) * self.elliptic_functions(z)[0]

def Fprime(self, z):
    _, cn, dn = self.elliptic_functions(z)
    return (2 * np.sqrt(self._k) * self._K / (math.pi * np.sqrt(a**2 - 1 - z**2))
            * cn * dn)

def F2prime(self, z):
    _, cn, dn = self.elliptic_functions(z)
    return ((z / (a**2 -1 - z**2) - 4 * self._K / (math.pi * np.sqrt(a**2 - 1 - z**2))
            * dn) * self.Fprime(z) - 4 * np.sqrt(self._k) * (self._k + 1) * self._K**2
            / (math.pi**2 * (a**2 - 1 - z**2)) * cn)

def elliptic_functions(self, z):
    # ellipj does not, in its original form, take complex arguments
    u, v = np.real(self.W(z)), np.imag(self.W(z))
    snu, cnu, dnu, _ = ellipj(u, self._k)
    snv, cnv, dnv, _ = ellipj(v, self._kprime)
    sn = (snu * dnv + 1.j * cnu * dnu * snv * cnv) / (1 - snu**2 * dnv**2)
    cn = (cnu * cnv - 1.j * snu * dnu * snv * dnv) / (1 - snu**2 * dnv**2)
    dn = (dnu * cnv * dnv - 1.j * self._k**2 * snu * cnu * snv) / (1 - snu**2 * dnv**2)
    return sn, cn, dn
