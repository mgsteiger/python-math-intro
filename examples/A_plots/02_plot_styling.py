import numpy as np
import matplotlib.pyplot as plt

# In this example, we improve the appearance of a plot.
#
# We will:
# - plot two functions in the same coordinate system
# - add a title
# - label the axes
# - display a grid
# - add a legend
#
# These elements make plots easier to read and understand,
# especially when they are used in worksheets, exams or handouts.

x = np.linspace(-5, 5, 1000)

# Define two functions.

y1 = x**2
y2 = x**2 - 2 * x - 3

# Plot both functions.
#
# The label argument specifies the text that will later
# appear in the legend.

plt.plot(x, y1, label="f(x) = x²")
plt.plot(x, y2, label="g(x) = x² - 2x - 3")

# Add a title.

plt.title("Comparing Two Quadratic Functions")

# Label the axes.

plt.xlabel("x")
plt.ylabel("y")

# Display a grid.

plt.grid()

# Display the legend.
#
# The legend uses the labels defined in plt.plot().

plt.legend()

# Show the plot window.

plt.show()
