"""
Admissibility conditions from [Kuhl, 2014]
"""

from utils import pairwise, powerset

def boundary_admissible(Gamma):
    # del-admissibility
    ca = all(sum(Gamma[i]*Gamma[j] for i in J for j in J if i != j) < sum(Gamma[i]**2 for i in J)
                                                            for J in powerset(range(len(Gamma))))
    if not ca:
        print("Vorticities {} are not del-admissible.".format(Gamma))
    return ca

def L_admissible(Gamma):
    # L-admissibility
    iotaGamma = [(-1)**i * g for i, g in enumerate(Gamma)]
    la = ((all(g>0 for g in iotaGamma) or all(g<0 for g in iotaGamma))
         and (all(f >= g for f, g in pairwise(iotaGamma))
              or all(f <= g for f, g in pairwise(iotaGamma))))
    if not la:
        print("Vorticities {} are not L-admissible.".format(Gamma))
    return la

def delta_admissible(Gamma):
    # Delta-admissibility
    da = all(sum(Gamma[i]*Gamma[j] for i in J for j in J if i != j) != 0
                                        for J in powerset(range(len(Gamma))))
    if not da:
        print("Vorticities {} are not delta-admissible.".format(Gamma))
    return da

def is_admissible(Gamma):
    da = delta_admissible(Gamma)
    ca = boundary_admissible(Gamma)
    la = L_admissible(Gamma)
    return da and ca and la
