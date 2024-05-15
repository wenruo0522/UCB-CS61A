def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"

    result = n
    if k == 0:
        result = 1
    else:
        while k > 1:
            k -= 1
            n -= 1
            result *= n
    return result


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count = 0
    if n >= k:
        for index in range(1, n + 1):
            if index % k == 0:
                print(index)
                count += 1

    return count


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    digit_sum = 0
    digits = len(str(y))
    while digits > 0:
        digit = y // pow(10, digits - 1)
        res = y % pow(10, digits - 1)
        y = res
        digit_sum += digit
        digits -= 1
    return digit_sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    >>> double_eights(80880000)
    True
    """
    "*** YOUR CODE HERE ***"
    digits = len(str(n))
    first_digit = 0
    second_digit = 0
    is_double_eight = False
    while digits > 0:
        digit = n // pow(10, digits - 1)
        if digit == 8:
            if first_digit == 0:
                first_digit = digits
            elif second_digit == 0:
                second_digit = digits
                if abs(first_digit - second_digit) == 1:
                    is_double_eight = True
                    break
            else:
                # first_digit = digits
                # second_digit = 0
                if abs(second_digit - digits) == 1:
                    is_double_eight = True
                    break
                else:
                    first_digit = digits
                    second_digit = 0

        res = n % pow(10, digits - 1)
        n = res
        digits -= 1
    return is_double_eight

