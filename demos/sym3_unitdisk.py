from ..domains import *
from ..dynamics import NVortexProblem
from ..plot import VortexPlot
from ..utils import star_configuration

domain = UnitDisk()
problem = NVortexProblem(domain, Tmax=5)
app = VortexPlot(problem)

z0, Gamma = star_configuration([0.45889061, 0.79810972, 0.94462013], [-1/2, 1/3, -1/4], 3, centralGamma=2/3)

app.animate(z0, Gamma)
