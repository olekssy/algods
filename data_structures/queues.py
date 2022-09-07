""" Implementations of a queue. """

from typing import Optional

from data_structures import linked_lists


class CircularQueue:
    """ A queue data structure as a linked list with a fixed size k.
        Supports FIFO ordering.

    Attributes:
        front (int, None): Gets the front item from the queue, if not empty.
        rear (int, None): Gets the last item from the queue, if not empty.
        size (int): Number of elements present in the queue.
        capacity (int): Number of elements the queue can hold.

    Methods:
        bool enqueue(val): Inserts an element into the circular queue.
            Returns true if the operation is successful.
        bool dequeue(): Deletes a front element from the circular queue.
            Returns true if the operation is successful.
        bool is_empty(): Checks whether the circular queue is empty or not.
        bool is_full(): Checks whether the circular queue is full or not.
    """

    def __init__(self, capacity: int = 5) -> None:
        self.capacity = capacity
        self.size: int = 0
        self.head: Optional[linked_lists.Node] = None
        self.tail: Optional[linked_lists.Node] = None

    @property
    def front(self) -> Optional[int]:
        """ Gets the front item from the queue, if not empty. """

        return self.head.val if not self.is_empty() else None

    @property
    def rear(self) -> Optional[int]:
        """ Gets the last item from the queue, if not empty. """

        return self.tail.val if not self.is_empty() else None

    def enqueue(self, val: int) -> bool:
        """ Inserts an element into the circular queue.
            Returns true if the operation is successful. """

        if self.is_full():
            return False
        if self.is_empty():
            self.head = linked_lists.Node(val)
            self.tail = self.head
        else:
            self.tail.next = linked_lists.Node(val)
            self.tail = self.tail.next
        self.size += 1
        return True

    def dequeue(self) -> bool:
        """ Deletes a front element from the circular queue.
            Returns true if the operation is successful. """

        if self.is_empty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def is_empty(self) -> bool:
        """ Checks whether the circular queue is empty or not. """

        return not self.size

    def is_full(self) -> bool:
        """ Checks whether the circular queue is full or not. """

        return self.size == self.capacity
