""" Implementations of a queue. """

from typing import Optional

from data_structures import lists


class CircularQueue:
    """ A circular queue as a linked list with a fixed size.

    Attributes:
        front (int, None): Front element in the queue, if not exists.
        rear (int, None): Last item from the queue, if not exists.
        size (int): Number of elements in the queue.
        capacity (int): Number of elements the queue can hold.

    Methods:
        bool enqueue(val): Inserts an element into the queue.
        bool dequeue(): Deletes a front element from the queue.
        bool is_empty(): Checks whether the queue is empty.
        bool is_full(): Checks whether the queue is full.
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
        """ Inserts an element into the queue.
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
        """ Deletes a front element from the queue.
            Returns true if the operation is successful, or false otherwise. """

        if self.is_empty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def is_empty(self) -> bool:
        """ Checks whether the queue is empty. """

        return not self.size

    def is_full(self) -> bool:
        """ Checks whether the queue is full. """

        return self.size == self.capacity


class CircularDeque(CircularQueue):
    """ A circular double-ended queue as a linked list with a fixed size.

    Attributes:
        front (int, None): Front item from the queue, if not empty.
        rear (int, None): Last item from the queue, if not empty.
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


class StackQueue:
    """ Implementation of a queue with stacks. Amortized push, pop operations
        in O(1), if used in sequence, O(N) otherwise.

    Attributes:
        size (int): Number of elements in the queue.
        front (int, None): Front element in the queue, if exists.

    Methods:
        null push(val): Inserts an element into the queue.
        bool pop(): Deletes a front element from the queue.
        int peek(): Gets the first element in queue, if exists.
        bool is_empty(): Checks whether the queue is empty.
    """

    def __init__(self) -> None:
        self.pop_stack: list[int] = list()
        self.push_stack: list[int] = list()
        self.front: Optional[int] = None
        self.size: int = 0

    def push(self, val) -> None:
        """ Inserts an element into the queue. """

        if self.pop_stack:
            # reverse order transfer
            while self.pop_stack:
                self.push_stack.append(self.pop_stack.pop())

        self.push_stack.append(val)
        self.size += 1

    def pop(self) -> bool:
        """ Deletes a front element from the queue. """

        if self.is_empty():
            return False

        if self.push_stack:
            # reverse order transfer
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

        self.pop_stack.pop()
        self.size -= 1
        return True

    def peek(self) -> Optional[int]:
        """ Gets the first element in queue, if exists. """

        if self.is_empty():
            return None

        return self.push_stack[0] if self.push_stack else self.pop_stack[-1]

    def is_empty(self) -> bool:
        """ Checks whether the queue is empty. """

        return not self.pop_stack and not self.push_stack
