""" Unit tests for a linked list. """

import pytest
from data_structures.linked_list import LinkedList


@pytest.fixture
def list_0():
    """ Gets an empty LL instance. """

    return LinkedList()


@pytest.fixture
def list_1(list_0: LinkedList) -> LinkedList:
    """ Gets a LL instance with 1 element. """

    list_0.add(key=None, val=1)
    return list_0


@pytest.fixture
def list_2(list_0: LinkedList) -> LinkedList:
    """ Gets a LL instance with 2 elements. """

    list_0.add(key=None, val=1)
    list_0.add(key=None, val=2)
    return list_0


@pytest.fixture
def list_3(list_0: LinkedList) -> LinkedList:
    """ Gets a LL instance with 3 elements. """

    list_0.add(key=None, val=1)
    list_0.add(key=None, val=2)
    list_0.add(key=None, val=3)
    return list_0


@pytest.fixture
def list_4(list_0: LinkedList) -> LinkedList:
    """ Gets a LL instance with 4 elements. """

    list_0.add(key=None, val=1)
    list_0.add(key=None, val=2)
    list_0.add(key=None, val=2)
    list_0.add(key=None, val=4)
    return list_0


@pytest.fixture
def odd_palindrom(list_0: LinkedList) -> LinkedList:
    """ Gets a LL palindom instance with odd num elements. """

    list_0.add(key=None, val=1)
    list_0.add(key=None, val=2)
    list_0.add(key=None, val=1)
    return list_0


@pytest.fixture
def even_palindrom(list_0: LinkedList) -> LinkedList:
    """ Gets a LL palindom instance with even num elements. """

    list_0.add(key=None, val=1)
    list_0.add(key=None, val=2)
    list_0.add(key=None, val=2)
    list_0.add(key=None, val=1)
    return list_0


@pytest.fixture
def two_palindrom(list_0: LinkedList) -> LinkedList:
    """ Gets a LL palindom instance with 2 elements. """

    list_0.add(key=None, val=2)
    list_0.add(key=None, val=2)
    return list_0


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
