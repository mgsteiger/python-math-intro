import sympy as sp

# SymPy can also solve quadratic equations.
#
# In this example, we solve
#
#     x² - 2x - 3 = 0

x = sp.symbols("x")

equation = sp.Eq(x**2 - 2 * x - 3, 0)

solutions = sp.solve(equation, x)

print("Equation:")
sp.pprint(equation)

print()
print("Solutions:")
sp.pprint(solutions)
