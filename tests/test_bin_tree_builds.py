""" Unit tests for binary tree traversal algorithms. """

import pytest
from algorithms import binary_trees as bt
from data_structures.trees import BinTreeNode


@pytest.fixture
def preorder() -> list[int]:
    return [4, 2, 1, 3, 6, 5]


@pytest.fixture
def inorder() -> list[int]:
    return [1, 2, 3, 4, 5, 6]


@pytest.fixture
def postorder() -> list[int]:
    return [1, 3, 2, 5, 6, 4]


def test_from_inorder_postorder(preorder, inorder, postorder):
    """ Tests building a bnary tree from the inorder, postorder val lists. """

    tree: BinTreeNode = bt.from_inorder_postorder(inorder, postorder)
    assert preorder == bt.pre_order(tree)
    assert inorder == bt.in_order(tree)
    assert postorder == bt.post_order(tree)
