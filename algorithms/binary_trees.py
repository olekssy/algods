""" Implementations of binary tree algorithms. """

from data_structures import trees


def pre_order(root: trees.BinTreeNode) -> list[int]:
    """ Preorder traversal of the binary tree. """

    vals = list()

    def traverse(root):
        if root:
            vals.append(root.val)
            traverse(root.left)
            traverse(root.right)

    traverse(root)
    return vals


def in_order(root: trees.BinTreeNode) -> list[int]:
    """ Inorder traversal of the binary tree. """

    vals = list()

    def traverse(root):
        if root:
            traverse(root.left)
            vals.append(root.val)
            traverse(root.right)

    traverse(root)
    return vals


def post_order(root: trees.BinTreeNode) -> list[int]:
    """ Postorder traversal of the binary tree. """

    vals = list()

    def traverse(root):
        if root:
            traverse(root.left)
            traverse(root.right)
            vals.append(root.val)

    traverse(root)
    return vals


def from_inorder_postorder(inorder: list[int],
                           postorder: list[int]) -> trees.BinTreeNode:
    """ Builds a binary tree from the lists of inorder, postorder vals. """

    inorder_map: dict = {v: i for i, v in enumerate(inorder)}
    idx = 1

    def build(left: int, right: int):
        if left > right:
            return
        nonlocal idx
        root = trees.BinTreeNode(postorder[-idx])
        idx += 1
        root_id = inorder_map[root.val]
        root.right = build(root_id + 1, right)
        root.left = build(left, root_id - 1)
        return root

    return build(0, len(inorder) - 1)


def from_preorder_inorder(inorder: list[int],
                          preorder: list[int]) -> trees.BinTreeNode:
    """ Builds a binary tree from the lists of inorder, preorder vals. """

    inorder_map: dict = {v: i for i, v in enumerate(inorder)}
    idx = 0

    def build(left: int, right: int):
        if left > right:
            return
        nonlocal idx
        root = trees.BinTreeNode(preorder[idx])
        idx += 1
        root_id = inorder_map[root.val]
        root.left = build(left, root_id - 1)
        root.right = build(root_id + 1, right)
        return root

    return build(0, len(inorder) - 1)
