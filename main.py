#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

y0 = float(input("Digite o valor de y0: "))

vy0 = float(input("Digite o valor de vy0: "))

q = float(input("Digite o valor de q: "))
E = float(input("Digite o valor de E: "))
m = float(input("Digite o valor de m: "))

omega = float(input("Digite o valor de omega: "))

t = np.linspace(0,10,100)

x = (q*E/(2*m*omega**2))*(1-np.cos(omega*t))

y = y0 + vy0*t + (q*E/(2*m*omega**2))*(t-np.sin(omega*t))

print(x, "\n", y)

plt.plot(x,y)
plt.show()

