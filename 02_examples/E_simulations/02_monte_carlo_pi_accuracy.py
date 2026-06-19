import random

import matplotlib.pyplot as plt
import numpy as np

# In the previous example, we estimated π using random points.
#
# The estimate was not exact because it was based on a finite number
# of random points.
#
# In this example, we investigate how the estimate changes when we
# increase the number of random points.

# Different sample sizes.

sample_sizes = [
    10,
    20,
    50,
    100,
    200,
    500,
    1_000,
    2_000,
    5_000,
    10_000,
    20_000,
    50_000,
    100_000,
]

# Store the estimates.

estimates = []

for n in sample_sizes:
    inside_circle = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / n
    estimates.append(pi_estimate)

    print(f"n = {n:>6}   π ≈ {pi_estimate:.6f}")

# Plot the estimates.
#
# The horizontal line shows the actual value of π.
#
# For small sample sizes, the estimates may vary quite a lot.
# With larger sample sizes, they usually get closer to π.

plt.plot(sample_sizes, estimates, marker="o", label="Monte Carlo estimate")
plt.axhline(np.pi, linestyle="--", label="π")

# A logarithmic x-axis is useful because the sample sizes span several
# orders of magnitude.
#
# The y-axis remains linear so that the estimates can be compared
# directly with π.

plt.xscale("log")

plt.title("Monte Carlo Estimates of π")
plt.xlabel("Number of random points")
plt.ylabel("Estimated value of π")

plt.grid()
plt.legend()

plt.show()
