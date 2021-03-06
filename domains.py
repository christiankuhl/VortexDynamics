from importlib import import_module
from abc import ABCMeta, abstractmethod

class AbstractDomain(metaclass=ABCMeta):
    """
    ABC to define the minimum implementation requirements for domains in which
    to simulate the N-vortex problem.
    """
    @abstractmethod
    def JGradG(self, z1, z2):
        """
        JGradG(z1, z2) is the product of the 2d symplectic matrix J with the gradient
        with respect to the first variable of the Green's function G of the negative
        Dirichlet Laplacian in the domain. Should return a 2d numpy array.
        """
        pass

    @abstractmethod
    def JGradh(self, z):
        """
        JGradh(z) is the product of the 2d symplectic matrix J with the gradient
        of the Robin's function of the domain. Should return a 2d numpy array.
        """
        pass

    @abstractmethod
    def plot_me(self, t):
        """
        Should provide a parametrisation of the interval (0, 1) to the domain's boundary.
        """

class Domain(AbstractDomain):
    """
    Base class for all N-vortex domains. To implement a new domain MyDomain,
    simply define a class MyDomain inheriting from Domain and implement functions
    as defined in AbstractDomain in a module named mydomain.py
    """
    def __init_subclass__(cls):
        module = import_module(cls.__name__.lower())
        for name, obj in module.__dict__.items():
            setattr(cls, name, obj)

    def __init__(self, xlim=(-1, 1), ylim=(-1, 1)):
        self.xlim = xlim
        self.ylim = ylim

class UnitDisk(Domain):
    """
    This class implements the N-vortex dynamics for the unit disk.
    """
    pass

class Plane(Domain):
    """
    This class implements the N-vortex dynamics for the Euclidean plane.
    """
    pass

class HalfPlane(Domain):
    """
    This class implements the N-vortex dynamics for the half plane.
    """
    pass

class Ellipse(Domain):
    """
    This class implements the N-vortex dynamics for the ellipse.
    """
    pass
