#!/usr/bin/python3.6

import numpy as np
from domains import UnitDisk
from dynamics import NVortexProblem
from plot import VortexPlot
from utils import star_configuration

if __name__ == '__main__':
    domain = UnitDisk()
    problem = NVortexProblem(domain, Tmax=16)
    x0, Gamma = star_configuration([-1/8], [.1], 3)
    x1, Gamma1 = star_configuration([-1/8], [-.1], 3)
    x1 = np.array([x1[j:j+2] @ [[1/2, -1/2*np.sqrt(3)], [1/2*np.sqrt(3), 1/2]] for j in range(0, len(x1), 2)]).flatten()

    z0 = list(x0) + list(x1)
    Gamma = list(Gamma) + list(Gamma1)
    app = VortexPlot(problem)
    app.animate(z0, Gamma)
