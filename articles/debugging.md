# Debugging

> For a walkthrough of this guide, check out Antonio Kam's [video](https://youtu.be/mNEJkV0HOEc).

## Introduction

When an error occurs in a Python program, a traceback is displayed. For example:

```
Traceback (most recent call last):
  File ".../ex.py", line 7, in <module>
    print(f(4))
          ^^^^
  File ".../ex.py", line 2, in f
    print(g(x + 1) + 2)
          ^^^^^^^^
  File ".../ex.py", line 5, in g
    return print(2) + 3
           ~~~~~~~~~^~~
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

### Traceback Messages

The lines in the traceback are paired together. The **first** line in each pair has the following format:

```
File "<file name>", line <number>, in <function>
```

That line provides you with the following information:

- **File name**: the name of the file that contains the problem.
- **Number**: the line number in the file that caused the problem, or the line number that contains the next function call
- **Function**: the name of the function in which the line can be found.

The **second** line in the pair (it's indented farther in than the first) displays the actual line of code that makes the *next* function call. This gives you a quick look at what expressions were involved.

The traceback is organized with the **most recent call last**, so look at the bottom.

### Error Messages

The very last line in the traceback message is the error statement. An *error statement* has the following format:

```
<error type>: <error message>
```

This line provides you with two pieces of information:

- **Error type**: the type of error that was caused (e.g. `SyntaxError`, `TypeError`). These are usually descriptive enough to help you narrow down your search for the cause of error.
- **Error message**: a more detailed description of exactly what caused the error. Different error types produce different error messages.

## Debugging Techniques

### Running doctests

Python has a great way to quickly write tests for your code. These are called doctests, and look like this:

```
def foo(x):
    """A random function.

    >>> foo(4)
    4
    >>> foo(5)
    5
    """
```

The lines in the docstring that look like interpreter outputs are the **doctests**. To run them, go to your terminal and type:

```
python3 -m doctest file.py
```

This effectively loads your file into the Python interpreter, and checks to see if each doctest input (e.g. `foo(4)`) is the same as the specified output (e.g. `4`). If it isn't, a message will tell you which doctests you failed.

The command line tool has a `-v` option that stands for *verbose*.

```
python3 -m doctest file.py -v
```

In addition to telling you which doctests you failed, it will also tell you which doctests passed.

Usually, we will provide doctests for you in the starter files. You can add more tests by following the same format. It is often helpful to write additional tests to uncover more details about the shape of the inputs and the expected outputs of the problem, in addition to helping with the implementation of the program itself. A little time spent upfront writing tests can save a lot of time down the line.

### Printing

Once the doctests tell you where the error is, you have to figure what went wrong. If the doctest gave you a traceback message, look at what [type of error](#error-types) it is to help narrow your search. Also check that you aren't making any [common mistakes](#common-bugs).

When you first learn how to program, it can be hard to spot bugs in your code. One common practice is to add `print` calls. For example, let's say the following function `foo` keeps returning the wrong thing:

```
def foo(x):
    result = some_function(x)
    return result // 5
```

We can add a print call before the return to check what `some_function` is returning:

```
def foo(x):
    result = some_function(x)
    print('DEBUG: result is', result)
    return other_function(result)
```

> Note: prefixing debug statements with the specific string `"DEBUG: "` allows them to be ignored by the `ok` autograder used by cs61a. Since `ok` generally tests all the output of your code, it will fail if there are debug statements that aren't explicitly marked as such, even if the outputs are identical.

If it turns out `result` is not what we expect it to be, we would go look in `some_function` to see if it works properly. Otherwise, we might have to add a print call before the return to check `other_function`:

```
def foo(x):
    result = some_function(x)
    print('DEBUG: result is', result)
    tmp = other_function(result)
    print('DEBUG: other_function returns', tmp)
    return tmp
```

Some advice:

- Don't just print out a variable -- add some sort of message to make it easier for you to read:

  ```
  print(x)   # harder to interpret
  print('DEBUG: x =', x)  # easier
  ```

- Use `print` calls to view the results of function calls (i.e. after function calls).

- Use `print` calls at the end of a `while` loop to view the state of the counter variables after each iteration:

  ```
  i = 0
  while i < n:
      i += func(i)
      print('DEBUG: i is', i)
  ```

### Interactive Debugging

One way a lot of programmers like to investigate their code is by using Python interactively:

```
python3 -i file.py
```

starts an interactive Python session after executing the contents of `file.py`.

If you are using the `ok` autograder, the `-i` option starts an interactive session in the environment of a failing test case:

```
python3 ok -q ### Q1: name -i
```

You can then evaluate expressions related to the test to see what is going wrong.

### PythonTutor Debugging

Sometimes the best way to understand what is going on with a given piece of python code is to create an environment diagram.[PythonTutor](http://tutor.cs61a.org/) creates environment diagrams automatically.

## Error Types

The following are common error types that Python programmers run into.

### `SyntaxError`

- **Cause**: code syntax mistake

- **Example**:

  ```
    File "file name", line number
      def incorrect(f)
                      ^
  SyntaxError: invalid syntax
  ```

- **Solution**: the `^` symbol points to the code that contains invalid syntax. The error message doesn't tell you *what* is wrong, but it does tell you *where*.

- **Notes**: Python will check for `SyntaxErrors` before executing any code. This is different from other errors, which are only raised during runtime.

### `IndentationError`

- **Cause**: improper indentation

- **Example**:

  ```
    File "file name", line number
      print('improper indentation')
  IndentationError: unindent does not match any outer indentation level
  ```

- **Solution**: The line that is improperly indented is displayed. Simply re-indent it.

- **Notes**: If you are inconsistent with tabs and spaces, Python will raise one of these. Make sure you use spaces! (It's just less of a headache in general in Python to use spaces and all cs61a content uses spaces).

### `TypeError`

- **Cause 1**:

  - Invalid operand types for primitive operators. You are probably trying to add/subract/multiply/divide incompatible types.

  - **Example**:

    ```
    TypeError: unsupported operand type(s) for +: 'function' and 'int'
    ```

- **Cause 2**:

  - Using non-function objects in function calls.

  - **Example**:

    ```
    >>> square = 3
    >>> square(3)
    Traceback (most recent call last):
      ...
    TypeError: 'int' object is not callable
    ```

- **Cause 3**:

  - Passing an incorrect number of arguments to a function.

  - **Example**:

    ```
    >>> add(3)
    Traceback (most recent call last):
      ...
    TypeError: add expected 2 arguments, got 1
    ```

### `NameError`

- **Cause**: variable not assigned to anything OR it doesn't exist. This includes function names.

- **Example**:

  ```
  File "file name", line number
    y = x + 3
  NameError: global name 'x' is not defined
  ```

- **Solution**: Make sure you are initializing the variable (i.e. assigning the variable to a value) before you use it.

- **Notes**: The reason the error message says "global name" is because Python will start searching for the variable from a function's local frame. If the variable is not found there, Python will keep searching the parent frames until it reaches the global frame. If it still can't find the variable, Python raises the error.

### `IndexError`

- **Cause**: trying to index a sequence (e.g. a tuple, list, string) with a number that exceeds the size of the sequence.

- **Example**:

  ```
  File "file name", line number
    x[100]
  IndexError: tuple index out of range
  ```

- **Solution**: Make sure the index is within the bounds of the sequence. If you're using a variable as an index (e.g. `seq[x]`, make sure the variable is assigned to a proper index.

## Common Bugs

### Spelling

Python is *case sensitive*. The variable `hello` is not the same as `Hello` or `hello` or `helo`. This will usually show up as a `NameError`, but sometimes misspelled variables will actually have been defined. In that case, it can be difficult to find errors, and it is never gratifying to discover it's just a spelling mistake.

### Missing Parentheses

A common bug is to leave off the closing parenthesis. This will show up as a `SyntaxError`. Consider the following code:

```
def fun():
    return foo(bar()   # missing a parenthesis here

fun()
```

Python will raise a `SyntaxError`, but will point to the line *after* the missing parenthesis:

```
File "file name", line "number"
    fun()
      ^
SyntaxError: invalid syntax
```

In general, if Python points a `SyntaxError` to a seemingly correct line, you are probably forgetting a parenthesis somewhere.

### Missing close quotes

This is similar to the previous bug, but much easier to catch. Python will actually tell you the line that is missing the quote:

```
File "file name", line "number"
  return 'hi
           ^
SyntaxError: EOL while scanning string literal
```

`EOL` stands for "End of Line."

### `=` vs. `==`

The single equal sign `=` is used for *assignment*; the double equal sign `==` is used for testing equivalence. The most common error of this form is something like:

```
if x = 3:
```

### Infinite Loops

Infinite loops are often caused by `while` loops whose conditions never change. For example:

```
i = 0
while i < 10:
    print(i)
```

Sometimes you might have incremented the wrong counter:

```
i, n = 0, 0
while i < 10:
    print(i)
    n += 1
```

### Off-by-one errors

Sometimes a `while` loop or recursive function might stop one iteration too short. Here, it's best to walk through the iteration/recursion to see what number the loop stops at.