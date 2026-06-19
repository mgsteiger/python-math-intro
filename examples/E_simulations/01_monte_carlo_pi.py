import random

import matplotlib.pyplot as plt
import numpy as np

# Monte Carlo methods use random numbers to approximate quantities.
#
# In this example, we estimate the value of π.
#
# Imagine a circle of radius 1 inside a square with side length 2.
#
# The area of the circle is
#
#     π · 1² = π
#
# The area of the square is
#
#     2 · 2 = 4
#
# Therefore:
#
#     area(circle) / area(square) = π / 4
#
# If we generate many random points inside the square,
# the proportion of points inside the circle should be
# approximately equal to π / 4.

# Try changing this number and observe how the estimate changes.
n = 1000

# Count how many points fall inside the circle.
#
# Store the generated points so that we can visualize the simulation.

inside_x = []
inside_y = []

outside_x = []
outside_y = []

inside_circle = 0

for _ in range(n):
    # Generate a random point in the square [-1, 1] × [-1, 1].

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Check whether the point lies inside the circle.
    #
    # A point is inside the circle if
    #
    #     x² + y² ≤ 1

    if x**2 + y**2 <= 1:
        inside_circle += 1

        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)

# Estimate π.

pi_estimate = 4 * inside_circle / n

print(f"Estimated π: {pi_estimate}")
print(f"Points inside circle: {inside_circle}")
print(f"Total points: {n}")
print(f"Inside fraction: {inside_circle / n:.5f}")

# Create points on the unit circle.
#
# These points are only used to draw the circle boundary.

theta = np.linspace(0, 2 * np.pi, 500)

circle_x = np.cos(theta)
circle_y = np.sin(theta)

# Plot the random points.

plt.scatter(
    outside_x,
    outside_y,
    s=5,
    label="Outside circle",
)

plt.scatter(
    inside_x,
    inside_y,
    s=5,
    label="Inside circle",
)

# Draw the circle boundary.

plt.plot(circle_x, circle_y, linewidth=2)

# Use the same scale on both axes so that the circle
# appears as a circle.

plt.axis("equal")

plt.title(f"Monte Carlo Estimate of π ≈ {pi_estimate:.5f}")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.legend()

plt.show()
