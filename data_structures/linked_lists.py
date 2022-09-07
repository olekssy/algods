""" Implementations of a linked list with common ops. """

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
        add(val, index): inserts a value node at the index, if valid.
        remove(index): removes node at the index, if valid.
        get(index): gets value of the node at the index, if valid.
        find(val): finds index of the node matching value, if exists.
        to_list(): gets all values as an array.
        reverse(): reverses linked list inplace.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size: int = 0

    def add(self, val: int, index: int = 0) -> bool:
        """ Inserts a value node at the index, if valid.
            Returns True if success, False otherwise. """

        if index > self.size or index < 0:
            # index is out of range
            return False

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

        self.size += 1
        return True

    def remove(self, index: int) -> bool:
        """ Removes node at the index, if valid.
            Returns True if success, False otherwise. """

        if index < 0 or index > self.size - 1 or not self.size:
            # index is out of range or list is empty
            return False

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

        self.size -= 1
        return True

    def get(self, index: int) -> Optional[int]:
        """ Gets value of the node at the index, if valid. """

        if index < 0 or index > self.size - 1 or not self.size:
            # index is out of range or list is empty
            return

        else:
            head = self.head
            while head.next and index:
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

    def reverse(self) -> None:
        """ Reverses linked list inplace. """

        curr = self.head
        self.head = None
        while curr:
            tail = curr.next
            curr.next = self.head
            self.head = curr
            curr = tail


# Linked List ops
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


def is_palindrom(linked_list: LinkedList) -> bool:
    """ Checks if linked list values form a palidrom. """

    head: Node = linked_list.head

    if not head:
        # empty list is not a palindrom
        return False

    elif not head.next:
        # a list with single element is a palindrom
        return True

    # split list in half with slow-fast pointers
    slow = head
    fast = head
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
    first = head
    while second.next:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True


def rotate(linked_list: LinkedList, k: int) -> None:
    """ Rotate a linked list by k places. """

    if not k or linked_list.size < 2:
        # no iters on single element
        return

    # get last head
    last = linked_list.head
    while last.next:
        last = last.next

    # remove redundant shifts
    k = linked_list.size - k % linked_list.size

    last.next = linked_list.head  # make cycle
    while k:  # shift last by k places
        k -= 1
        last = last.next
    linked_list.head = last.next  # reassign head
    last.next = None  # break cycle


if __name__ == '__main__':
    pass
