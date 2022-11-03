""" Array sorting algorithms. """


def selection_sort(arr: list[int]) -> None:
    """ Sorts array inplace. Unstable sort. O(n^2), O(1). """

    for i in range(len(arr)):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k

        arr[i], arr[min_index] = arr[min_index], arr[i]


def bubble_sort(arr: list[int]) -> None:
    """ Sorts array inplace. Stable sort. O(n^2), O(1). """

    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                _sorted = False


def insertion_sort(arr: list[int]) -> None:
    """ Sorts array inplace. Stable sort. O(n^2), O(1).
        Preferred for almost sorted or small arrays. """

    for i in range(1, len(arr)):
        curr_id = i

        while curr_id > 0 and arr[curr_id - 1] > arr[curr_id]:
            arr[curr_id], arr[curr_id - 1] = arr[curr_id - 1], arr[curr_id]
            curr_id -= 1
