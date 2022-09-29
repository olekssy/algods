""" Implementations of binary tree algorithms. """

from data_structures import trees


def pre_order(root: trees.BinTreeNode, vals: list[int] = list()) -> list[int]:
    """ Preorder traversal of the binary tree. """

    if root:
        vals.append(root.val)
        pre_order(root.left, vals)
        pre_order(root.right, vals)
    return vals


def in_order(root: trees.BinTreeNode, vals: list[int] = list()) -> list[int]:
    """ Preorder traversal of the binary tree. """

    if root:
        in_order(root.left, vals)
        vals.append(root.val)
        in_order(root.right, vals)
    return vals


def post_order(root: trees.BinTreeNode, vals: list[int] = list()) -> list[int]:
    """ Preorder traversal of the binary tree. """

    if root:
        post_order(root.left, vals)
        post_order(root.right, vals)
        vals.append(root.val)
    return vals
