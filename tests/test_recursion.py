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


@pytest.mark.parametrize(argnames=['depth', 'expected'],
                         argvalues=[
                             (-3, []),
                             (0, [[1]]),
                             (1, [[1], [1, 1]]),
                             (2, [[1], [1, 1], [1, 2, 1]]),
                             (3, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
                             (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                                  [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]),
                         ])
def test_pascals_triangle(depth: int, expected: list[list[int]]):
    assert recursion.pascals_triangle(depth) == expected


@pytest.mark.parametrize(argnames=['depth', 'expected'],
                         argvalues=[
                             (-3, []),
                             (0, []),
                             (1, [1]),
                             (2, [1, 1]),
                             (3, [1, 1, 2]),
                             (5, [1, 1, 2, 3, 5]),
                             (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
                         ])
def test_fibonacci(depth: int, expected: list[list[int]]):
    assert recursion.fibonacci(depth) == expected


@pytest.mark.parametrize(argnames=['x', 'n', 'expected'],
                         argvalues=[
                             (2, 0, 1),
                             (2, 1, 2),
                             (2, 10, 1024),
                             (2, -10, 0.0009765625),
                         ])
def test_power(x: int, n: int, expected: float):
    assert recursion.power(x, n) == expected
