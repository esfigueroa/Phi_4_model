# import input.variables as var
import numpy as np


def force(dx, D, B_square) -> float:
    """
    Define force for the solitons
    :param dx: var.dx
    :param D: var.D
    :param B_square: var.B
    :return:
    """
    f = np.zeros((D, D), float)
    print(f.shape)
    for m in range(0, D):
        for n in range(0, D):
            #first_term = 0.5 * (4*B_square - 1)
            #inner_term = np.sqrt(B_square) * dx * (n - (D - 1) / 2)
            #sec_term = np.sinh(inner_term)
            #thr_term = np.cosh(inner_term)*np.cosh(inner_term)*np.cosh(inner_term)
            #f[m][n] = first_term * sec_term / thr_term
            f[m][n] = -0.008
    return f
