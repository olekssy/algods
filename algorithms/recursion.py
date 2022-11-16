""" Applied recursion algorithms. """


def reverse_arr(arr: int, i: int = 0):
    """ Reverses arr inplace with recursion. """

    right = len(arr) - 1 - i
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
