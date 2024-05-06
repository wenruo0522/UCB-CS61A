# Lab 0: Getting Started <kbd>[lab00.zip](./lab00.zip)</kbd>

*Due by 11:59 pm on Wednesday, January 24.*

## Starter Files

Download [lab00.zip](./lab00.zip). Inside the archive, you will find starter files for the questions in this lab, along with a copy of the `Ok` auto-grader.

**This lab is required for all students and counts toward you lab score,** but try to complete it at home before you come to Lab 1.

## Introduction

This lab explains how to setup your computer to complete assignments and introduces some of the basics of Python. If you need any help at any time through the lab, please feel free to come to [office hours](https://cs61a.org/office-hours), post on Ed, or come to your assigned lab section.

Here's an outline of the lab:

- **Setup**: Setting up the essential software for the course. This will require several components, listed below.
  - **Install a Terminal**: Install a terminal so you can interact with files in this course and run OK commands. If you have a terminal on your computer and feel comfortable using it, you can skip this part.
  - **Install Python 3**: Install the Python programming language to your computer. If you already have Python 3.7 or later (ideally Python 3.9) installed, you can skip this part.
  - **Install a Text Editor**: Install software to edit `.py` files for this course (e.g. VSCode, Atom, etc.). You can skip this part if you already have a text editor you like.
- **Walk-through: Using the Terminal**: This walks you through how to use the terminal and Python interpreter. If you already feel comfortable with both of these you do not need to read this section.
- **Walk-through: Organizing your Files**: This section walks you through how to use your terminal to organize and navigate files for this course. **Everyone should at least skim this section**, as it has important information specific to this class, but if you are already comfortable navigating directory structures with a terminal much of this will feel familiar.
- **Required: Doing the Assignment**: You must complete this section to get points for the assignment. Here you will practice the different types of problems you will be asked to do in lab, homework, and project assignments for this course. The main goal of this assignment is to give you practice using our software.
- **Required: Submitting the Assignment**: You must complete this section to get points for the assignment. This will walk you through how to turn in your work after completing the previous section and how to verify that your work is turned in on Grade-scope.
- **Appendix: Useful Python Command Line Options**: These are commands that are useful in debugging your work, but not required to complete the lab. We include them because we imagine they're likely to be helpful to you throughout the course.

## Setup

> To setup your device, select the guide that corresponds to your operating system.

- **[Guide for Windows](https://cs61a.org/articles/setup-windows/)**

- **[Guide for Mac & Linux](https://cs61a.org/articles/setup-mac)**

## Your First Assignment

> When working on assignments, ensure that your terminal's working directory is correct (which is likely where you unzipped the assignment).

### 1) What Would Python Do? (WWPD)

One component of lab assignments is to predict how the Python interpreter will behave.

>Enter the following in your terminal to begin this section:
>
>```
>python3 ok -q python-basics -u
>```
>
>You will be prompted to enter the output of various statements/expressions. You must enter them correctly to move on, but there is no penalty for incorrect answers.
>
>The first time you run Ok, you will be prompted for your bCourses email. Please follow [these directions](../Articles/using-ok.md). We use this information to associate your code with you when grading.

```
>>> x = 20
>>> x + 2
______

>>> x
______

>>> y = 5
>>> y = y + 3
>>> y * 2
______

>>> y + x
______
```

### 2) Implementing Functions

Labs will often ask you to implement functions. Open `lab00.py` in your text editor. You should see a function called `twenty_twenty_four` that has a blank `return` statement. That blank is the only part you should change. Replace it with an expression that evaluates to 2024. What's the most creative expression you can come up with?

> Don't forget to save your assignment after you edit it! Even better, turn on Auto Save (in the file menu of VS Code).

### 3) Running Tests

In CS 61A, we will use a program called `ok` to test our code. `ok` will be included in every assignment in this class.

Back to the terminal—make sure you are in the `lab00` directory we created earlier (remember, the `cd` command lets you [change directories](https://cs61a.org/lab/lab00/#changing-directories)).

In that directory, you can type `ls` to verify that there are the following four files:

- `lab00.py`: the starter file you just edited
- `ok`: our testing program
- `lab00.ok`: a configuration file for Ok

Now, let's test our code to make sure it works. You can run `ok` with this command:

```
python3 ok
```

> Remember, if you are using Windows and the `python3` command doesn't work, try using just `python` or `py`. See the the [install Python 3](https://cs61a.org/lab/lab00/#install-python-3) section for more info and ask for help if you get stuck!

If you wrote your code correctly and you finished unlocking your tests, you should see a successful test:

```
=====================================================================
Assignment: Lab 0
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    2 test cases passed! No cases failed.
```

If you didn't pass the tests, `ok` will instead show you something like this:

```
---------------------------------------------------------------------
Doctests for twenty_twenty_four

>>> from lab00 import *
>>> twenty_twenty_four()
0

# Error: expected
#     2024
# but got
#     0

---------------------------------------------------------------------
Test summary
    0 test cases passed before encountering first failed test case
```

Fix your code in your text editor until the test passes.

> Every time you run Ok, Ok will try to back up your work. Don't worry if it says that the "Connection timed out." We won't use your backups for grading.
>
> While `ok` is the primary assignment "autograder" in CS 61A, you may find it useful at times to write some of your own tests in the form of [doctests](https://cs61a.org/lab/lab00/#understanding-problems). Then, you can try them out using the `-m doctest` [option for Python](#appendix-useful-python-command-line-options)).

## Appendix: Useful Python Command Line Options

Here are the most common ways to run Python on a file.

1. Using no command-line options will run the code in the file you provide and return you to the command line. If your file just contains function definitions, you'll see no output unless there is a syntax error.

   ```
   python3 lab00.py
   ```

2. **`-i`**: The `-i` option runs the code in the file you provide, then opens an interactive session (with a `>>>` prompt). You can then evaluate expressions, for example calling functions you defined. To exit, type `exit()`. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac machines or `Ctrl-Z Enter` on Windows.

   If you edit the Python file while running it interactively, you will need to exit and restart the interpreter in order for those changes to take effect.

   Here's how we can run `lab00.py` interactively:

   ```
   python3 -i lab00.py
   ```

3. **`-m doctest`**: Runs the doctests in a file, which are the examples in the docstrings of functions.

   Each test in the file consists of `>>>` followed by some Python code and the expected output.

   Here's how we can run the doctests in `lab00.py`:

   ```
    python3 -m doctest lab00.py
   ```

   When our code passes all of the doctests, no output is displayed. Otherwise, information about the tests that failed will be displayed.