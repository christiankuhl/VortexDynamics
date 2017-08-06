#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dynamics import HamiltonianSolution, scatterList

class VortexPlot(object):
    def __init__(self, Tmax=10, eps=.01):
        self.Tmax = Tmax
        self.eps = .01
        self.setup()

    def animate(self, z0, Gamma):
        self.solution = HamiltonianSolution(z0, Gamma, self.Tmax, self.eps)
        self.scat = self.ax.scatter(scatterList(z0)[0],scatterList(z0)[1], c=Gamma)
                        #   s=.5, lw=0.5)#, edgecolors=[0,0],
                        #   facecolors='none')
        animation = FuncAnimation(self.fig, lambda n: self.scat.set_offsets(self.solution[n]), interval=1, frames=1000)
        plt.show()

    def setup(self):
        self.fig = plt.figure(figsize=(7, 7))
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        self.ax.set_xlim(-1, 1), self.ax.set_xticks([])
        self.ax.set_ylim(-1, 1), self.ax.set_yticks([])
        circ = plt.Circle((0, 0), radius=1, edgecolor='black', facecolor='None')
        self.ax.add_patch(circ)

if __name__ == '__main__':
    app = VortexPlot()
    x0 = [-.5,0,0,.5,0,-.5,.5,0]
    Gamma = [-1,1,-1,1]
    app.animate(x0, Gamma)
