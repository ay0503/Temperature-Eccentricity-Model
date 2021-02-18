#Stefan-Boltzmann Law
from math import *
from vpython import *

#constants
sigma = 5.67e-8
Ts = 5778
Rs = 6.96e8
Re = 6.37e6
D  = 1.496e11

Te = Ts * (Rs / 2 /D) ** 0.5
print(Te)