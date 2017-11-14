#!/usr/bin/python3.6

from domains import *
from dynamics import NVortexProblem
from plot import VortexPlot
from utils import star_configuration

if __name__ == '__main__':
    # domain = Ellipse(2)
    domain = UnitDisk()
    problem = NVortexProblem(domain, Tmax=50)
    app = VortexPlot(problem)
    # x0, Gamma = ([0,3/4], [4])
    x0, Gamma = ([-1/4, 0,0,0, 1/4, 0], [1/4, -1/4, 1/4])
    # x0, Gamma = star_configuration([1/4, 1/2, 3/4], [-3/2, 1, -1/2], 3, centralGamma=2)
    app.animate_gradient(x0, Gamma)
