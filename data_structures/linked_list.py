""" Implementation of a linked list with common methods. """

from typing import Optional


class ListNode:
    """ Singly linked list node. """

    def __init__(self, key: any = None, val: any = None, _next=None) -> None:
        self.key = key
        self.val = val
        self.next = _next


class LinkedList:
    """ Singly linked list.

    Attributes:
        head (ListNode): a head node of the linked list.
        size (int): number of nodes in the linked list.

    Methods:
        clear(): resets list to the initial (empty) state.
        add(key, val, index): inserts a key-value node at the index, if valid.
        remove(index): removes node at the index, if valid.
        get(index): gets key-value of the node at the index, if valid.
        find(key): finds index of the node matching key, if exists.
        to_list(): gets all key-value pairs as a list.
        rotate(k): rotate list by k places.
        reverse(): reverses linked list inplace.
    """

    def __init__(self) -> None:
        self.head: Optional[ListNode] = self.clear()
        self.size: int = 0

    def clear(self) -> None:
        """ Resets list to the initial (empty) state. """

        self.head = None
        self.size = 0

    def add(self, key, val=None, index: int = 0) -> None:
        """ Inserts a key-val node at the index, if valid. """

        if index > self.size or index < 0:
            # index is out of range
            return
        elif not index:
            # list is empty
            new_node = ListNode(key, val, _next=self.head)
            self.head = new_node
            self.size += 1
        else:
            # traverse list until found an insertion point
            new_node = ListNode(key, val)
            head = self.head
            while index > 1 and head.next:
                head = head.next
                index -= 1
            new_node.next = head.next
            head.next = new_node
            self.size += 1

    def remove(self, index: int) -> None:
        """ Removes node at the index, if valid. """

        if index < 0 or index > self.size - 1 or not self.size:
            # index is out of range or list is empty
            return
        elif not index:
            # remove first node
            self.head = self.head.next
            self.size -= 1
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

    def get(self, index: int) -> Optional[tuple]:
        """ Gets key-value of the node at the index, if valid. """

        if index < 0 or index > self.size - 1 or not self.size:
            # index is out of range or list is empty
            return
        else:
            head = self.head
            while head.next and index > 0:
                head = head.next
                index -= 1
            return head.key, head.val

    def find(self, key) -> Optional[int]:
        """ Finds index of the node matching key, if exists. """

        head = self.head
        i = 0
        while head:
            if head.key == key:
                return i
            head = head.next
            i += 1

    def to_list(self) -> list[tuple]:
        """ Gets all key-value pairs as a list. """

        kv_pairs = list()
        head = self.head
        while head:
            kv_pairs.append((head.key, head.val))
            head = head.next
        return kv_pairs

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
        print(k)

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
            next_node = curr.next
            curr.next = self.head
            self.head = curr
            curr = next_node


if __name__ == '__main__':
    pass
