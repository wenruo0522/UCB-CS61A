# Discussion 3: Recursion

### Q1: Swipe

Implement `swipe`, which prints the digits of argument `n`, one per line, first backward then forward. The left-most digit is printed only once. Do not use `while` or `for` or `str`. (Use recursion, of course!)

```python
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        all_but_last, last = n // 10, n % 10
        print(last)
        swipe(all_but_last)
        print(last)
```

### Q2: Skip Factorial

Define the base case for the `skip_factorial` function, which returns the product of every other positive integer, starting with `n`.

```python
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1 or n == 2:
        return n
    else:
        return n * skip_factorial(n - 2)
```

### Q3: Is Prime

Implement `is_prime` that takes an integer `n` greater than 1. It returns `True` if `n` is a prime number and `False` otherwise. Try following the approach below, but implement it recursively without using a `while` (or `for`) statement.

```python
def is_prime(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True
```

You will need to define another "helper" function (a function that exists just to help implement this one). Does it matter whether you define it within `is_prime` or as a separate function in the global frame? Try to define it to take as few arguments as possible.

```python
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    assert n > 1
    if n == 2:
        return True

    def helper(i):
        if n % i == 0:
            return False
        elif i == n - 1:
            return True
        else:
            return helper(i + 1)

    return helper(2)
```

### Q4: Recursive Hailstone

Recall the `hailstone` function from [Homework 1](https://cs61a.org/hw/hw01/). First, pick a positive integer `n` as the start. If `n` is even, divide it by 2. If `n` is odd, multiply it by 3 and add 1. Repeat this process until `n` is 1. Complete this recursive version of `hailstone` that prints out the values of the sequence and returns the number of steps.

```python
def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """

    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)


def even(n):
    return 1 + hailstone(n // 2)


def odd(n):
    """*** YOUR CODE HERE ***"""
    if n == 1:
        return 1
    else:
        return 1 + hailstone(3 * n + 1)
```

# Extra Challenge

You'll need your whole discussion group for this question. At least try it out. You might have fun. We'll review the question in lecture on Friday.

### Q5: Sevens

**The Game of Sevens**: Players in a circle count up from 1 in the clockwise direction. (The starting player says 1, the player to their left says 2, etc.) If a number is divisible by 7 or contains a 7 (or both), switch directions. Numbers must be said on the beat at [60 beats per minute](https://www.youtube.com/watch?v=ymJIXzvDvj4). If someone says a number when it's not their turn or someone misses the beat on their turn, the game ends.

For example, 5 people would count to 20 like this:

```python
Player 1 says 1
Player 2 says 2
Player 3 says 3
Player 4 says 4
Player 5 says 5
Player 1 says 6  # All the way around the circle
Player 2 says 7  # Switch to counterclockwise
Player 1 says 8
Player 5 says 9  # Back around the circle counterclockwise
Player 4 says 10
Player 3 says 11
Player 2 says 12
Player 1 says 13
Player 5 says 14 # Switch back to clockwise
Player 1 says 15
Player 2 says 16
Player 3 says 17 # Switch back to counterclockwise
Player 2 says 18
Player 1 says 19
Player 5 says 20
```

Play a few games. Post the highest score your group reached on Discord.

Then, implement `sevens` which takes a positive integer `n` and a number of players `k`. It returns which of the `k` players says `n`. You may call `has_seven`.

An effective approach to this problem is to simulate the game, stopping on turn `n`. The implementation must keep track of the final number `n`, the current number `i`, the player `who` will say `i`, and the current `direction` that determines the next player (either increasing or decreasing). It works well to use integers to represent all of these, with `direction` switching between `1` (increase) and `-1` (decreasing).

```python
def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """

    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"

        is_seven_number = i % 7 == 0 or has_seven(i)
        if is_seven_number:
            direction = -1 * direction
        if direction == 1:
            who = who % k + 1
        else:
            if who == 1:
                who = k
            else:
                who = who - 1
        return f(i + 1, who, direction)

    return f(1, 1, 1)


def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
```

### Q6: Karel the Robot

[Karel the robot](https://compedu.stanford.edu/karel-reader/docs/python/en/chapter1.html) starts in the corner of an `n` by `n` square for some unknown number `n`. Karel responds to only four functions:

- `move()` moves Karel one square forward if there is no wall in front of Karel and errors if there is.
- `turn_left()` turns Karel 90 degrees to the left.
- `front_is_blocked()` returns whether there is a wall in front of Karel.
- `front_is_clear()` returns whether there is no wall in front of Karel.

Implement a `main()` function that will leave Karel stopped halfway in the middle of the bottom row. For example, if the square is 7 x 7 and Karel starts in position (1, 1), the bottom left, then Karel should end in position (1, 4) (three steps from either side on the bottom row). Karel can be facing in any direction at the end. If the bottom row length is even, Karel can stop in either position (1, `n // 2`) or (1, `n // 2 + 1`).

**Important** You can only write `if` or `if`/`else` statements and function calls in the body of `main()`. You may not write assignment statements, def statements, lambda expressions, or while/for statements.
