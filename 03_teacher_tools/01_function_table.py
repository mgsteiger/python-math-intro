import sympy as sp

# Function tables are useful for worksheets, tests, and quick handouts.
# This script creates a small value table and also prints LaTeX table rows
# that can be copied into a document.

x = sp.symbols("x")

# Change this expression to create a different table.

f = x**2 - 2 * x - 3

# Choose the x-values that should appear in the table.

x_values = [-2, -1, 0, 1, 2, 3, 4]

print("Function:")
print("f(x) =", f)

print()
print("Value table:")
print("x | f(x)")
print("--|-----")

for x_value in x_values:
    y_value = f.subs(x, x_value)
    print(x_value, "|", y_value)

print()
print("LaTeX table rows:")

for x_value in x_values:
    y_value = f.subs(x, x_value)
    print(f"{x_value} & {sp.latex(y_value)} \\\\")

