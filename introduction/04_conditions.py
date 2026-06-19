# A condition lets Python choose between different actions.
# The result of a comparison is either True or False.

x = 3

if x > 0:
    print("x is positive")
else:
    print("x is zero or negative")

# Conditions are important in simulations.
# For example, a point is inside the unit circle if x**2 + y**2 <= 1.

point_x = 0.4
point_y = 0.7

distance_squared = point_x**2 + point_y**2

print()
print("Point:", point_x, point_y)
print("Distance squared:", distance_squared)

if distance_squared <= 1:
    print("The point is inside the unit circle.")
else:
    print("The point is outside the unit circle.")

# More than two cases can be handled with elif.

temperature = 18

print()

if temperature < 15:
    print("The room is cool.")
elif temperature <= 22:
    print("The room is comfortable.")
else:
    print("The room is warm.")

