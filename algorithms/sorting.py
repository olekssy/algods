""" Array sorting algorithms. """


def selection_sort(arr: list[int]) -> None:
    """ Sorts array values in ascending order. O(n^2), O(1). """

    for i in range(len(arr)):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k

        arr[i], arr[min_index] = arr[min_index], arr[i]
