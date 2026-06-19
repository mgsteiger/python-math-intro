import random

import matplotlib.pyplot as plt

# The law of large numbers states that relative frequencies tend to
# approach the corresponding probabilities as the number of trials
# becomes large.
#
# We illustrate this idea with repeated coin flips.
#
# For a fair coin:
#
#     P(heads) = 0.5
#
# The relative frequency of heads may fluctuate strongly at the
# beginning, but it should gradually move closer to 0.5.

# Number of coin flips.

n = 10_000

heads_count = 0

flip_numbers = []
relative_frequencies = []

for flip in range(1, n + 1):
    # Simulate a fair coin.

    if random.random() < 0.5:
        heads_count += 1

    # Compute the current relative frequency of heads.

    relative_frequency = heads_count / flip

    flip_numbers.append(flip)
    relative_frequencies.append(relative_frequency)

# Display the final result.

print(f"Heads: {heads_count}")
print(f"Total flips: {n}")
print(f"Relative frequency: {heads_count / n:.5f}")

# Plot the relative frequency.

plt.plot(
    flip_numbers,
    relative_frequencies,
    label="Relative frequency of heads",
)

# Plot the theoretical probability.

plt.axhline(
    0.5,
    linestyle="--",
    label="P(heads) = 0.5",
)

plt.title("Law of Large Numbers")
plt.xlabel("Number of coin flips")
plt.ylabel("Relative frequency")

plt.grid()
plt.legend()

plt.show()
