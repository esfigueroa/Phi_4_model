import input.variables as var

import numpy as np


def define_variables() -> tuple:
    """
    Define variables to use
     dt = dx / np.sqrt(2.)
    """
    u = np.zeros((var.D, var.D, 3), float)
    v_ini = np.zeros((var.D, var.D), float)
    f = np.zeros((var.D, var.D), float)
    psi = np.zeros((var.D, var.D), float)
    psi_time_list = []
    force_time_list = []
    return u, v_ini, f, psi, psi_time_list, force_time_list
