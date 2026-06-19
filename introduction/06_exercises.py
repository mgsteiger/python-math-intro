# Short exercises for the Python introduction.
# Run the file after each change and inspect the output.


# Exercise 1:
# Change the value of x and predict the output before running the file.

x = 5
y = x**2 - 2 * x - 3

print("Exercise 1")
print("x =", x)
print("y =", y)


# Exercise 2:
# Add two more numbers to x_values.
#
# Predict the corresponding y-values before running the file.

x_values = [-2, -1, 0, 1, 2]
y_values = []

for x in x_values:
    y_values.append(x**2)

print()
print("Exercise 2")
print("x-values:", x_values)
print("y-values:", y_values)


# Exercise 3:
# Change point_x and point_y.
# Decide before running whether the point is inside the unit circle.

point_x = 0.8
point_y = 0.3

if point_x**2 + point_y**2 <= 1:
    position = "inside"
else:
    position = "outside"

print()
print("Exercise 3")
print("The point is", position, "the unit circle.")


# Exercise 4:
# Complete the function so that it returns the value of
#
#     f(x) = x**2 - 4
#
# Then use the loop below to evaluate the function.


def f(x):
    return 0


print()
print("Exercise 4")

for x in [-3, -2, -1, 0, 1, 2, 3]:
    print("x =", x, "f(x) =", f(x))
