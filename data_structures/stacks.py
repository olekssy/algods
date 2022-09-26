""" Implementations of a stack. """

from typing import Optional

from data_structures import linked_lists


class Node(linked_lists.Node):

    def __init__(self, val: int = 0, next=None, min=0) -> None:
        super().__init__(val, next)
        self.min = min


class Stack(linked_lists.LinkedList):
    """ A stack data structure as a linked list. Supports LIFO ordering and all
        methods in O(N).

    Attributes:
        head (ListNode, None): a top node of the stack.
        size (int): number of elements in the stack.

    Methods:
        push(item): adds an item to the top of the stack.
        pop(): removes the top item from the stack, if exists.
        peek(): returns the top of the stack.
        is_empty(): returns true if and only if the stack is empty.
        min(): retrieves the minimum element in the stack.
        * other methods inherited from the parent class.
    """

    def __init__(self) -> None:
        super().__init__()

    def push(self, item: int) -> None:
        """ Adds an item to the top of the stack. """

        _min = min(self.head.min, item) if self.head else item
        self.head = Node(val=item, next=self.head, min=_min)
        self.size += 1

    def pop(self) -> None:
        """ Removes the top item from the stack, if exists. """

        if self.head:
            self.head = self.head.next
            self.size -= 1

    def peek(self) -> Optional[int]:
        """ Returns the top of the stack. """

        return self.head.val if self.head else None

    def is_empty(self) -> bool:
        """ Returns true if and only if the stack is empty. """

        return not bool(self.size)

    def min(self) -> Optional[int]:
        """ Retrieves the minimum element in the stack. """

        return self.head.min if self.head else None
