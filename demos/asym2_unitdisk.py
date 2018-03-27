#!/usr/bin/python3.6

import numpy as np
from domains import UnitDisk
from dynamics import NVortexProblem
from plot import VortexPlot

if __name__ == '__main__':
    domain = UnitDisk()
    problem = NVortexProblem(domain, Tmax=5)
    x0, Gamma = [-1/2,0,1/3,0], [-3, 6]
    sol = problem.GradientSolution(x0, Gamma)
    z0 = sol[-1].flatten()
    problem2 = NVortexProblem(domain, Tmax=30)
    app = VortexPlot(problem2)
    z0 += 0.02 * np.random.randn(len(z0))
    app.animate(z0, Gamma)
