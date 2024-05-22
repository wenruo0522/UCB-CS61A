def inverse_cascade(n):
    """
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


def grow(n):
    return f_then_g(grow, print, n // 10)


def shrink(n):
    return f_then_g(print, shrink, n // 10)
