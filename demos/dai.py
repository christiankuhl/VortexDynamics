import numpy as np
from domains import UnitDisk
from dynamics import NVortexProblem
from plot import VortexPlot
from utils import *

r = 1/8
domain = UnitDisk()
problem = NVortexProblem(domain, Tmax=12)
app = VortexPlot(problem)
z0, Gamma = star_configuration([r], [.01], 6)
app.animate(z0, Gamma)
