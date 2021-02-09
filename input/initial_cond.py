import numpy as np
import input.variables as var


def initial(u: np.ndarray) -> np.ndarray:
    """
    Define initial conditions
    :type u: float
    :param u: field
    :return:
    Note: if change the initial condition, it is necessary to chance the "dx" like dx=x_0/100 (for example) to obtain a simetric soliton
    """
    uf = np.zeros((var.D, var.D), float)
    yy = -var.y_0
    for i in range(0, var.D):
        xx = -var.x_0
        for j in range(0, var.D):
            tmp = xx-var.x_00
            u[i][j][0] = np.tanh(tmp) # gamma_rel * tmp
            xx = xx + var.dx
        yy = yy + var.dy
    return u

