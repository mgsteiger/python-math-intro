import sympy as sp

# SymPy can convert mathematical expressions to LaTeX.
# This is useful when preparing worksheets, exams, handouts, or solutions.

x = sp.symbols("x")

# Change this expression to create LaTeX for a different function.

f = (x + 1) ** 2 - 4

# SymPy can also rewrite expressions into useful equivalent forms.

expanded = sp.expand(f)
factored = sp.factor(expanded)
derivative = sp.diff(f, x)

print("Plain Python-style output:")
print("f(x) =", f)

print()
print("LaTeX output:")
print("f(x) =", sp.latex(f))

print()
print("Expanded form:")
print(sp.latex(expanded))

print()
print("Factored form:")
print(sp.latex(factored))

print()
print("Derivative:")
print(sp.latex(derivative))

print()
print("Ready-to-copy LaTeX snippets:")
print(f"$f(x) = {sp.latex(f)}$")
print(f"$f'(x) = {sp.latex(derivative)}$")

