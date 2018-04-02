import numpy as np
from domains import UnitDisk
from dynamics import NVortexProblem
from plot import VortexPlot
from utils import *

domain = UnitDisk()
problem = NVortexProblem(domain, Tmax=5)
app = VortexPlot(problem)
z0, Gamma = star_configuration(r=[0.45889061, 0.79810972, 0.94462013],
                               Gamma=[-1/2, 1/3, -1/4],
                               axes=3,
                               centralGamma=2/3)
app.animate(z0, Gamma)
