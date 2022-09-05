""" Unit tests for a linked list. """

import pytest

from data_structures import linked_list
from data_structures.linked_list import LinkedList


@pytest.fixture
def list_0() -> LinkedList:
    """ Gets an empty LL instance. """

    return LinkedList()


@pytest.fixture
def list_1() -> LinkedList:
    """ Gets a LL instance with 1 element. """

    ll = LinkedList()
    ll.add(1)
    return ll


@pytest.fixture
def list_2() -> LinkedList:
    """ Gets a LL instance with 2 elements. """

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    return ll


@pytest.fixture
def list_3() -> LinkedList:
    """ Gets a LL instance with 3 elements. """

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    return ll


@pytest.fixture
def list_4() -> LinkedList:
    """ Gets a LL instance with 4 elements. """

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    return ll


@pytest.fixture
def odd_palindrom() -> LinkedList:
    """ Gets a LL palindom instance with odd num elements. """

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(1)
    return ll


@pytest.fixture
def even_palindrom() -> LinkedList:
    """ Gets a LL palindom instance with even num elements. """

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(2)
    ll.add(1)
    return ll


@pytest.fixture
def two_palindrom() -> LinkedList:
    """ Gets a LL palindom instance with 2 elements. """

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(2)
    ll.add(1)
    return ll


@pytest.mark.parametrize(argnames=['ll', 'expected'],
                         argvalues=[
                             ('two_palindrom', True),
                             ('odd_palindrom', True),
                             ('even_palindrom', True),
                             ('list_0', False),
                             ('list_1', True),
                             ('list_3', False),
                             ('list_4', False),
                         ])
def test_is_palindrome(ll: str, expected: bool, request):
    """ Tests correctness of the LL palindrom checker method. """

    assert request.getfixturevalue(ll).is_palindrom() == expected


@pytest.mark.parametrize(
    argnames='ll',
    argvalues=['list_0', 'list_1', 'list_2', 'list_3', 'list_4'])
def test_reverse(ll: str, request):
    ll = request.getfixturevalue(ll)
    ll.reverse()
    if ll.head:
        assert ll.head.val == 1


@pytest.mark.parametrize(argnames=['l1', 'l2', 'expected'],
                         argvalues=[
                             ('list_0', 'list_0', []),
                             ('list_0', 'list_1', [1]),
                             ('list_1', 'list_2', [1, 1, 2]),
                             ('list_2', 'list_3', [1, 1, 2, 2, 3]),
                             ('list_3', 'list_4', [1, 1, 2, 2, 3, 3, 4]),
                         ])
def test_merge_sorted(l1: str, l2: str, expected: list[int], request):
    """ Tests correctness of the LL palindrom checker method. """

    list1: LinkedList = request.getfixturevalue(l1)
    list1.reverse()
    list2: LinkedList = request.getfixturevalue(l2)
    list2.reverse()
    merged = linked_list.merge_sorted(list1, list2)
    assert merged.to_list() == expected
