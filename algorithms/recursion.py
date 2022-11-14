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

        if i < 0 or j < 0:
            return
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
