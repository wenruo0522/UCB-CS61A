def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branch must be a tree"
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])

print("tree:", t)
print("label(t):", label(t))
print("branches(t):", branches(t))
print("label(branches(t)[1]):", label(branches(t)[1]))
print("is_leaf(t):", is_leaf(t))
print("is_leaf(branches(t)[0]):", is_leaf(branches(t)[0]))


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


print("fib_tree(5):", fib_tree(5))


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(branch) for branch in branches(tree)]
        return sum(branch_counts)


print("count_leaves(fib_tree(5)):", count_leaves(fib_tree(5)))


def partition_tree(n, m):
    if n == 0:
        return tree(True)
    if n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


print("partition_tree(6, 4):", partition_tree(6, 4))


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


print_parts(partition_tree(6, 4))


# def right_binarize(tree):
#     if is_leaf(tree):
#         return tree
#     if len(tree) > 2:
#         tree = [tree[0], tree[1:]]
#     return [right_binarize(branch) for branch in tree]
#
#
# print(right_binarize([1, 2, 3, 4, 5, 6, 7]))


def count_paths(t, total):
    """
    Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total.
    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """

    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])
