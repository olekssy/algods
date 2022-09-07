""" Unit tests for a linked list. """

import pytest
from data_structures import linked_lists
from data_structures.linked_lists import LinkedList


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
                         ])
def test_is_palindrome(ll: str, expected: bool, request):
    """ Tests correctness of the LL palindrom checker method. """

    assert linked_lists.is_palindrom(request.getfixturevalue(ll)) == expected


@pytest.mark.parametrize(argnames='ll',
                         argvalues=['list_0', 'list_1', 'list_2', 'list_3'])
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
                         ])
def test_merge_sorted(l1: str, l2: str, expected: list[int], request):
    """ Tests correctness of the LL palindrom checker method. """

    list1: LinkedList = request.getfixturevalue(l1)
    list1.reverse()
    list2: LinkedList = request.getfixturevalue(l2)
    list2.reverse()
    merged = linked_lists.merge_sorted(list1, list2)
    assert merged.to_list() == expected


@pytest.mark.parametrize(argnames=['i', 'expected'],
                         argvalues=[
                             (0, [99, 3, 2, 1]),
                             (1, [3, 99, 2, 1]),
                             (3, [3, 2, 1, 99]),
                             (4, [3, 2, 1]),
                         ])
def test_add(list_3: LinkedList, i: int, expected: list[int]):
    """ Tests adding elements at different indices. """

    list_3.add(99, index=i)
    assert list_3.to_list() == expected


@pytest.mark.parametrize(argnames=['i', 'expected'],
                         argvalues=[
                             (0, [2, 1]),
                             (1, [3, 1]),
                             (2, [3, 2]),
                             (4, [3, 2, 1]),
                             (-1, [3, 2, 1]),
                         ])
def test_remove(list_3: LinkedList, i: int, expected: list[int]):
    """ Tests removing a node at index. """

    list_3.remove(i)
    assert list_3.to_list() == expected


@pytest.mark.parametrize(argnames=['i', 'expected'],
                         argvalues=[
                             (0, 3),
                             (1, 2),
                             (2, 1),
                             (4, None),
                             (-1, None),
                         ])
def test_get(list_3: LinkedList, i: int, expected: int):
    """ Tests value getter given index. """

    assert list_3.get(i) == expected


@pytest.mark.parametrize(argnames=['val', 'expected'],
                         argvalues=[
                             (0, None),
                             (1, 2),
                             (2, 1),
                             (3, 0),
                             (-1, None),
                         ])
def test_find(list_3: LinkedList, val: int, expected: int):
    """ Tests index finder. """

    assert list_3.find(val) == expected


def test_size(list_3: LinkedList):
    """ Tests list size counter. """

    assert list_3.size == 3
    list_3.remove(0)
    list_3.remove(0)
    assert list_3.size == 1
    list_3.add(11)
    list_3.add(12)
    list_3.remove(0)
    list_3.add(12)
    list_3.remove(0)
    list_3.add(12)
    assert list_3.size == 3
    list_3.remove(0)
    list_3.remove(0)
    list_3.remove(0)
    list_3.remove(0)
    assert list_3.size == 0
