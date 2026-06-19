import random

import matplotlib.pyplot as plt

# Simulate repeated coin flips.
#
# For a fair coin, the probability of heads is
#
#     P(heads) = 0.5
#
# We investigate how the relative frequency changes
# as we perform more flips.

n = 1000

heads_count = 0

flip_numbers = []
relative_frequencies = []

for flip in range(1, n + 1):
    if random.random() < 0.5:
        heads_count += 1

    relative_frequency = heads_count / flip

    flip_numbers.append(flip)
    relative_frequencies.append(relative_frequency)

plt.plot(
    flip_numbers,
    relative_frequencies,
    label="Relative frequency of heads",
)

plt.axhline(
    0.5,
    linestyle="--",
    label="Theoretical probability",
)

plt.title("Coin Flips")
plt.xlabel("Number of flips")
plt.ylabel("Relative frequency of heads")

plt.grid()
plt.legend()

plt.show()
