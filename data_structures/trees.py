""" Definitions of the tree data structures. """


class BinTreeNode:
    """ Binary tree node with left and right subtrees. """

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
