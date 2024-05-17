from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    assert n >= 0, "must be a positive integer"
    count = 1
    total = 1
    while count <= n:
        total *= term(count)
        count += 1
    return total


def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    "*** YOUR CODE HERE ***"
    count = 1
    total = 0
    while count <= n:
        if count == 1:
            total = term(count)
        else:
            total = fuse(total, term(count))
        count += 1

    return fuse(start, total)


def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)


def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    "*** YOUR CODE HERE ***"

    def repeater(x):
        assert n >= 1, "at least implement function once"
        count = 1
        while count <= n:
            x = f(x)
            count += 1
        return x

    return repeater


# --- Exam Practice ---

def parabola(x):
    """A parabola function (for testing the again_function)."""
    return (x - 3) * (x - 6)


def vee(x):
    """A V-shaped function (for testing the again_function)."""
    return abs(x - 2)


def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.

    >>> again(parabola) # parabola(4) == parabola(5)
    5
    >>> again(vee) # vee(1) == vee(3)
    3
    """

    n = 1  # line 1
    while True:  # line 2
        m = 0  # line 3
        while n > m:  # line 4
            if f(n) == f(m):  # line 5
                return n  # line 6
            m = m + 1  # line 7
        n = n + 1  # line 8


def restrict_domain(f, low_d, high_d):
    """Return a function that restricts the domain of F,
    a function that takes a single argument x.
    If x is not between LOW_D and HIGH_D (inclusive),
    it returns -Infinity, but otherwise returns F(x)

    >>> from math import sqrt
    >>> f = restrict_domain(sqrt, 1, 100)
    >>> f(25)
    5.0
    >>> f(-25)
    -inf
    >>> f(125)
    -inf
    >>> f(1)
    1.0
    """

    def wrapper_method_name(x):  # a
        if low_d <= x <= high_d:  # b
            return f(x)  # c
        return float('-inf')  # d

    return wrapper_method_name


def restrict_range(f, low_r, high_r):
    """Returns a function that restricts the range of F, a function
    that takes a single argument X. If the return value of F(X)
    is not between LOW_R and HIGH_R (inclusive), it returns -Infinity,
    but otherwise returns F(X)

    >>> cube = lambda x: x * x * x
    >>> f = restrict_range(cube, 1, 1000)
    >>> f(1)
    1
    >>> f(-5)
    -inf
    >>> f(5)
    125
    >>> f(10)
    1000
    >>> f(11)
    -inf
    """

    def wrapper_method_name(x):  # a
        r = f(x)  # b
        if low_r <= r <= high_r:  # c
            return r  # d
        return float("-inf")  # e

    return wrapper_method_name


def restrict_both(f, low_d, high_d, low_r, high_r):
    """
    Returns a version of F with a domain restricted to (LOW_D, HIGH_D)
    and a range restricted to (LOW_R, HIGH_R).

    >>> diva = lambda x: (10000 // x) * 9
    >>> f = restrict_both(diva, 1, 1000, 100, 999)
    >>> f(0)
    -inf
    >>> f(10000)
    -inf
    >>> f(200)
    450
    >>> f(100)
    900
    >>> f(1000)
    -inf
    """

    def wrapper_method_name(x):
        domain_value = restrict_domain(f, low_d, high_d)(x)
        if domain_value != float("-inf"):
            return restrict_range(f, low_r, high_r)(x)
        return float("-inf")

    return wrapper_method_name


def tik(tok):
    """Returns a function that takes gram and prints tok and gram on a line

    >>> tik(5)(6)
    5 6
    >>> tik(tik(5)(print(6)))(print(7))
    6
    5 None
    7
    None None
    """

    def insta(gram):
        print(str(tok) + " " + str(gram))

    return insta
