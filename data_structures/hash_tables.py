""" Implementations of a hash table. """

from typing import Optional

from data_structures import lists


class KVNode(lists.ListNode):
    """ Singly linked list node holding key-value attributes. """

    def __init__(self,
                 key: any = None,
                 val: Optional[int] = None,
                 next=None) -> None:
        super().__init__(val, next)
        self.key = key  # an immutable hashable object, e.g. str, int.


class KVList(lists.List):
    """ Singly linked list adapted for a key-value storage.

    Attributes:
        head (Node, None): a head node of the linked list.
        size (int): number of nodes in the linked list.

    Methods:
        add(key, val): inserts a node holding a key-val pair.
        get(index): gets key-val of the node at the index, if valid.
        find(val): finds index of the node matching key, if exists.
        to_list(): gets all key-value pairs as a list.
        * methods inherited from the parent class.
    """

    def __init__(self) -> None:
        super().__init__()

    def add(self, key: any, val: int) -> None:
        """ Inserts a node holding a key-val pair. """

        self.head = KVNode(key, val, next=self.head)
        self.size += 1

    def find(self, key: any) -> Optional[int]:
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

        vals = list()
        head = self.head
        while head:
            vals.append((head.key, head.val))
            head = head.next
        return vals

    def get(self, index: int) -> Optional[tuple]:
        """ Gets key-val of the node at the index, if valid. """

        if index < 0 or index > self.size - 1 or not self.size:
            # index is out of range or list is empty
            return

        else:
            head = self.head
            while head.next and index > 0:
                head = head.next
                index -= 1
            return head.key, head.val


class HashTable:
    """ A hash table implementation as an array of singly linked lists.

    Attributes:
        keys (set): set of keys in the hash table.
        values (list): list of all values in the hash table.
        items (set[tuple]): set of key-val pairs.

    Methods:
        put(key, val): adds new record into the hash table.
        remove(key): removes record matching key, if exists.
        get(key): gets value matching the key, if exists.
    """

    def __init__(self, size: int = 10) -> None:
        if size < 1 or not isinstance(size, int):
            raise ValueError('Array size must be a positive integer.')
        self.size = size
        # instantiate N separate KVLL objects within a list
        self.lists: list[KVList] = [KVList() for i in range(self.size)]

    @property
    def items(self) -> set[tuple]:
        """ Set of key-val pairs. """

        pairs = set()
        for head in self.lists:
            pairs |= set(head.to_list())
        return pairs

    def _get_item(self, key: bool) -> list:
        """ Gets all keys or values from the hash table. """

        items = list()  # collection of keys or values
        for head in self.lists:
            i = 0
            while i < head.size:
                # a key is at 0th index in the key-val tuple
                items.append(head.get(i)[not key])
                i += 1
        return items

    @property
    def keys(self) -> set:
        """ Set of keys in the hash table. """

        return set(self._get_item(key=True))

    @property
    def values(self) -> list:
        """ List of all values in the hash table. """

        return self._get_item(key=False)

    def put(self, key, val) -> None:
        """ Adds new record into the hash table. """

        head = self.lists[hash(key) % self.size]
        if key in self.keys:
            # replace existing recodrd by removing and adding a new one
            self.remove(key)
        head.add(key, val)

    def remove(self, key) -> bool:
        """ Removes record matching key, if exists.
            Returns True if success, False otherwise. """

        head = self.lists[hash(key) % self.size]
        if head.find(key) is not None:
            head.remove(head.find(key))
            return True
        return False

    def get(self, key) -> Optional[any]:
        """ Gets value matching the key, if exists. """

        head = self.lists[hash(key) % self.size]
        key_id = head.find(key)
        if key_id is not None:
            # a value is at the 1st index in the key-val tuple
            return head.get(key_id)[1]


if __name__ == '__main__':
    pass
