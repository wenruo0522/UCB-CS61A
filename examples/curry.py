def print_sum(n):
    print(n)

    def next_sum(k):
        return print_sum(n + k)

    return next_sum


print_sum(1)(3)(5)  # 1 4 9
