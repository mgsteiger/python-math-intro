import random

import matplotlib.pyplot as plt

# In the previous examples, we simulated individual coin flips.
#
# We now repeat an entire experiment many times.
#
# Experiment:
#
#     Flip a fair coin 10 times.
#
# We count how often we obtain
#
#     0 heads
#     1 head
#     2 heads
#     ...
#     10 heads
#
# The resulting distribution is called a binomial distribution.

# Number of coin flips in each experiment.

n = 10

# Number of repeated experiments.

num_experiments = 10_000

# Count how often each outcome occurs.
#
# Example:
#
#     counts[7]
#
# stores how many experiments resulted in exactly 7 heads.

counts = [0] * (n + 1)

for _ in range(num_experiments):
    heads = 0

    # Perform one experiment consisting of n coin flips.

    for _ in range(n):
        if random.random() < 0.5:
            heads += 1

    counts[heads] += 1

# Convert counts into relative frequencies.

frequencies = [count / num_experiments for count in counts]

# Display the results.

for heads, frequency in enumerate(frequencies):
    print(f"{heads:2d} heads: {frequency:.4f}")

# Create a bar chart.

plt.bar(range(n + 1), frequencies)

plt.title("Binomial Distribution")
plt.xlabel("Number of heads")
plt.ylabel("Relative frequency")

plt.grid(axis="y")

plt.show()
