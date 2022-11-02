""" Tests for sorting algorithms. """

import pytest
from algorithms import sorting as srt


@pytest.mark.parametrize(argnames=['arr', 'expected'],
                         argvalues=[
                             ([], []),
                             ([1], [1]),
                             ([5, 4, 3, 1, 2], [1, 2, 3, 4, 5]),
                         ])
def test_selection_sort(arr: list[int], expected: list[int]):
    srt.selection_sort(arr)
    assert arr == expected


@pytest.mark.parametrize(argnames=['arr', 'expected'],
                         argvalues=[
                             ([], []),
                             ([1], [1]),
                             ([5, 4, 3, 1, 2], [1, 2, 3, 4, 5]),
                         ])
def test_bubble_sort(arr: list[int], expected: list[int]):
    srt.bubble_sort(arr)
    assert arr == expected
