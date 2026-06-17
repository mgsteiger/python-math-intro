import numpy as np
import matplotlib.pyplot as plt

# We want to plot the function
#
#     f(x) = x^2 - 2x - 3
#
# In mathematics, we usually think of x as a real variable.
# A computer, however, cannot draw "all" real x-values.
# Instead, we choose many individual x-values in a given interval.

x = np.linspace(-5, 5, 1000)

# x is now an array containing 1000 numbers between -5 and 5.
# For each of these x-values, Python computes the corresponding y-value.
#
# Important:
# In Python, powers are written with **.
#
#     x**2   means   x^2
#
# Since x is an array, the following line computes all y-values at once.

y = x**2 - 2 * x - 3

# Now we plot the computed points.
# Matplotlib connects the points with lines, so the result looks like
# the graph of the continuous function.

plt.plot(x, y)

# Show the plot window.

plt.show()
