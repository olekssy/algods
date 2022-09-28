""" Implementations of a queue. """

from typing import Optional

from data_structures import lists


class CircularQueue:
    """ A circular queue as a linked list with a fixed size.

    Attributes:
        front (int, None): Gets the front item from the queue, if not empty.
        rear (int, None): Gets the last item from the queue, if not empty.
        size (int): Number of elements present in the queue.
        capacity (int): Number of elements the queue can hold.

    Methods:
        bool enqueue(val): Inserts an element into the circular queue.
        bool dequeue(): Deletes a front element from the circular queue.
        bool is_empty(): Checks whether the circular queue is empty or not.
        bool is_full(): Checks whether the circular queue is full or not.
    """

    def __init__(self, capacity: int = 5) -> None:
        self.capacity = capacity
        self.size: int = 0
        self.head: Optional[lists.ListNode] = None
        self.tail: Optional[lists.ListNode] = None

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
            Returns true if the operation is successful, or false otherwise. """

        if self.is_full():
            return False
        if self.is_empty():
            self.head = lists.ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = lists.ListNode(val)
            self.tail = self.tail.next
        self.size += 1
        return True

    def dequeue(self) -> bool:
        """ Deletes a front element from the circular queue.
            Returns true if the operation is successful, or false otherwise. """

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


class CircularDeque(CircularQueue):
    """ A circular double-ended queue as a linked list with a fixed size.

    Attributes:
        front (int, None): Gets the front item from the queue, if not empty.
        rear (int, None): Gets the last item from the queue, if not empty.
        size (int): Number of elements present in the queue.
        capacity (int): Number of elements the queue can hold.

    Methods:
        bool enqueue_front(): Adds an item at the front of Deque.
        bool enqueue_last() Adds an item at the rear of Deque.
        bool dequeue_front() Deletes an item from the front of Deque.
        bool dequeue_last() Deletes an item from the rear of Deque.
        bool is_empty(): Checks whether the circular queue is empty or not.
        bool is_full(): Checks whether the circular queue is full or not.
    """

    def __init__(self, capacity: int = 5) -> None:
        super().__init__(capacity)
        self.head: Optional[lists.DoublyNode] = None
        self.tail: Optional[lists.DoublyNode] = None

    def enqueue_front(self, value: int) -> bool:
        """ Adds an item at the front of Deque.
            Returns true if the operation is successful, false otherwise. """

        if self.is_full():
            return False
        elif self.is_empty():
            # front and rear point to the same node
            self.head = lists.DoublyNode(value)
            self.tail = self.head
        else:
            # link existing nodes
            head = lists.DoublyNode(value, next=self.head)
            self.head.prev = head
            self.head = self.head.prev
        self.size += 1
        return True

    def enqueue_last(self, value: int) -> bool:
        """ Adds an item at the rear of Deque.
            Returns true if the operation is successful, false otherwise. """

        if self.is_full():
            return False
        elif self.is_empty():
            # front and rear point to the same node
            self.tail = lists.DoublyNode(value)
            self.head = self.tail
        else:
            # link existing nodes
            tail = lists.DoublyNode(value, prev=self.rear)
            self.tail.next = tail
            self.tail = self.tail.next
        self.size += 1
        return True

    def dequeue_front(self) -> bool:
        """ Deletes an item from the front of Deque.
            Returns true if the operation is successful, or false otherwise. """

        if self.is_empty():
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return True

    def dequeue_last(self) -> bool:
        """ Deletes an item from the rear of Deque.
            Returns true if the operation is successful, or false otherwise. """

        if self.is_empty():
            return False
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1
        return True
