import numpy as np
from itertools import tee
from scipy.integrate import odeint
from utils import scatterList, symplectic
from domains import UnitDisk

class NVortexProblem(object):
    """
    Represents the dynamics of the N-vortex problem in a given domain.
    """

    def __init__(self, domain=UnitDisk(), Tmax=10, eps=.01):
        """
        Initialise solver for the domain with maximal time Tmax and timestep eps.
        """
        self.domain = domain
        self._Tmax = Tmax
        self._eps = eps
        self._N = int(self._Tmax / self._eps)

    @property
    def stepsize(self):
        return self._eps

    @stepsize.setter
    def stepsize(self, value):
        if value <= 0:
            raise ValueError("Nonpositive stepsize is not allowed.")
        else:
            self._eps = value
            self._N = int(self._Tmax / self._eps)

    @property
    def timesteps(self):
        return self._N

    @timesteps.setter
    def timesteps(self, number):
        if value <= 0:
            raise ValueError("Nonpositive number of timesteps is not allowed.")
        else:
            self._N = int(number)
            self._eps = int(self._Tmax / self._N)

    @property
    def Tmax(self):
        return self._Tmax

    @Tmax.setter
    def Tmax(self, value):
        if value <= 0:
            raise ValueError("Nonpositive simulation time is not allowed.")
        else:
            self._Tmax = value
            self._N = int(self._Tmax / self._eps)

    def RHS(self, z, Gamma):
        """
        RHS(z, Gamma) represents the right hand side of the ODE we are interested in.
        """
        z = zip(*[iter(z)]*2)
        z = list(enumerate(zip(z, Gamma)))
        return np.array([Gamma_j * self.domain.JGradh(z_j)  + 2 *
                                        sum(Gamma_i * self.domain.JGradG(z_j, z_i)
                                            for (i, (z_i, Gamma_i)) in z if i != j)
                                            for (j, (z_j, Gamma_j)) in z]).flatten()

    def HamiltonianSolution(self, z0, Gamma):
        """
        This is our ODE solver. Solution data is a list of numpy arrays of the form
        [[x1, ..., xn], [y1, ..., yn]] for each timestep.
        """
        t = [self._eps * tau for tau in range(self._N + 1)]
        f = lambda z, t: self.RHS(z, Gamma=Gamma)
        sol = odeint(f, z0, t)
        return [np.transpose(scatterList(s)) for s in sol]


    def GradientSolution(self, z0, Gamma):
        """
        This is our ODE solver for the corresponding gradient vector field.
        Solution data is a list of numpy arrays of the form
        [[x1, ..., xn], [y1, ..., yn]] for each timestep.
        """
        t = [self._eps * tau for tau in range(self._N + 1)]
        J = np.array([[symplectic(i, j) for i in range(len(z0))] for j in range(len(z0))])
        f = lambda z, t: self.RHS(z, Gamma=Gamma) @ J
        sol = odeint(f, z0, t)
        return [np.transpose(scatterList(s)) for s in sol]
