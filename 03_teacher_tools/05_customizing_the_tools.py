import random

import sympy as sp

# Practice tasks for adapting the teacher tools.
# The file is runnable as it is, but each exercise comment suggests
# a small change that is useful for worksheet or exam preparation.

x = sp.symbols("x")

# random.seed(...) makes the random results reproducible.
#
# As long as the seed stays the same, the random exercises below
# are the same every time the script is run.
#
# Change the number to get different random exercises.
# Remove or comment out this line if you want different results
# every time the script runs.

random.seed(3)


# Exercise 1:
# Change the function and the x-values to create a table for your lesson.

f = x**2 - 4
x_values = [-3, -2, -1, 0, 1, 2, 3]

print("Exercise 1: Function table")
print("x | f(x)")
print("--|-----")

for x_value in x_values:
    y_value = f.subs(x, x_value)
    print(x_value, "|", y_value)


# Exercise 2:
# Change g and copy the printed LaTeX into a worksheet.

g = (x - 2) * (x + 5)

print()
print("Exercise 2: LaTeX")
print(f"$g(x) = {sp.latex(sp.expand(g))}$")
print(f"$g(x) = {sp.latex(sp.factor(g))}$")


# Exercise 3:
# Change number_of_equations to create a longer or shorter practice set.

number_of_equations = 4

print()
print("Exercise 3: Random linear equations")

for exercise_number in range(1, number_of_equations + 1):
    solution = random.randint(-5, 5)

    a = random.randint(1, 6)
    b = random.randint(-8, 8)
    right_side = a * solution + b

    equation = sp.Eq(a * x + b, right_side)

    print(f"{exercise_number}. Solve ${sp.latex(equation)}$")
    print(f"   Answer: $x = {solution}$")


# Exercise 4:
# Change the possible roots to control the difficulty.

possible_roots = [-4, -3, -2, -1, 1, 2, 3, 4]

root_1 = random.choice(possible_roots)
root_2 = random.choice(possible_roots)

while root_2 == root_1:
    root_2 = random.choice(possible_roots)

quadratic = sp.expand((x - root_1) * (x - root_2))
equation = sp.Eq(quadratic, 0)

print()
print("Exercise 4: Random quadratic equation")
print(f"Solve ${sp.latex(equation)}$")
print(f"Answer: $x = {root_1}$ or $x = {root_2}$")
