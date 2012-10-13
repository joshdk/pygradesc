import numpy as np




def _ordinal(vec):
	imax = 0
	vmax = vec[0]
	for i,v in enumerate(vec):
		if abs(v) > abs(vmax):
			vmax = v
			imax = i
	ret = np.array([0]*len(vec), dtype=float)
	ret[imax] = 1 if vmax >= 0 else -1
	# print(imax, vmax)
	return ret


def _normal(fn, start, delta):
	loc = np.array(start, dtype=float)
	dim = len(loc) # given x, solve for y, given x & y, solve for z, etc...

	# running vector for a surface normal
	running = np.array([0]*(dim+1), dtype=float)

	for i in range(dim):
		# generate cardinal vectors of the form
		# (in 2d) [1,0] [0,1]
		# (in 3d) [1,0,0] [0,1,0] [0,0,1]
		# etc...
		vmask  = ([0]*i) + [] + ([0]*(dim-i-i))
		vmask  = np.array([0] * dim)
		vmask[i] = 1

		vdelta = vmask * delta

		# a position to the left and right of loc
		vlloc  = loc - vdelta
		vrloc  = loc + vdelta

		# value of fn() at thoes two positions
		slval  = fn(*vlloc)
		srval  = fn(*vrloc)

		# calculate a the slope vector
		vgrad  = np.array([delta * 2, slval - srval], dtype=float)
		vgrad /= np.linalg.norm(vgrad)

		# calculate the inverse (perpendicular) slope vector
		vigrad = np.array([-vgrad[1], vgrad[0]], dtype=float)
		vigrad /= np.linalg.norm(vigrad)

		# map the inverse slope to a higher space
		component = np.array([0.0]*(dim+1), dtype=float)
		component[-1] = vigrad[1]

		# make sure slope points in a "downward" direction
		if slval < srval:
			component[i] = -abs(vigrad[0])
		else:
			component[i] = abs(vigrad[0])

		# add oomponent to tally
		running += component

	# normalize to the unit-hypersphere
	running /= np.linalg.norm(running)

	return running


def minimize(fn, start, delta, steps, mode='smooth'):
	# starting location in space
	current = np.array(start, dtype=float)

	# history of all locations
	hist = [list(current)+[fn(*current)]]

	for step in range(steps):
		
		# calculate surface normal
		norm = _normal(fn, current, delta)

		# flatted into a lower dimension
		dir = norm[:-1]

		if mode == 'unit':
			# constrain next location to 1 unit distance away from current point
			dir /= np.linalg.norm(dir)
		elif mode == 'square':
			# constrain next location to 1 unit distance away from current point in the dominant ordinal direction
			dir = _ordinal(dir)

		# move to the next location
		current += dir * delta

		# add it to the history list
		hist.append(list(current)+[fn(*current)])

	return hist
