""" Implementations of a queue. """

from typing import Optional

from data_structures.linked_lists import LinkedList


class Queue(LinkedList):
    """ A queue data structure as a linked list. Supports FIFO ordering.

    Attributes:
        head (ListNode, None): a top node of the queue.
        tail (ListNode, None): a tail node of the queue.
        size (int): number of elements in the queue.

    Methods:
        add(item): adds an item to the end of the list.
        remove(): removes the first item in the list.
        peek(): returns the top of the queue.
        is_empty(): returns true if and only if the queue is empty.
    """

    def __init__(self) -> None:
        super().__init__()

    def add(self, item: int) -> None:
        """ Adds an item to the end of the list. """

        raise NotImplementedError

    def remove(self) -> Optional[int]:
        """ Removes the first item in the list. """

        raise NotImplementedError

    def peek(self) -> Optional[int]:
        """ Returns the top of the queue. """

        raise NotImplementedError

    def is_empty(self) -> bool:
        """ Returns true if and only if the queue is empty. """

        raise NotImplementedError
