import os
import platform
from pathlib import Path
import numpy as np

pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth).parents[0])

D = 200
dx = 0.5
dy = 0.25
dt = 0.01
x_0 = dx*100
y_0 = dy*100
x_00 = 2
y_00 = 4
v_0 = 0.08
Gamma = 0.1
B_square = 0.25
gamma_rel = np.sqrt(1/(1 - v_0 * v_0)) # include in the initials conditions
sigma = 15
Disp = 1 / (2 + (Gamma * dt))
Dism = (2 - (Gamma * dt))
dts = (dt / dx) * (dt / dx)
number_iterations = 499
number_steps_print_file = 20
print(PATH)
# VARIABLES FOR OUTPUTS
if platform.system() == "Darwin":
    output = PATH + "/output/"
else:
    output = PATH + "\\output\\"

dir_name = "phi_4_dx_" + str(dx) + "dy_" + str(dy) + "_dt_" + str(round(dt, 2)) + "_D_" + str(D) + "_B_square_" + str(
    float(round(B_square, 2))) + "_x_0_" + str(float(round(x_00, 2))) + "_Gamma_" + \
           str(float(round(Gamma, 2)))+ "_f_-0.008" + "_v_0_" + str(float(round(v_0, 2))) + "_gamma_rel_" + str(float(round(gamma_rel, 2)))
