""" Dynamic programming algorithms. """

from data_structures import lists


def reverse_arr(arr: list[int], i: int = 0):
    """ Reverses arr inplace with recursion. """

    right: int = len(arr) - 1 - i
    if i >= right:
        return
    reverse_arr(arr, i + 1)
    arr[i], arr[right] = arr[right], arr[i]


def pascals_triangle(depth: int) -> list[list[int]]:
    """ Constructs Pascal's triangle with non-negative depth recursively. """

    if depth < 0:
        return list()

    def get_val(i, j, cache: dict[tuple, int]) -> int:
        """ Calculates (i, j)-th value of the Pascal's triangle recursively
            with cache optimization. """

        if i == j or not j:
            return 1

        key = (i, j)
        if key not in cache.keys():
            cache[key] = (get_val(i - 1, j - 1, cache) +
                          get_val(i - 1, j, cache))
        return cache[key]

    triangle = []
    cache = dict()
    for i in range(depth + 1):
        triangle.append([get_val(i, j, cache) for j in range(i + 1)])

    return triangle


def fibonacci(depth: int) -> list[int]:
    """ Creates the Fibonacci sequence of the given depth recursively. """

    if depth < 0:
        return list()

    def get_val(i: int, cache: dict[int, int]) -> int:
        """ Gets i-th Fibonacci value. """

        if i < 2:
            return 1
        if i not in cache.keys():
            cache[i] = get_val(i - 1, cache) + get_val(i - 2, cache)

        return cache[i]

    cache = dict()
    return [get_val(i, cache) for i in range(depth)]


def power(x: int, n: int) -> float:
    """ Raises x to the power of n recursively. """

    if not n:
        return 1
    if n < 0:
        # the topmost branch takes 1/x, creates recursive calls below
        return 1 / power(x, -n)
    if not n % 2:
        # square x, reduce n by half. Tail recursion optimization.
        return power(x * x, n // 2)
    return x * power(x, n - 1)


def merge_sorted(list1: lists.ListNode,
                 list2: lists.ListNode) -> lists.ListNode:
    """ Merges two sorted linked lists recursively.
        This method destroys input lists. """

    if not list1 or not list2:
        return list1 or list2

    if list1.val < list2.val:
        list1.next = merge_sorted(list1.next, list2)
        return list1

    list2.next = merge_sorted(list1, list2.next)
    return list2


def is_valid_bst(root, low=float('-inf'), high=float('+inf')) -> bool:
    """ Validates binary search tree recursively in O(n), O(n). """

    if not root:
        return True

    if root.val <= low or root.val >= high:
        return False

    return is_valid_bst(root.left, low, root.val) and is_valid_bst(
        root.right, root.val, high)
