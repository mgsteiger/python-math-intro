import random

import sympy as sp

# This script creates quadratic equations with integer solutions.
# It is useful for preparing practice problems on factoring or solving
# quadratic equations.
#
# The roots are chosen first. Then the quadratic equation is built from them.
# This guarantees that the answer key is simple.

x = sp.symbols("x")

# random.seed(...) makes the random results reproducible.
#
# As long as the seed stays the same, the script creates the same
# worksheet every time it is run.
#
# Change the number to create a different worksheet.
# Remove or comment out this line if you want different results
# every time the script runs.

random.seed(2)

number_of_equations = 8

questions = []
answers = []

for exercise_number in range(1, number_of_equations + 1):
    root_1 = random.randint(-6, 6)
    root_2 = random.randint(-6, 6)

    while root_2 == root_1:
        root_2 = random.randint(-6, 6)

    factor = random.randint(1, 3)

    expression = factor * (x - root_1) * (x - root_2)
    expanded_expression = sp.expand(expression)
    equation = sp.Eq(expanded_expression, 0)

    questions.append(equation)
    answers.append((root_1, root_2))

print("Quadratic equations")
print()

for exercise_number in range(1, number_of_equations + 1):
    equation = questions[exercise_number - 1]
    print(f"{exercise_number}. Solve ${sp.latex(equation)}$")

print()
print("Answer key")
print()

for exercise_number in range(1, number_of_equations + 1):
    root_1 = answers[exercise_number - 1][0]
    root_2 = answers[exercise_number - 1][1]
    print(f"{exercise_number}. $x = {root_1}$ or $x = {root_2}$")
