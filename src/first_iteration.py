import input.variables as var
import numpy as np


def first_it(u, f) -> np.array:
    """
    First iteration
    :param u: field u
    :param f: field of the force
    :return:
    """
    for m in range(1, var.D - 1):
        for l in range(1, var.D - 1):
            a2 = u[m + 1][l][0] + u[m - 1][l][0] + u[m][l + 1][0] + u[m][l - 1][0]
            tmp = 0.25 * a2
            cub_tmp = tmp * tmp * tmp
            u1 = .5 * ((var.dts * a2) + (var.dt * var.dt * (0.5) * (tmp-cub_tmp)))
            u2 = (1 - (2 * var.dts)) * u[m][l][0]
            uf = 0.5 * f[m][l] * var.dt * var.dt
            u[m][l][1] = u1 + u2 + uf
    return u
