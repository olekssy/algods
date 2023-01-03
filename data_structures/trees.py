""" Definitions of the tree data structures. """


class BinTreeNode:
    """ Binary tree node with left and right subtrees. """

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTNode(BinTreeNode):
    """ Binary search tree node with position count in a tree attribute. """

    def __init__(self, val: int = 0, count: int = 1, left=None, right=None):
        super().__init__(val, left, right)
        self.count = count


class BST:
    """ A binary search tree data structure for add, remove, and search
        operations in O(H).

    Methods:
        push(val) -> None: adds element to the BST.
        remove(val) -> None: removes element from the BST.
        search(val) -> BSTNode: gets node mathing value.
        to_list() -> list[int]: gets sorted list of elements.
        kth_largest(k: int) -> int: gets k-th largest element in the BST.
        """

    def __init__(self, nums: list[int] = list()) -> None:
        self.root: BSTNode = None
        for val in nums:
            self.push(val)

    def push(self, val) -> None:
        """ Adds element into the tree. """

        def add(root, val) -> BSTNode:
            if not root:
                return BSTNode(val)
            if root.val < val:
                root.right = add(root.right, val)
            else:
                root.left = add(root.left, val)
            root.count += 1
            return root

        self.root = add(self.root, val)

    def remove(self, val) -> None:
        """ Removes element from the tree. """

        def delete(root, val) -> BSTNode:
            if not root:
                return root

            if root.val == val:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    root.val = self._predecessor(root).val
                    root.right = delete(root.right, root.val)
            elif root.val < val:
                root.right = delete(root.right, val)
            else:
                root.left = delete(root.left, val)
            return root

        self.root = delete(self.root, val)

    def search(self, val) -> BSTNode:
        """ Finds node matching value. """

        def find(root, val) -> BSTNode:
            if not root or root.val == val:
                return root
            if root.val < val:
                return find(root.right, val)
            return find(root.left, val)

        return find(self.root, val)

    def to_list(self) -> list[int]:
        """ Gets sorted list of elements. """

        nums = list()

        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)

        inorder(self.root)
        return nums

    def _predecessor(self, node) -> BSTNode:
        """ Finds predecessor node of the given node. """

        node = node.right
        while node.left:
            node = node.left
        return node

    def kth_largest(self, k: int) -> int:
        """ Gets k-th largest element in the BST. """

        def find(root, k) -> int:
            m = root.right.count if root.right else 0
            if k == m + 1:
                return root.val
            elif k <= m:
                return find(root.right, k)
            else:
                return find(root.left, k - m - 1)

        return find(self.root, k)
