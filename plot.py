#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils import star_configuration, scatterList
from dynamics import NVortexProblem

class VortexPlot(object):
    """
    Encapsulates a plot object for a given N-vortex problem
    """
    def __init__(self, problem=NVortexProblem()):
        """
        Create a plot object for the underlying N-vortex problem.
        """
        self.problem = problem
        self.domain = domain
        self.setup()

    def animate(self, z0, Gamma):
        """
        Animate the solution with initial state z0 and vortices Gamma.
        """
        self.solution = self.problem.HamiltonianSolution(z0, Gamma)
        self.scat = self.ax.scatter(scatterList(z0)[0],scatterList(z0)[1], c=Gamma)
        animation = FuncAnimation(self.fig, lambda n: self.scat.set_offsets(self.solution[n]),
                                                                    interval=1, frames=1000)
        plt.show()

    def setup(self):
        """
        Setup the plot area.
        """
        self.fig = plt.figure(figsize=(7, 7))
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        self.ax.set_xlim(-1, 1), self.ax.set_xticks([])
        self.ax.set_ylim(-1, 1), self.ax.set_yticks([])
        circ = plt.Circle((0, 0), radius=1, edgecolor='black', facecolor='None')
        self.ax.add_patch(circ)

if __name__ == '__main__':
    app = VortexPlot()
    x0, Gamma = star_configuration([1/4, 1/2, 3/4], [-3/2, 1, -1/2], 3, centralGamma=2)
    app.animate(x0, Gamma)
