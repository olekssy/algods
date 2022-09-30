""" Unit tests for a stack queue. """

from data_structures.queues import StackQueue


def test_push():
    q = StackQueue()
    assert q.is_empty()
    q.push(11)
    q.push(22)
    assert not q.is_empty()
    q.push(33)
    assert q.size == 3
    assert not q.is_empty()


def test_peek():
    q = StackQueue()
    q.push(11)
    assert q.peek() == 11
    q.push(22)
    assert q.peek() == 11
    q.pop()
    q.push(33)
    assert q.peek() == 22
    q.pop()
    assert q.peek() == 33


def test_pop():
    q = StackQueue()
    q.push(11)
    assert q.pop()
    q.push(22)
    assert q.pop()
    q.push(33)
    assert q.peek() == 33
    assert q.pop()
    assert q.is_empty()
    assert not q.pop()
    q.push(44)
    assert q.peek() == 44
