#!/usr/bin/python3.6

import numpy as np
from domains import *
from dynamics import NVortexProblem
from plot import VortexPlot
from utils import star_configuration

if __name__ == '__main__':
    domain = UnitDisk()
    problem = NVortexProblem(domain, Tmax=5)
    app = VortexPlot(problem)
    # x0, Gamma = ([0,3/4], [-1])
    # x0, Gamma = star_configuration([1/4, 1/2, 3/4], [-3/2, 1, -3/4], 3, centralGamma=2)
    # x0, Gamma = ([-1/5**(1/4),0,0,0,1/5**(1/4),0], [-1,1,-1])
    # x0, Gamma = ([-1/4, 0,0,0, 1/4, 0], [1/4, -1/4, 1/4])
    # sol = problem.GradientSolution(x0, Gamma)
    # z0 = sol[-1].flatten()
    # print(z0)
    z0, Gamma = star_configuration([0.45889061, 0.79810972, 0.94462013], [-1/2, 1/3, -1/4], 3, centralGamma=2/3)
    # print(z0)
    # epsilon = .02 * np.random.rand(len(z0))
    # epsilon = [-.02,0,0,0,.02,0]
    # z0 += epsilon
    # app.animate_gradient(x0, Gamma)
    app.animate(z0, Gamma)
