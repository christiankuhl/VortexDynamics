import numpy as np
from math import pi, sqrt
from itertools import tee
from scipy.integrate import odeint

def JGradG(z1, z2):
    x, y = z1
    u, v = z2
    xnorm = x**2 + y**2
    if u == 0 and v == 0 and 0 < xnorm < 1:
        return np.array([-y / (2 * pi * xnorm), x / (2 * pi * xnorm)])
    else:
        unorm = u**2 + v**2
        prod = x * u + y * v
        gx = (unorm - 1) * (unorm * x + (1 - 2 * v * y) * x + u * (-1 - x**2 + y**2))
        gy = (unorm - 1) * (unorm * y + (1 - 2 * u * x) * y + v * (-1 + x**2 - y**2))
        denominator = 2 * pi * (unorm + xnorm - 2 * prod) * (1 - 2 * prod + unorm * xnorm)
        return np.array([gy, -gx])/denominator

def JGradh(z):
    x, y = z
    if x == 0 and y == 0:
        return np.array([0, 0])
    else:
        xnorm = x**2 + y**2
        return np.array([y / (pi * (xnorm - 1)), -x / (pi * (xnorm - 1))])

def RHS(z, Gamma):
    z = zip(*[iter(z)]*2)
    z = list(enumerate(zip(z, Gamma)))
    return np.array([Gamma_j * JGradh(z_j)  + 2 * sum(Gamma_i * JGradG(z_j, z_i)
                                 for (i, (z_i, Gamma_i)) in z if i != j)
                                 for (j, (z_j, Gamma_j)) in z]).flatten()

def scatterList(z):
    k = int(len(z)/2)
    return [z[2*j] for j in range(k)], [z[2*j+1] for j in range(k)]

def HamiltonianSolution(z0, Gamma, Tmax=10, eps=.01):
    N = int(Tmax / eps)
    t = [eps * tau for tau in range(N+1)]
    f = lambda z, t: RHS(z, Gamma=Gamma)
    sol = odeint(f, z0, t)
    return [np.transpose(scatterList(s)) for s in sol]
    
