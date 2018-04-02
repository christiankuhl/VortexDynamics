import numpy as np
import math
from functools import wraps
from itertools import chain, combinations, tee

def star_configuration(r, Gamma, axes, centralGamma=None):
    """
    Returns a "star-shaped" configuration of vortices in the following way:
    The vortices with strength Gamma_i are placed on the x-axis, with distance
    r_i to the origin and the whole configuration is rotated onto the n axes
    of a regular n-gon. If the parameter centralGamma is supplied, an additional
    vortex is placed at the origin with strength centralGamma.
    """
    n = axes
    Gamma = np.array(list(Gamma)*n)
    x0 = np.array([[rho*math.cos(k*2*math.pi/n), rho*math.sin(k*2*math.pi/n)]
                                    for k in range(n) for rho in r]).flatten()
    if centralGamma:
        x0 = np.append(x0, [0, 0])
        Gamma = np.append(Gamma, [centralGamma])
    return x0, Gamma

def scatterList(z):
    """
    scatterList reshapes the solution vector z of the N-vortex ODE for easy 2d plotting.
    """
    k = int(len(z)/2)
    return [z[2*j] for j in range(k)], [z[2*j+1] for j in range(k)]

def vectorized(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        def stripped_f(*args, **kwargs):
            return f(self, *args, **kwargs)
        ufunc = np.vectorize(stripped_f)
        return ufunc(*args, **kwargs)
    return wrapper

def symplectic(i, j):
    if i % 2 == 1:
        if i == j + 1:
            return 1
    else:
        if i == j - 1:
            return -1
    return 0

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(2,len(s)+1))
