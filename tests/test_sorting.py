""" Tests for sorting algorithms. """

import pytest
from algorithms import array_sorting


@pytest.mark.parametrize(argnames=['arr', 'expected'],
                         argvalues=[
                             ([], []),
                             ([1], [1]),
                             ([5, 4, 3, 1, 2], [1, 2, 3, 4, 5]),
                         ])
def test_selection_sort(arr: list[int], expected: list[int]):
    array_sorting.selection_sort(arr)
    assert arr == expected


@pytest.mark.parametrize(argnames=['arr', 'expected'],
                         argvalues=[
                             ([], []),
                             ([1], [1]),
                             ([5, 4, 3, 1, 2], [1, 2, 3, 4, 5]),
                         ])
def test_bubble_sort(arr: list[int], expected: list[int]):
    array_sorting.bubble_sort(arr)
    assert arr == expected


@pytest.mark.parametrize(argnames=['arr', 'expected'],
                         argvalues=[
                             ([], []),
                             ([1], [1]),
                             ([5, 4, 3, 1, 2], [1, 2, 3, 4, 5]),
                         ])
def test_inserion_sort(arr: list[int], expected: list[int]):
    array_sorting.insertion_sort(arr)
    assert arr == expected
