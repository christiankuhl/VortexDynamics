"""
This module implements the N-vortex dynamics for an ellipse.
Insert code here as if it were inside a class definition statement.
"""

import numpy as np
from scipy.special import ellipk
from scipy.optimize import newton
from mpmath import ellipfun
from cmath import asin
from utils import vectorized

def __init__(self, a):
    """
    Instantiates an ellipse with half axes a and 1.
    """
    self.a = a
    self.xlim = (-a, a)
    self.ylim = (-1, 1)
    self._k = self.solve_for_k()
    self._K = ellipk(self._k)
    print(self._k)

def JGradG(self, z1, z2):
    z1, z2 = complex(*z1), complex(*z2)
    fz, fw, fprimez = self.F(z1), self.F(z2), self.Fprime(z1)
    igradG = -1.j / (2 * np.pi) * (fprimez * np.conj(fw) * (1 - fz * np.conj(fw))
                                    / np.abs((1 - fz * np.conj(fw)))**2
                                    - (fprimez * (fz - fw)) / np.abs((fz - fw))**2)
    return np.array([np.real(igradG), np.imag(igradG)])

@vectorized
def JGradh(self, z):
    # z = complex(*z)
    f, fprime, f2prime = self.F(z), self.Fprime(z), self.F2prime(z)
    # f, fprime, f2prime = z, 1, 0
    jhprime = 1.j / (2 * np.pi) * (2 * f * fprime / (1 - np.abs(f)**2)
                                     + fprime * f2prime / (np.abs(fprime)**2))
    return np.array([np.real(jhprime), np.imag(jhprime)])

def plot_me(self, t):
    return np.array([self.a*np.cos(2*np.pi*t), np.sin(2*np.pi*t)])

# Main interface implemented above, lots of helper functions below this point

def solve_for_k(self):
    def rhs(k):
        c = 2/np.pi * np.arcsinh(2 * self.a / (self.a**2 - 1))
        return ellipk(np.sqrt(1 - k**2)) / ellipk(k) - c
    return newton(rhs, .5)

@vectorized
def W(self, z):
    return 2 * self._K / np.pi * asin(z / np.sqrt(self.a**2 - 1))

def h(self, z):
    return 1/(2*np.pi)*np.log((1-np.abs(self.F(z))**2)/np.abs(self.Fprime(z)))

def F(self, z):
    return np.sqrt(self._k) * self.snW(z)

def Fprime(self, z):
    cn, dn = self.cnW(z), self.dnW(z)
    return (2 * np.sqrt(self._k) * self._K / (np.pi * np.sqrt(self.a**2 - 1 - z**2))
            * cn * dn)

def F2prime(self, z):
    sn, cn, dn = self.snW(z), self.cnW(z), self.dnW(z)
    return 2*np.sqrt(self._k)*self._K/(np.pi*(self.a**2-1-z**2)**(3/2))*cn*dn*z-4*np.sqrt(self._k)*self._K**2/(np.pi**2*(self.a**2-1-z**2))*sn*(dn**2+self._k**2*cn**2)

@vectorized
def sn(self, z):
    return ellipfun('sn', z, self._k**2).__complex__()

@vectorized
def cn(self, z):
    return ellipfun('cn', z, self._k**2).__complex__()

@vectorized
def dn(self, z):
    return ellipfun('dn', z, self._k**2).__complex__()

@vectorized
def snW(self, z):
    return self.sn(self.W(z))

@vectorized
def cnW(self, z):
    return self.cn(self.W(z))

@vectorized
def dnW(self, z):
    return self.dn(self.W(z))
