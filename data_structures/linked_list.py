""" Implementation of the linked list alike data structurers. """

from typing import Optional


class Node:
    """ Singly linked list node. """

    def __init__(self, val: Optional[int] = None, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    """ Singly linked list.

    Attributes:
        head (Node, None): a head node of the linked list.
        size (int): number of nodes in the linked list.

    Methods:
        clear(): resets list to the initial (empty) state.
        add(val, index): inserts a value node at the index, if valid.
        remove(index): removes node at the index, if valid.
        get(index): gets value of the node at the index, if valid.
        find(val): finds index of the node matching value, if exists.
        to_list(): gets all values as an array.
        rotate(k): rotate list by k places.
        reverse(): reverses linked list inplace.
        is_palindrom(): checks if linked list values form a palidrom.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = self.clear()
        self.size: int

    def clear(self) -> None:
        """ Resets list to the initial (empty) state. """

        self.head = None

    @property
    def size(self) -> int:
        """ Number of nodes in the list. """

        n: int = 0
        head = self.head
        while head:
            head = head.next
            n += 1
        return n

    def add(self, val: int, index: int = 0) -> None:
        """ Inserts a value node at the index, if valid. """

        if index > self.size or index < 0:
            # index is out of range
            return

        elif not index:
            # list is empty
            new_node = Node(val, next=self.head)
            self.head = new_node

        else:
            # traverse list until found an insertion point
            new_node = Node(val)
            head = self.head
            while index > 1 and head.next:
                head = head.next
                index -= 1
            new_node.next = head.next
            head.next = new_node

    def remove(self, index: int) -> None:
        """ Removes node at the index, if valid. """

        if index < 0 or index > self.size - 1 or not self.size:
            # index is out of range or list is empty
            return

        elif not index:
            # remove first node
            self.head = self.head.next

        else:
            # link node following one at the index to the previous
            head = self.head
            i = 0
            while head.next and i < index - 1:
                head = head.next
                i += 1
            if head.next:
                head.next = head.next.next
            else:
                head.next = None

    def get(self, index: int) -> Optional[int]:
        """ Gets value of the node at the index, if valid. """

        if index < 0 or index > self.size - 1 or not self.size:
            # index is out of range or list is empty
            return

        else:
            head = self.head
            while head.next and index > 0:
                head = head.next
                index -= 1
            return head.val

    def find(self, val: int) -> Optional[int]:
        """ Finds index of the node matching value, if exists. """

        head = self.head
        i = 0
        while head:
            if head.val == val:
                return i
            head = head.next
            i += 1

    def to_list(self) -> list[int]:
        """ Gets all values as an array. """

        vals = list()
        head = self.head
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def rotate(self, k: int) -> None:
        """ Rotate list by k places. """

        if not k or self.size < 2:
            # no iters on single element
            return

        # get last head
        last = self.head
        while last.next:
            last = last.next

        # remove redundant shifts
        k = self.size - k % self.size

        last.next = self.head  # make cycle
        while k > 0:  # shift last by k* places
            k -= 1
            last = last.next
        self.head = last.next  # reassign head
        last.next = None  # break cycle

    def reverse(self) -> None:
        """ Reverses linked list inplace. """

        curr = self.head
        self.head = None
        while curr:
            tail = curr.next
            curr.next = self.head
            self.head = curr
            curr = tail

    def is_palindrom(self) -> bool:
        """ Checks if linked list values form a palidrom. """

        if not self.head:
            # empty list is not a palindrom
            return False

        if not self.head.next:
            # a list with single element is a palindrom
            return True

        # split list in half with slow-fast pointers
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow

        # reverse the other half
        curr = second
        second = None
        while curr:
            tail = curr.next
            curr.next = second
            second = curr
            curr = tail

        # compare values of the first and second halves
        first = self.head
        while second.next:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True


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


# Linked List OPS
def merge_sorted(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """ Merges two sorted singly linked lists into a one sorted list.
        NOTE: the method yields undefined result if passed unsorted list.
        Runtime: O(N), memory: O(N).

    Args:
        list1 (LinkedList): first LL.
        list2 (LinkedList): second LL.

    Returns:
        LinkedList: a sorted linked list.
    """

    # passed empty list1, list2, or both
    if not list1.size:
        return list2
    elif not list2.size:
        return list1
    elif (not list1.size) and (not list2.size):
        return LinkedList()

    # transfer vals from lists until either one is exhausted
    dummy: Node = Node()
    head = dummy
    h1: Node = list1.head
    h2: Node = list2.head
    while h1 and h2:
        if h1.val < h2.val:
            head.next = Node(h1.val)
            h1 = h1.next
        else:
            head.next = Node(h2.val)
            h2 = h2.next
        head = head.next

    # link tail of the non-empty list
    if h1:
        head.next = h1
    elif h2:
        head.next = h2

    # transform node into LL
    merged = LinkedList()
    merged.head = dummy.next
    return merged


if __name__ == '__main__':
    pass
