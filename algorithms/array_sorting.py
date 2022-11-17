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


def merge_sort(arr: list[int]) -> list[int]:
    """ Sorts array with recursive, top-down merge sort algorithm.
        Stable sort in O(n logn), O(n). """

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge_sorted(left, right)


def merge_sort_alt(arr: list[int]) -> list[int]:
    """ Sorts array with recursive, bottom-up merge sort algorithm.
        Stable sort in O(n logn), O(n). """

    if len(arr) < 2:
        return arr

    val_splits = [[n] for n in arr]

    while len(val_splits) > 1:
        ordered = list()
        for i in range(0, len(val_splits), 2):
            # i + 1 can be out of range
            right = val_splits[i + 1] if i + 1 < len(val_splits) else list()
            ordered.append(_merge_sorted(val_splits[i], right))
            i += 2
        val_splits = ordered

    return val_splits[0]


def _merge_sorted(l1: list[int], l2: list[int]) -> list[int]:
    """ Merges two sorted arrays. """

    p1 = p2 = 0
    merged = list()

    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            merged.append(l1[p1])
            p1 += 1
        else:
            merged.append(l2[p2])
            p2 += 1

    merged += l1[p1:] + l2[p2:]
    return merged
