import sympy as sp

# SymPy can solve systems of equations.
#
# In this example, we solve
#
#     x + y = 5
#     2x - y = 1

x, y = sp.symbols("x y")

eq1 = sp.Eq(x + y, 5)
eq2 = sp.Eq(2 * x - y, 1)

solution = sp.solve((eq1, eq2), (x, y))

print("System:")
sp.pprint(eq1)
sp.pprint(eq2)

print()
print("Solution:")
sp.pprint(solution)
