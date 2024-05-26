LAB_SOURCE_FILE = __file__

HW_SOURCE_FILE = __file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        if n == 8:
            return 1
        else:
            return 0
    elif n % 10 == 8:
        return 1 + num_eights(n // 10)
    else:
        return num_eights(n // 10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        rest_but_last, last = n // 10, n % 10
        if rest_but_last < 10:
            return abs(rest_but_last - last) + digit_distance(rest_but_last)
        else:
            return abs(rest_but_last % 10 - last) + digit_distance(rest_but_last)


def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"

    def calculate_from(i, total=0, start_flag=-1):
        if start_flag == 1:
            total += even_func(i)
        elif start_flag == -1:
            total += odd_func(i)
        if i < n:
            return calculate_from(i + 1, total, start_flag * (-1))
        elif i == n:
            return total

    return calculate_from(1)


def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    def find_smaller_coin(change_coin):
        if change_coin == 1:
            return 1
        smaller_coin = next_smaller_coin(change_coin)
        if smaller_coin is None:
            return find_smaller_coin(change_coin - 1)
        else:
            return change_coin

    def count(total_coin, partition_coin):
        if total_coin == 0:
            return 1
        elif total_coin < 0:
            return 0
        elif partition_coin == 1:
            return 1
        else:
            small_coin = find_smaller_coin(partition_coin)
            return count(total_coin - small_coin, small_coin) + count(total_coin, find_smaller_coin(small_coin - 1))

    return count(total, find_smaller_coin(total))


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
    else:
        spare = 6 - start - end
        move_stack(n - 1, start, spare)
        print_move(start, end)
        move_stack(n-1, spare, end)


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))


#  Exam Practice
def collapse(n):
    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.

    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(1120000001333)
    12013
    """

    left, last = n // 10, n % 10
    if left == 0:
        return last
    elif left % 10 == last:
        return collapse(left)
    else:
        return collapse(left) * 10 + last


def find_pair(p):
    """Given a two-argument function P, return a function that takes a
    non-negative integer and returns True if and only if two adjacent digits
    in that integer satisfy P (that is, cause P to return a true value).
    >>> z = find_pair(lambda a, b: a == b)  # Adjacent equal digits
    >>> z(1313)
    False
    >>> z(12334)
    True
    >>> z = find_pair(lambda a, b: a > b)
    >>> z(1234)
    False
    >>> find_pair(lambda a, b: a <= b)(9753)
    False
    >>> find_pair(lambda a, b: a == b)(1)  # Only one digit: no pairs.
    False
    """

    def find(n):
        while n // 10 > 0:
            if p(n // 10 % 10, n % 10):
                return True
            else:
                n = n // 10
        return False

    return find


def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n % 10, n // 10
    if rest == 0:
        return last + last * 10
    return repeat_digits(rest) * 100 + repeat_digits(last)


def pal(n):
    """Return a palindrome starting with n.

    >>> pal(12430)
    1243003421
    """
    m = n
    while m:
        n, m = n * 10 + m % 10, m // 10
    return n


def contains(a, b):
    """Return whether the digits of a are contained in the digits of b.

    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """

    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)


def biggest_palindrome(n):
    """Return the largest even-length palindrome in n.

    >>> biggest_palindrome(3425534)
    4554
    >>> biggest_palindrome(126130450234125)
    21300312
    """
    return big(n, 0)


def big(n, k):
    """A helper function for biggest_palindrome."""
    if n == 0:
        return 0

    choices = [big(n // 10, k), big(n // 10, 10 * k + n % 10)]
    if contains(k, n):
        choices.append(pal(k))
    return max(choices)
