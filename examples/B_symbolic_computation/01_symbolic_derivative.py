import sympy as sp

# Python normally works with numbers.
#
# By using the SymPy library, Python can also perform symbolic
# computations, similar to a CAS (Computer Algebra System)
# such as the TI-Nspire CX II-T CAS.
#
# This means that Python can manipulate mathematical expressions,
# solve equations and compute derivatives symbolically.

# Create the symbolic variable x.

x = sp.symbols("x")

# Define the function
#
#     f(x) = x² - 2x - 3

f = x**2 - 2 * x - 3

# Display the symbolic expression.

print("f(x) =", f)

# Compute the derivative.
#
# The function sp.diff() performs symbolic differentiation.

df = sp.diff(f, x)

print("f'(x) =", df)
