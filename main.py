#!/usr/bin/python3.6

from domains import *
from dynamics import NVortexProblem
from plot import VortexPlot
from utils import star_configuration

if __name__ == '__main__':
    domain = Ellipse(1.2)
    # domain = UnitDisk()
    problem = NVortexProblem(domain, Tmax=10)
    app = VortexPlot(problem)
    x0, Gamma = ([1.0,0], [4])
    x0, Gamma = ([-1/4, 0,0,0, 1/4, 0], [1/4, -1/4, 1/4])
    x0, Gamma = star_configuration([1/4, 1/2, 3/4], [-3/2, 1, -1/2], 3, centralGamma=2)
    import matplotlib.pyplot as plt
    import numpy as np
    from utils import scatterList
    x = np.arange(-2.1, 2.1, 0.05)
    y = np.arange(-1.1, 1.1, 0.05)
    xx, yy = np.meshgrid(x, y, sparse=True)
    z = domain.h(xx + 1.j*yy)
    h = plt.contour(x,y,z, levels=np.arange(-2,2,.05))
    plt.clabel(h, inline=1, fontsize=6)
    # app.animate(x0, Gamma)
    # plt.figure()
    # plt.contour(x,y,z)
    plt.show()
