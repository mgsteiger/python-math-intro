import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# SymPy can help us find extrema of a function.
#
# The basic idea is:
#
# 1. Compute the derivative.
# 2. Find where the derivative is zero.
# 3. These points are candidates for extrema.
# 4. Visualize the result.

# Create the symbolic variable x.

x = sp.symbols("x")

# Define the function
#
#     f(x) = x³ - 3x

f = x**3 - 3 * x

# Compute the derivative.

df = sp.diff(f, x)

# Find the critical points.
#
# These are the points where the derivative is zero.

critical_points = sp.solve(df, x)

print("Function:")
sp.pprint(f)

print()
print("Derivative:")
sp.pprint(df)

print()
print("Critical points:")
sp.pprint(critical_points)

# Convert the symbolic function into a numerical function.

f_num = sp.lambdify(x, f, "numpy")

# Create x-values for plotting.

x_values = np.linspace(-3, 3, 1000)

# Compute the corresponding y-values.

y_values = f_num(x_values)

# Plot the function.

plt.plot(x_values, y_values, label=r"$f(x)=x^3-3x$")

# Mark the critical points.

for point in critical_points:
    y_point = f.subs(x, point)

    plt.plot(
        float(point),
        float(y_point),
        "o",
    )

# Add labels and a grid.

plt.title("Critical Points of a Function")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.legend()

# Show the plot window.

plt.show()
