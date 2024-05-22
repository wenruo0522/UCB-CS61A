def repeat(k):
    """When called repeatedly, print each repeated argument.

    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    >>> f = repeat(1)(7)(1)
    1
    """
    return detector(lambda j: False)(k)


def detector(have_seen):
    def g(i):
        if have_seen(i):
            print(i)
        return detector(lambda j: j == i or have_seen(j))

    return g

# Most important
# have_seen0(j) = lambda j: False
# have_seen1(j) = lambda j: j == 1 or have_seen0(j)
# have_seen2(j) = lambda j: j == 7 or have_seen1(j)
# ...
