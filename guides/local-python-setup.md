# Local Python Setup

This guide explains how to set up Python locally on your computer in a clean and reproducible way.

The guide is divided into two parts:

- **Part I:** Things you only need to do once.
- **Part II:** The workflow you will repeat for every Python project.

For most users, the recommended setup is:

```text
One Python installation + one virtual environment (venv) per project + VS Code
```

Advanced users who need multiple Python versions can optionally use `pyenv` (see Appendix A).

---

## Part I: One-time setup

You only need to complete this part once on your computer.

### 1. Install Python

#### Recommended approach

Install the current stable version of Python.

##### Windows

Install Python from https://www.python.org.

During installation, enable:

```text
Add Python to PATH
```

##### macOS

Install Python from https://www.python.org.

##### Linux

Use your distribution package manager.

For example, on Debian or Ubuntu:

```bash
sudo apt install python3 python3-venv python3-pip
```

### 2. Install Visual Studio Code

Install Visual Studio Code from https://code.visualstudio.com.

Then install the following extensions:

- [Python](vscode:extension/ms-python.python)
- [Ruff](vscode:extension/charliermarsh.ruff)

VS Code may suggest additional Python-related extensions.
The extensions listed above are sufficient for this guide.

The author of this repository uses VS Code exclusively and therefore only provides detailed instructions for VS Code.

---

## Part II: Setup for each new project

The following steps should be repeated for every new Python project.

### 3. Create a project folder

Create a new folder for your Python project using the file explorer of your operating system.

For example:

    my-python-project

Open this folder in VS Code before continuing.

### 4. Create and activate a virtual environment

A virtual environment keeps the packages of one project separate from all other projects.

This matters because different projects may need different packages or different package versions.

For example:

- one project might need an older version of a package
- another project might need a newer version of the same package

Without a virtual environment, these projects can interfere with each other.

A virtual environment avoids this problem by creating an isolated Python environment for one project.

```text
Computer
    │
    └── Python
            │
            ├── Project A
            │      └── .venv
            │
            └── Project B
                   └── .venv
```

This section contains two steps:

1. Create the virtual environment once.
2. Activate it whenever you work on the project.

The first step is performed once per project.
The second step must be repeated whenever you work on the project.

#### Create the virtual environment

Open a terminal inside VS Code (`Terminal` → `New Terminal`) and run:

```bash
python -m venv .venv
```

This creates a folder called `.venv`. This folder should remain inside the project folder. You do not need to open or modify this folder manually.

#### Activate the virtual environment

##### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, Windows may show an execution policy error.
In that case, use the following command once in PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating the virtual environment again.

##### macOS / Linux

```bash
source .venv/bin/activate
```

After activation, your terminal usually shows something like:

```text
(.venv)
```

### 5. Install packages with pip

`pip` installs Python packages.

Python itself only provides the programming language.
Additional functionality is provided by packages.

For this repository, the most important packages are:

- `numpy` for numerical computations
- `matplotlib` for plots
- `sympy` for symbolic mathematics

Always install packages **only after activating the virtual environment**.

This step is usually performed only once when setting up a project.

```bash
python -m pip install numpy matplotlib sympy
```

### 6. Selecting the Python interpreter in VS Code

VS Code needs to know which Python installation should be used for this project.

If the project contains a `.venv` folder, VS Code will often detect it automatically.

If not, select the interpreter manually:

1. Open the Command Palette.
2. Search for `Python: Select Interpreter`.
3. Select the interpreter inside the `.venv` folder.

**This usually only needs to be done once per project.**

After the interpreter has been selected, VS Code normally remembers this choice when the project is opened again.

You only need to select the interpreter manually if VS Code did not detect the `.venv` automatically.

### 7. Daily workflow

Once a project has been set up, the daily workflow becomes very simple.

1. Open the project folder in VS Code.
2. Open a terminal inside VS Code.
3. Activate the virtual environment.

   macOS / Linux

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks the activation script, see the note in section 4.

4. Open the Python file you want to run.
5. Run the file using the ▶ button in the top right corner of the editor.
6. When you work on the same project again, simply repeat steps 1–5.

If you install additional packages later, first activate the virtual environment and then run:

```bash
python -m pip install <package>
```

---

## For students

For students, the setup should be as simple as possible.

Recommendation order:

1. WebTigerPython
2. Thonny
3. Full local setup (as descibed above) only if necessary

### WebTigerPython

Best for short activities and first experiments:

https://webtigerpython.ethz.ch

Advantages:

- no installation
- no login
- runs in the browser
- simple interface

### Thonny

Recommended if students need a local installation:

https://thonny.org/

Advantages:

- beginner-friendly
- simple interface
- Python included
- fewer configuration problems

### Why not VS Code or PyCharm for beginners?

VS Code and PyCharm are excellent tools, but they introduce many additional concepts:

- interpreters
- terminals
- virtual environments
- extensions
- project folders
- package management

For beginners, these concepts can distract from learning Python itself.

---

## Appendix A: pyenv

The main guide above assumes that you install a single Python version.

If you work on many Python projects and need multiple Python versions, you can use `pyenv`.

It is particularly useful if you:

- work on many Python projects
- need different Python versions for different projects
- want to avoid modifying the system Python installation

Example:

- Project A requires Python 3.10
- Project B requires Python 3.14

The installation of `pyenv` depends on the operating system and package manager being used.

Detailed installation instructions can be found at:

https://github.com/pyenv/pyenv

A typical workflow with `pyenv` is:

```bash
pyenv install 3.14
pyenv local 3.14
python -m venv .venv
```

For beginners, using a single Python installation together with `venv` is usually the better choice.

---

## Appendix B: PyCharm

[PyCharm](https://www.jetbrains.com/de-de/pycharm/) is another popular Python IDE.

Advantages:

- excellent Python support
- integrated virtual environment management
- powerful refactoring tools

Disadvantages:

- more complex than VS Code
- heavier and less flexible

The author of this repository does not use PyCharm and therefore cannot provide detailed recommendations for its configuration.
