import numpy as np
import math

def star_configuration(r, Gamma, n, centralGamma=None):
    """
    Returns a "star-shaped" configuration of vortices in the following way:
    The vortices with strength Gamma_i are placed on the x-axis, with distance
    r_i to the origin and the whole configuration is rotated onto the n axes
    of a regular n-gon. If the parameter centralGamma is supplied, an additional
    vortex is placed at the origin with strength centralGamma.
    """
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
