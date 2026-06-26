# Python Math Intro

A gentle introduction to Python for mathematics, visualization, symbolic computation and simulations.

This repository contains examples and resources demonstrating how Python can be used to:

- visualize mathematical concepts
- perform symbolic computations
- solve equations
- run simulations
- explore probability and statistics

No prior Python experience is required.

## Getting Started

The examples in this repository are provided as regular Python files and can be explored without installing Python locally.

### Option 1: WebTigerPython (recommended)

Open https://webtigerpython.ethz.ch in your browser and either:

- copy and paste one of the example files
- upload an example file directly

WebTigerPython provides a simple environment for experimenting with Python and includes many commonly used scientific and mathematical packages.

### Option 2: Local Installation

See [guides/local-python-setup.md](guides/local-python-setup.md).

## Repository Structure

The examples are organized by topic and can be explored in order.

```text
01_introduction/
├── 01_variables_and_print.py
├── 02_lists.py
├── 03_loops.py
├── 04_conditions.py
├── 05_functions.py
└── 06_exercises.py

02_examples/
├── A_plots/
│   ├── 01_plot_function.py
│   ├── 02_plot_styling.py
│   ├── 03_plot_textbookstyle.py
│   └── 04_exercises.py
│
├── B_symbolic_computation/
│   ├── 01_symbolic_derivative.py
│   ├── 02_pretty_printing.py
│   ├── 03_latex_output.py
│   ├── 04_symbolic_integral.py
│   └── 05_exercises.py
│
├── C_equations/
│   ├── 01_linear_equation.py
│   ├── 02_quadratic_equation.py
│   ├── 03_system_of_equations.py
│   └── 04_exercises.py
│
├── D_calculus/
│   ├── 01_tangent_line.py
│   ├── 02_extrema.py
│   ├── 03_function_analysis.py
│   └── 04_exercises.py
│
└── E_simulations/
    ├── 01_monte_carlo_pi.py
    ├── 02_monte_carlo_pi_accuracy.py
    ├── 03_coin_flips.py
    ├── 04_law_of_large_numbers.py
    ├── 05_binomial_distribution.py
    └── 06_exercises.py

03_teacher_tools/
├── 01_function_table.py
├── 02_latex_from_expression.py
├── 03_random_linear_equations.py
├── 04_random_quadratic_equations.py
└── 05_customizing_the_tools.py
```

## How to Use This Repository

Open an example file and run it.

Then experiment by modifying the code:

- change functions
- change intervals
- compare multiple functions
- adjust the appearance of plots

The examples are intentionally small and heavily commented.

If you are new to Python, start with the files in `01_introduction/`.
They introduce only the basic Python ideas needed for the later folders:
variables, lists, loops, conditions, functions, and short exercises.

The files are organized by topic and can be explored in order.

## Learning Path

### Introduction

The introduction folder gives a very short first contact with Python:

- variables and `print()`
- lists
- loops
- conditions
- functions
- practice exercises

### A. Plots

The first topic introduces plotting with `Matplotlib`:

- plotting a function
- improving plot appearance
- creating textbook-style coordinate systems
- practice exercises

### B. Symbolic Computation

The second topic introduces symbolic mathematics with `SymPy`:

- symbolic differentiation
- symbolic integration
- pretty printing
- LaTeX output
- practice exercises

### C. Solving Equations

The third topic introduces equation solving with `SymPy`:

- linear equations
- quadratic equations
- systems of equations
- practice exercises

### D. Calculus

The fourth topic combines plotting and symbolic computation:

- tangent lines
- critical points
- classification of extrema
- practice exercises

### E. Simulations

The fifth topic introduces probabilistic simulations:

- Monte Carlo estimation of π
- coin flips
- law of large numbers
- binomial distributions
- practice exercises

### Teacher Tools (Optional)

The `03_teacher_tools/` folder contains short practical scripts for preparing
teaching materials. These tools are independent of the learning path and can be explored at any time.

- function tables for worksheets
- LaTeX output from symbolic expressions
- random linear equations with answer keys
- random quadratic equations with answer keys
- ideas for customizing the tools

## Resources

### Python

- Python: https://www.python.org
- Python Tutorial: https://docs.python.org/3/tutorial/

### WebTigerPython

- WebTigerPython: https://webtigerpython.ethz.ch

### NumPy

- NumPy: https://numpy.org
- NumPy User Guide: https://numpy.org/doc/stable/user/

### Matplotlib

- Matplotlib: https://matplotlib.org
- Matplotlib Tutorials: https://matplotlib.org/stable/tutorials/
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/
- Matplotlib Cheat Sheets: https://matplotlib.org/cheatsheets/

### SymPy

- SymPy: https://www.sympy.org
- SymPy Documentation: https://docs.sympy.org/latest/

## License

MIT License
