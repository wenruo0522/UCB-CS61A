def trace(f):
    def g(n, m):
        print(f.__name__, "(", str(n), ",", str(m), ") was called")
        result = f(n, m)
        print(f.__name__, "(", str(n), ",", str(m), ") -> ", str(result))
        return result

    return g


@trace
def count_partitions(n, m):
    """
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    """

    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, min(m, n - m))
        without_m = count_partitions(n, m - 1)
        return with_m + without_m


count_partitions(2, 4)
