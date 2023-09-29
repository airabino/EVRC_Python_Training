'''
This module holds a class which simulates a Mass-Spring-Damper system with external input
'''

import matplotlib.pyplot as plt

from math import sin, cos

class MassSpringDamper():

	def __init__(self, mass, spring, damper):

		self.mass=mass
		self.spring=spring
		self.damper=damper

	def Simulate(self, x_w, v_w, t):

		x_m = [self.mass.x_0] * len(x_w)
		v_m = [self.mass.v_0] * len(x_w)
		x_k = [self.mass.x_0 - x_w[0]] * len(x_w)
		v_k = [self.mass.v_0 - v_w[0]] * len(x_w)

		for idx in range(1, len(x_w)):

			dt = t[idx] - t[idx - 1]

			spring_force = self.spring.Step(x_k[idx - 1])
			damper_force = self.spring.Step(v_k[idx - 1])

			force = spring_force + damper_force

			x_m[idx], v_m[idx] = self.mass.Step(force, x_m[idx - 1], v_m[idx - 1], dt)
			x_k[idx] = x_m[idx] - x_w[idx]
			v_k[idx] = v_m[idx] - v_w[idx]

		return x_m, v_m, x_k, v_k

class Mass():

	def __init__(self, mass, x_0 = 0, v_0 = 0):

		self.mass = mass
		self.x_0 = x_0
		self.v_0 = v_0

	def Step(self, force, x, v, dt):

		a = force / self.mass

		x = x + v * dt + .5 * a * dt ** 2
		v = v + a * dt

		return x, v

class Spring():

	def __init__(self, k):

		self.k = k

	def Step(self, x):

		force = -self.k * x

		return force

class Damper():

	def __init__(self, b):

		self.b = b

	def Step(self, v):

		force = -self.b * v




def OscilatingForce(a = 1, c = 1, t0 = 0, tf = 1, dt = .1):

	n = round((tf - t0) / dt)
	t = [0.] * n
	x_w = [0.] * n
	v_w = [0.] * n

	for idx in range(n):
		t[idx] = t0 + dt * idx
		x_w[idx] = a * sin(c * t[idx])
		v_w[idx] = a * cos(c * t[idx])

	return x_w, v_w, t