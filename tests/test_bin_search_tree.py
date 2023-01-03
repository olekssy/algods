""" Unit tests for binary search tree ops. """

import pytest
from data_structures.trees import BST


@pytest.fixture
def bst() -> BST:
    return BST([4, 2, 1, 3, 6, 5])


def test_inorder_list(bst: BST):
    assert bst.to_list() == [1, 2, 3, 4, 5, 6]


def test_push(bst: BST):
    bst.push(10)
    bst.push(11)
    bst.push(12)
    assert bst.to_list() == [1, 2, 3, 4, 5, 6, 10, 11, 12]


def test_remove(bst: BST):
    bst.remove(4)
    bst.remove(1)
    assert bst.to_list() == [2, 3, 5, 6]


def test_search(bst: BST):
    found = bst.search(2)
    assert found.val == 2
    assert found.count == 3


def test_kth_largest_element(bst: BST):
    assert bst.kth_largest(2) == 5
    assert bst.kth_largest(4) == 3
    assert bst.kth_largest(1) == 6
