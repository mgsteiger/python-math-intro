import sympy as sp

# SymPy can also compute symbolic integrals.
#
# Instead of evaluating an integral numerically,
# SymPy returns an exact symbolic result.

x = sp.symbols("x")

# Define the function
#
#     f(x) = x² - 2x - 3

f = x**2 - 2 * x - 3

# Compute an antiderivative.
#
# The function sp.integrate() performs symbolic integration.

F = sp.integrate(f, x)

print("f(x) =", f)

print()

print("F(x) =")
sp.pprint(F)

# Note:
# SymPy returns one antiderivative.
# The constant of integration (+C) is omitted.
