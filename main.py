#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Valores típicos usados em tubos de raios catódicos (CRT):
y0 = 0.0              # posição inicial em y (m)
vy0 = 2e5             # velocidade inicial em y (m/s) – feixe lançado rápido
q = 1.6e-19           # carga do elétron (C)
E = 3e4               # campo elétrico (V/m)
m = 9.11e-31          # massa do elétron (kg)
omega = 2e7           # frequência angular (rad/s) – variação do campo

t = np.linspace(0, 1e-6, 1000)  # tempo em MICROSEGUNDOS

# Equações de movimento sob campo oscilatório
x = (q*E/(2*m*omega**2)) * (1 - np.cos(omega * t))
y = y0 + vy0 * t + (q*E/(2*m*omega**2)) * (t - np.sin(omega * t))

plt.plot(x, y)
plt.xlabel("Posição x (m)")
plt.ylabel("Posição y (m)")
plt.title("Trajetória do feixe eletrônico (simulação CRT)")
plt.grid(True)
plt.show()
