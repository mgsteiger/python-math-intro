import sympy as sp

# SymPy expressions can be displayed in different ways.
#
# The standard print() function shows expressions in a format that is
# convenient for Python.
#
# The pprint() function ("pretty print") displays expressions in a more
# mathematical form.

x = sp.symbols("x")

# Define a slightly more interesting expression.
#
# Pretty printing becomes particularly useful for fractions,
# roots and larger symbolic expressions.
f = (x**2 - 2) / sp.sqrt(x + 3)

df = sp.diff(f, x)

print("Standard output:")
print()

print("f(x) =")
print(f)

print()
print("f'(x) =")
print(df)

print()
print("-" * 40)
print()

print("Pretty printing:")
print()

print("f(x) =")
sp.pprint(f)

print()
print("f'(x) =")
sp.pprint(df)
