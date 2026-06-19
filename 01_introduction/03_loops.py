# A loop repeats the same block of code.
# This is useful when we want to compute many values.

x_values = [-2, -1, 0, 1, 2]
y_values = []

for x in x_values:
    # This line belongs to the loop because it is indented.
    y = x**2
    y_values.append(y)

print("x-values:", x_values)
print("y-values:", y_values)

print()
print("Table:")

for x in x_values:
    y = x**2
    print("x =", x, "y =", y)

# range(n) creates the numbers 0, 1, ..., n - 1.
#
# This sometimes surprises beginners because Python starts counting
# at 0 rather than at 1.
#
# range(5) therefore creates:
#
#     0, 1, 2, 3, 4
#
# It is often used when a simulation should run many times.

print()
print("Counting simulation runs:")

for run in range(5):
    print("Run number:", run)

# If counting should start at 1, use range(1, n + 1).

print()
print("Counting from 1:")

for run in range(1, 6):
    print("Run number:", run)
