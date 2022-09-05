""" Implementation of a stack data structure. """

from data_structures.linked_list import LinkedList
from data_structures.linked_list import Node
from typing import Optional


class Stack(LinkedList):
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

        new_head = Node(val=item, next=self.head)
        self.head = new_head
        self.size += 1

    def pop(self) -> None:
        """ Removes the top item from the stack, if exists. """

        if self.head:
            self.head = self.head.next
            self.size -= 1

    def peek(self) -> Optional[int]:
        """ Returns the top of the stack. """

        return self.head.val

    def is_empty(self) -> bool:
        """ Returns true if and only if the stack is empty. """

        return bool(self.size)
