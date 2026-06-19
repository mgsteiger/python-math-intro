import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# In the previous examples, we used Matplotlib's default coordinate system.
#
# For teaching mathematics, we often prefer a coordinate system that resembles
# the textbook style used in classrooms:
#
# - equal scaling on both axes
# - axes through the origin
# - arrowheads indicating the positive directions
# - a visible grid


# Define the x-values used to evaluate the function.
x = np.linspace(-5, 5, 1000)


# Define the function values.
y = 3 * np.sin(x)


# Use the same scale on both axes.
#
# One unit on the x-axis has the same length as one unit on the y-axis.
# Without equal scaling, circles may appear as ellipses and angles may look distorted.
plt.axis("equal")


# Plot the function.
plt.plot(x, y)


# Place the axis labels near the positive ends of the axes.
plt.xlabel("x", loc="right", labelpad=-10)
plt.ylabel("y", loc="top", rotation=0, labelpad=-10)


# Get a reference to the current axes object.
#
# This gives access to more advanced customisation options.
ax = plt.gca()

# Move the axes to the origin and hide the outer frame.
ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add arrowheads to indicate the positive directions.
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Configure the major ticks.
#
# Major ticks appear every 1 unit.
# Grid lines are drawn at the tick positions.
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))


# Configure the minor ticks.
#
# Minor ticks appear every 0.5 units.
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))


# Draw grid lines for both major and minor ticks.
ax.grid(which="both")


# Show the plot window.
plt.show()
