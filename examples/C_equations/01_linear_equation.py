import sympy as sp

# SymPy can solve equations symbolically.
#
# In this example, we solve the linear equation
#
#     3x + 5 = 17

x = sp.symbols("x")

equation = sp.Eq(3 * x + 5, 17)

# Solve the equation for x.

solution = sp.solve(equation, x)

print("Equation:")
sp.pprint(equation)

print()
print("Solution:")
sp.pprint(solution)
