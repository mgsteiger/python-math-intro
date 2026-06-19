# A function is a reusable block of code.
# It can receive input values and return a result.


def square(x):
    return x**2


print("square(3) =", square(3))
print("square(-4) =", square(-4))


# Functions are particularly useful in mathematics because they allow us
# to represent formulas that can be evaluated for many different values.


def f(x):
    return x**2 - 2 * x - 3


x_values = [-2, -1, 0, 1, 2, 3, 4]
y_values = []

for x in x_values:
    y = f(x)
    y_values.append(y)

print()
print("x-values:", x_values)
print("y-values:", y_values)


# A function can also return True or False.
# This is useful for tests such as "inside the circle".


def is_inside_unit_circle(x, y):
    return x**2 + y**2 <= 1


print()
print("Is (0.4, 0.7) inside?", is_inside_unit_circle(0.4, 0.7))
print("Is (1.0, 1.0) inside?", is_inside_unit_circle(1.0, 1.0))
