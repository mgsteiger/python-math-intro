import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# In the previous example, we found critical points by solving
#
#     f'(x) = 0
#
# In this example, we also use the second derivative to classify
# these points as local minima or local maxima.

# Create the symbolic variable x.

x = sp.symbols("x")

# Define the function
#
#     f(x) = x³ - 3x

f = x**3 - 3 * x

# Compute the first and second derivative.

df = sp.diff(f, x)
ddf = sp.diff(df, x)

# Find the critical points.

critical_points = sp.solve(df, x)

print("Function:")
sp.pprint(f)

print()
print("First derivative:")
sp.pprint(df)

print()
print("Second derivative:")
sp.pprint(ddf)

print()
print("Critical points:")

for point in critical_points:
    y_point = f.subs(x, point)
    second_derivative_value = ddf.subs(x, point)

    if second_derivative_value > 0:
        point_type = "local minimum"
    elif second_derivative_value < 0:
        point_type = "local maximum"
    else:
        point_type = "inconclusive"

    print()
    print(f"x = {point}")
    print(f"f(x) = {y_point}")
    print(f"f''(x) = {second_derivative_value}")
    print(f"Type: {point_type}")

# Convert the symbolic function into a numerical function for plotting.

f_num = sp.lambdify(x, f, "numpy")

# Create x-values for plotting.

x_values = np.linspace(-3, 3, 1000)

# Compute the corresponding y-values.

y_values = f_num(x_values)

# Plot the function.

plt.plot(x_values, y_values, label=r"$f(x)=x^3-3x$")

# Mark and label the critical points.

for point in critical_points:
    y_point = f.subs(x, point)
    second_derivative_value = ddf.subs(x, point)

    if second_derivative_value > 0:
        point_type = "local minimum"
    elif second_derivative_value < 0:
        point_type = "local maximum"
    else:
        point_type = "inconclusive"

    plt.plot(float(point), float(y_point), "o")

    plt.annotate(
        point_type,
        xy=(float(point), float(y_point)),
        xytext=(8, 8),
        textcoords="offset points",
    )

# Add labels and a grid.

plt.title("Classifying Critical Points")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.legend()

# Show the plot window.

plt.show()
