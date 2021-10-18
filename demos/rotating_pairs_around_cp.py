from math import pi
from domains import UnitDisk
from dynamics import NVortexProblem
from plot import VortexPlot
from utils import *

r = .664693523
eps = pi / 32
domain = UnitDisk()
problem = NVortexProblem(domain, Tmax=16)
app = VortexPlot(problem)
z, Gamma = star_configuration([r,-r], [.1, -.1], 3)
z1 = rotate(z, eps)
z2 = rotate(z, -eps)
z0 = list(z1) + list(z2)
Gamma = list(Gamma) + list(Gamma)
app.animate(z0, Gamma)
