import numpy as np
import matplotlib.pyplot as plt

L = 0.1
n = 10
T0 = 0
t1, t2 = 40, 20
dx = L / n
alpha = 0.0001
tf = 60
dt = 0.1

x = np.linspace(0, L, n)
t = np.arange(0, tf, dt)
T = np.ones(n) * T0 

def dT_dt():
  deriv = np.zeros(n)
  for i in range(n):
    t_b = T[i-1] if i > 0 else t1
    t_f = T[i+1] if i < n-1 else t2
    deriv[i] = alpha * (t_b -2*T[i] + t_f) / dx**2
  return deriv 

plt.ion()

for ti in t:
  plt.plot(x, T)
  plt.axis([0, L, 0, 50]) 
  plt.draw()
  plt.pause(0.01)
  plt.clf()

  T += dT_dt() * dt
