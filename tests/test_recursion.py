""" Tests for recursive algorithms. """

import pytest
from algorithms import recursion


@pytest.mark.parametrize(argnames=['arr', 'expected'],
                         argvalues=[
                             ([], []),
                             ([1], [1]),
                             ([1, 2], [2, 1]),
                             ([5, 4, 3, 1, 2], [2, 1, 3, 4, 5]),
                         ])
def test_reverse_arr(arr: list[int], expected: list[int]):
    recursion.reverse_arr(arr)
    assert arr == expected
