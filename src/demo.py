#!/usr/bin/env python2

from matplotlib import cm, pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import *
import sys
import pygradesc as gd




def frange(start, end, step=1):
	res = []
	while start < end:
		res.append(start)
		start += step
	return res


def plot3d(fxy, points, xseq, yseq):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.axis("off")

	xgrid,ygrid = np.meshgrid(xseq, yseq)
	zgrid = [[0.0] * len(xseq) for _ in yseq]

	for j,y in enumerate(yseq):
		for i,x in enumerate(xseq):
			x = float(x)
			y = float(y)
			zgrid[j][i] = fxy(x, y)

	X = map(lambda x:x[0], points)
	Y = map(lambda x:x[1], points)
	Z = map(lambda x:x[2], points)

	ax.plot(X, Y, Z, c='k', lw=3, marker='o')
	ax.plot_surface(xgrid, ygrid, zgrid, rstride=1, cstride=1, cmap=cm.jet, linewidth=0.25)

	ax.set_xlabel(r'$x$')
	ax.set_ylabel(r'$y$')
	ax.set_zlabel(r'$f(x,y)$')
	plt.show()


def demo():
	# fancy function f(x,y)=z
	fxy = lambda x,y: (-exp(-x**2-y**2)) + (exp(-(x-3)**2-y**2)) + ((x**2+y**2)/100)

	# run the gradient descent algorithm
	points = gd.minimize(fxy, [3.5, 0.1], 0.25, 1000, mode='smooth')

	# plot the surface as well as the steps taken
	plot3d(fxy, points, frange(-.25, 5.5, .25), frange(-3.5, 3.5, .25))


def main(argv=None):
	if argv == None:
		argv = sys.argv
	argc = len(argv)

	demo()

	return 0




if __name__ == '__main__':
	sys.exit(main())
