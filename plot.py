#!/usr/bin/python3.6

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
        self.setup()

    def _animate(self, z0, Gamma, solution):
        """
        Animate 'solution' with dots of colour 'Gamma' and initial position 'z0'
        """
        scat = self.ax.scatter(*scatterList(z0), c=Gamma)
        framenumber = len(solution) - 1
        animation = FuncAnimation(self.fig, lambda n: scat.set_offsets(solution[n]),
                                                interval=1, frames=framenumber)
        plt.show()

    def animate(self, z0, Gamma):
        """
        Animate the (Hamiltonian) solution with initial state z0 and vortices Gamma.
        """
        solution = self.problem.HamiltonianSolution(z0, Gamma)
        self._animate(z0, Gamma, solution)

    def animate_gradient(self, z0, Gamma):
        """
        Animate the gradient solution with initial state z0 and vortices Gamma.
        """
        solution = self.problem.GradientSolution(z0, Gamma)
        self._animate(z0, Gamma, solution)

    def setup(self):
        """
        Setup the plot area.
        """
        domain = self.problem.domain
        self.fig = plt.figure(figsize=(7, 7))
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        self.ax.set_xlim(*domain.xlim), self.ax.set_xticks([])
        self.ax.set_ylim(*domain.ylim), self.ax.set_yticks([])
        plt.axis('equal')
        boundary = scatterList(np.array([domain.plot_me(t) for t in
                                         np.arange(0.001, 1,.001)]).flatten())
        if boundary:
            self.ax.plot(*boundary, color="black")

if __name__ == '__main__':
    app = VortexPlot()
    x0, Gamma = star_configuration([1/4, 1/2, 3/4], [-3/2, 1, -1/2], 3, centralGamma=2)
    app.animate(x0, Gamma)
