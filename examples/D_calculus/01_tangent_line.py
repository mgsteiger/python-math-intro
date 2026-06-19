import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# In the previous examples, we learned how to:
#
# - plot functions with Matplotlib
# - compute derivatives with SymPy
#
# In this example, we combine both ideas.
#
# We will:
#
# - compute the derivative of a function
# - determine the slope at a given point
# - construct the tangent line
# - plot the function and its tangent

# Create the symbolic variable x.

x = sp.symbols("x")

# Define the function
#
#     f(x) = x²

f = x**2

# Compute the derivative.
#
#     f'(x) = 2x

df = sp.diff(f, x)

# Choose the point where the tangent should be constructed.

x0 = 1

# Compute the corresponding y-value.

y0 = f.subs(x, x0)

# Compute the slope of the tangent.
#
# The derivative gives the slope of the tangent at a point.

m = df.subs(x, x0)

# Construct the tangent line.
#
# Point-slope form:
#
#     y = m(x - x0) + y0

tangent = m * (x - x0) + y0

# Display the symbolic results.

print("Function:")
sp.pprint(f)

print()
print("Derivative:")
sp.pprint(df)

print()
print(f"Tangent point: ({x0}, {y0})")

print()
print("Tangent line:")
sp.pprint(tangent)

# lambdify() converts a symbolic SymPy expression into a function
# that can be evaluated numerically.

f_num = sp.lambdify(x, f, "numpy")
tangent_num = sp.lambdify(x, tangent, "numpy")

# Create x-values for plotting.

x_values = np.linspace(-2, 4, 1000)

# Compute the corresponding y-values.

y_function = f_num(x_values)
y_tangent = tangent_num(x_values)

# Plot the function.

plt.plot(x_values, y_function, label=r"$f(x)=x^2$")

# Plot the tangent.

plt.plot(
    x_values,
    y_tangent,
    "--",
    label="Tangent at x = 1",
)

# Mark the point of tangency.

plt.plot(x0, y0, "o")

# Add labels and a grid.

plt.title("Function and Tangent Line")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.legend()

# Show the plot window.

plt.show()
