""" Applied recursion algorithms. """


def reverse_arr(arr: int, i: int = 0):
    """ Reverses arr inplace with recursion. """

    right = len(arr) - 1 - i
    if i >= right:
        return
    reverse_arr(arr, i + 1)
    arr[i], arr[right] = arr[right], arr[i]
