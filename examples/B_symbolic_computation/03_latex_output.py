import sympy as sp

# SymPy can generate LaTeX code from mathematical expressions.
#
# This can be useful when creating worksheets, exams or lecture notes.

x = sp.symbols("x")

# Define a symbolic expression containing both a fraction
# and a square root.
#
# Such expressions are cumbersome to typeset manually but can
# be converted to LaTeX automatically.
f = (x**2 - 2) / sp.sqrt(x + 3)

df = sp.diff(f, x)

print("LaTeX code for f(x):")
print(sp.latex(f))

print()
print("LaTeX code for f'(x):")
print(sp.latex(df))

print()
print("Example LaTeX snippet:")
print(f"$f(x) = {sp.latex(f)}$")
