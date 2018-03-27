from utils import pairwise

def boundary_admissible(Gamma):
    return False

def L_admissible(Gamma):
    iGamma = map(lambda j, x: (-1)**j * x, enumerate(Gamma))
    signs = all(x > 0 for x in iGamma) or all(x < 0 for x in iGamma)
    direction = all(a <= b for (a, b) in pairwise(iGamma)) or all(a >= b for (a, b) in pairwise(iGamma))
    return signs and direction
