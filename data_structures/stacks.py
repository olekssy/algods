""" Implementations of a stack. """

from typing import Optional

from data_structures import linked_lists


class Stack(linked_lists.LinkedList):
    """ A stack data structure as a linked list. Supports LIFO ordering.

    Attributes:
        head (ListNode, None): a top node of the stack.
        size (int): number of elements in the stack.

    Methods:
        push(item): adds an item to the top of the stack.
        pop(): removes the top item from the stack, if exists.
        peek(): returns the top of the stack.
        is_empty(): returns true if and only if the stack is empty.
        * other methods inherited from the parent class.
    """

    def __init__(self) -> None:
        super().__init__()

    def push(self, item: int) -> None:
        """ Adds an item to the top of the stack. """

        self.head = linked_lists.Node(val=item, next=self.head)
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
