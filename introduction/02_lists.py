# A list stores several values in one variable.
# Lists are useful when we want to collect numbers for a table,
# a plot, or a simulation.

x_values = [-2, -1, 0, 1, 2]

print("x-values:")
print(x_values)

# List items are numbered starting at 0.

first_value = x_values[0]
third_value = x_values[2]

print()
print("First value:", first_value)
print("Third value:", third_value)

# New values can be added with append().
# This pattern appears in simulations where results are collected step by step.

results = []

results.append(4)
results.append(1)
results.append(0)
results.append(1)
results.append(4)

print()
print("Collected results:")
print(results)

# Lists can also contain text.

labels = ["inside circle", "outside circle"]

print()
print("Labels:")
print(labels)

