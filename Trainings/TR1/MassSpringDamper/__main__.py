'''
This module holds the __main__ script for the library
'''

import matplotlib.pyplot as plt

from .simulation import *

a, c, t0, tf, dt = 10, 2, 0, 10, .1
m, x_0, v_0 = 10, .1, 0
k = 100
b = 10

mass = Mass(m, x_0, v_0)
spring = Spring(k)
damper = Damper(b)
system = MassSpringDamper(mass, spring, damper)

x_w, v_w, t = OscilatingForce(a, c, t0, tf, dt)

x_m, v_m, x_k, v_k = system.Simulate(x_w, v_w, t)

fig, ax = plt.subplots(3, 1, figsize = (8,8))

ax[0].plot(t, x_w, color = 'b', linestyle = '--', linewidth = 2)
ax[0].set_ylabel(r'Wheel Position')
ax[1].plot(t, x_k, color = 'g', linestyle = '-.', linewidth = 2)
ax[1].set_ylabel(r'Spring Length')
ax[2].plot(t, x_m, color = 'k', linestyle = '-', linewidth = 2)
ax[2].set_xlabel('Time')
ax[2].set_ylabel(r'Mass Position')

[axes.grid(linestyle = '--') for axes in ax]

plt.show()

