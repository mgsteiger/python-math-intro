import random

import sympy as sp

# This script creates random linear equations with integer solutions.
# Such equations are useful for worksheets, short practice sets, or tests.
#
# The equations are generated from the solution first.
# This makes sure that every equation has a clean integer answer.

x = sp.symbols("x")

# random.seed(...) makes the random results reproducible.
#
# As long as the seed stays the same, the script creates the same
# worksheet every time it is run.
#
# Change the number to create a different worksheet.
# Remove or comment out this line if you want different results
# every time the script runs.

random.seed(1)

number_of_equations = 8

questions = []
answers = []

for exercise_number in range(1, number_of_equations + 1):
    solution = random.randint(-8, 8)

    a = random.randint(-6, 6)
    while a == 0:
        a = random.randint(-6, 6)

    b = random.randint(-10, 10)
    right_side = a * solution + b

    equation = sp.Eq(a * x + b, right_side)

    questions.append(equation)
    answers.append(solution)

print("Linear equations")
print()

for exercise_number in range(1, number_of_equations + 1):
    equation = questions[exercise_number - 1]
    print(f"{exercise_number}. Solve ${sp.latex(equation)}$")

print()
print("Answer key")
print()

for exercise_number in range(1, number_of_equations + 1):
    solution = answers[exercise_number - 1]
    print(f"{exercise_number}. $x = {solution}$")
