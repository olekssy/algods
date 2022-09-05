""" Unit tests for a hash table. """

import pytest

from data_structures.hash_table import HashTable


@pytest.fixture
def ht_3() -> HashTable:
    """ Gets a HT instance with 3 elements. """

    ht = HashTable()
    ht.put(1, 11)
    ht.put(2, 22)
    ht.put(3, 33)
    return ht


def test_keys(ht_3: HashTable):
    """ Tests keys attribute. """

    assert ht_3.keys == {1, 2, 3}


def test_values(ht_3: HashTable):
    """ Tests values attribute. """

    assert ht_3.values == [11, 22, 33]


def test_items(ht_3: HashTable):
    """ Tests items attribute. """

    assert ht_3.items == {(1, 11), (2, 22), (3, 33)}


def test_clear(ht_3: HashTable):
    """ Tests resetting a ht. """

    ht_3.clear()
    assert not ht_3.items


def test_put(ht_3: HashTable):
    """ Tests adding a key-val to the ht. """

    ht_3.put(4, 44)
    assert (4, 44) in ht_3.items
    ht_3.put(4, 555)
    assert (4, 44) not in ht_3.items
    assert (4, 555) in ht_3.items


def test_remove(ht_3: HashTable):
    """ Tests removing an element. """

    ht_3.remove(2)
    assert (2, 22) not in ht_3.items
    ht_3.remove(0)
    assert ht_3.keys == {1, 3}


def test_getter(ht_3: HashTable):
    """ Tests value getter. """

    assert ht_3.get(3) == 33
    assert ht_3.get(5) is None
