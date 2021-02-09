import numpy as np
import input.variables as var


def initial_vel(v_ini: np.ndarray) -> np.ndarray:
    """
    Define initial conditions for velocity
    :type v_ini: float
    :param v_ini: initial velocity
    :return:
    Note: if change the initial condition, it is necessary to chance the "dx" like dx=x_0/100 (for example) to obtain a simetric soliton
    """
    yy = -var.y_0
    for i in range(0, var.D):
        xx = -var.x_0
        for j in range(0, var.D):
            tmp = xx-var.x_00
            ch_square = np.cosh(tmp) * np.cosh(tmp)  # hyperbolic cosine square
            v_ini[i][j] = - var.gamma_rel * var.v_0 * var.dt / ch_square
            xx = xx + var.dx
        yy = yy + var.dy
    return v_ini
