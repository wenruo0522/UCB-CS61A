# Discussion 1: Control Environment Diagrams

### **Q1: Race**

```python
def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes
# race(2, 3) -> 15
```

- 当乌龟第一次超过兔子的时间**不是整数分钟**时，返回值不正确，比如在 `race(2,3)` 中，乌龟在 `7.5min ` 后超过兔子，但是存在一个更大的整数分钟，两种动物在此之后跑完完全相同的距离。

- 如果乌龟和兔子跑完相同距离的次数不是整数，例如，在 `race(4,5)` 中，乌龟在 `6.2min` 后超过兔子，而兔子从未赶上，那么赛跑函数将永远运行下去。

### **Q2: Fizzbuzz**

```python
def fizzbuzz(n):

    count = 1
    while count <= n:

        if count % 3 == 0 and count % 5 == 0:
            print("fizzbuzz")
        elif count % 3 == 0 and count % 5 != 0:
            print("fizz")
        elif count % 3 != 0 and count % 5 == 0:
            print("buzz")
        else:
            print(count)

        count += 1


fizzbuzz(16)
```

### **Q3: Is Prime?**

```python
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not prime number!!
    False
    """
    "*** YOUR CODE HERE ***"

    count = 1
    is_prime = False
    while count < n:
        if n % count == 0:
            is_prime = True
            return is_prime
        count += 1

    return is_prime


print(is_prime(10))
```

### **Q4: Unique Digits**

```python
def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    digits_set = set()
    while n > 0:
        res = n // 10
        digit = n % 10
        n = res
        if digit not in digits_set:
            digits_set.add(digit)

    return len(digits_set)


print(unique_digits(101))


def has_digit(n, k):
    """Return whether k is a digit in n
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """

    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    has_digit = False
    while n > 0:
        res = n // 10
        digit = n % 10
        n = res
        if digit == k:
            has_digit = True
            return has_digit

    return has_digit

print(has_digit(12, 7))
```

