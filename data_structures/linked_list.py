""" Implementation of a linked list with common methods. """

from typing import Optional


class ListNode:
    """ Singly linked list node. """

    def __init__(self, key: any = None, val: any = None) -> None:
        self.key = key
        self.val = val
        self.next = None


class LinkedList:
    """ Singly linked list.

    Attributes:
        head (ListNode): a head node of the linked list.
        size (int): number of nodes in the linked list.

    Methods:
        clear(): resets list to the initial (empty) state.
        add(key, val, index): inserts a key-value node at the index.
        remove(index): removes node at the index, if exists.
        get(index): gets key-value of the node at the index, if node exists.
        find(key): finds index of the node matching key, if exists.
        to_list(): gets all key-value pairs as a list.
        rotate(k): rotate list by k places.
        reverse(): reverses linked list inplace.
    """

    def __init__(self) -> None:
        self.head: Optional[ListNode] = self.clear()

    @property
    def size(self) -> int:
        """ Number of nodes in the linked list. """

        n = 0
        head = self.head
        while head:
            head = head.next
            n += 1
        return n

    def clear(self) -> None:
        """ Resets list to the initial (empty) state. """

        self.head = None

    def add(self, key, val=None, index: int = 0) -> None:
        """ Inserts a key-val node at the index. """

        new_node = ListNode(key, val)
        if self.head is None:
            # list is empty
            self.head = new_node
        elif index < 1:
            # prepend the list
            new_node.next = self.head
            self.head = new_node
        else:
            # traverse list until found an insertion point
            head = self.head
            while index > 1 and head.next:
                head = head.next
                index -= 1
            new_node.next = head.next
            head.next = new_node

    def remove(self, index: int) -> None:
        """ Removes node at the index, if exists. """

        # cap index in the arr size
        index = min(index, self.size - 1)

        if self.size < 1:
            # do nothing if list is empty
            return
        if index < 0 and self.size > 0:
            raise ValueError('Index must be non-negative.')
        elif index < 1:
            # remove first node if matches the index
            self.head = self.head.next
        else:
            # link node following one at the index to the previous one
            head = self.head
            i = 0
            while head.next and i < index - 1:
                head = head.next
                i += 1
            if head.next:
                head.next = head.next.next
            else:
                head.next = None

    def get(self, index: int) -> tuple:
        """ Gets key-value of the node at the index, if node exists. """

        head = self.head
        while head.next and index > 0:
            head = head.next
            index -= 1
        return head.key, head.val

    def find(self, key) -> int:
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

        # do nothing if k = 0, or list.size < 2
        if k == 0 or self.size < 2:
            return

        # get last head
        last = self.head
        while last.next:
            last = last.next

        # remove redundant shifts
        k %= self.size
        k = self.size - k

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
