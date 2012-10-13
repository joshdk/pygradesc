pygradesc
=========

An n-dimensional gradient descent algorithm


Example
-------

![Example output](https://raw.github.com/joshdk/pygradesc/master/img/graph1.png "Example output")


Usage
-----

### Importing

```python
import pygradesc as gd
````

### Creating functions

```python
# Functions (or lambdas) take the form f(a1, a2, ..., an) -> an+1

# Constructor a 2D function f(x) -> y
fx = lambda x: x*x

# Constructor a 3D function f(x,y) -> z
fxy = lambda x, y: (x-1)**2+(y-2)**2

# Constructor a 4D function f(x,y,z) -> d
fxyz = lambda x, y, z: x**2+5*y+z
```

### Running

```python
# Starting point
start = [-2, -6]

# Delta size (how far should we move towards our goal)
delta = 0.25

# Number of steps
steps = 1000

# Get a list of points for each step in the algorithm
points = gd.minimize(fxy, start, delta, steps)

print(points)
# points[0]   -> [-2.0,    -6.0,     73.0      ]
# points[1]   -> [-1.83.., -5.82..,  69.21..   ]
# ..
# points[999] -> [ 0.99..,  1.99..,  2.47..e-31]
```

Dependencies
------------

*   [numpy](http://numpy.scipy.org/)



