""" Unit tests for binary tree traversal algorithms. """

import pytest
from algorithms import binary_trees as bt
from data_structures.trees import BinTreeNode


@pytest.fixture
def tree() -> BinTreeNode:
    root = BinTreeNode(4)
    # first layer
    root.left = BinTreeNode(2)
    root.right = BinTreeNode(6)
    # second layer
    root.left.left = BinTreeNode(1)
    root.left.right = BinTreeNode(3)
    root.right.left = BinTreeNode(5)
    return root


def test_pre_order(tree: BinTreeNode):
    """ Tests pre-order traversal. """

    assert bt.pre_order(tree) == [4, 2, 1, 3, 6, 5]


def test_in_order(tree: BinTreeNode):
    """ Tests in-order traversal. """

    assert bt.in_order(tree) == [1, 2, 3, 4, 5, 6]


def test_post_order(tree: BinTreeNode):
    """ Tests post-order traversal. """

    assert bt.post_order(tree) == [1, 3, 2, 5, 6, 4]
