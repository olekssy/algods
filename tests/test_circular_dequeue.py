""" Unit tests for a circular dequeue. """

from data_structures.queues import CircularDeque


def test_enqueue():
    q = CircularDeque(3)
    assert q.is_empty()
    assert not q.is_full()
    assert q.enqueue_front(11)
    assert q.enqueue_last(22)
    assert not q.is_empty()
    assert not q.is_full()
    assert q.enqueue_last(33)
    assert not q.enqueue_front(44)
    assert q.size == 3
    assert not q.is_empty()
    assert q.is_full()


def test_front_rear():
    q = CircularDeque(3)
    assert q.enqueue_last(11)
    assert q.front == 11
    assert q.rear == 11
    assert q.enqueue_front(22)
    assert q.front == 22
    assert q.rear == 11
    assert q.enqueue_front(33)
    assert q.front == 33
    assert q.rear == 11
    assert not q.enqueue_last(44)
    assert q.front == 33
    assert q.rear == 11


def test_dequeue():
    q = CircularDeque(3)
    assert q.enqueue_front(11)
    assert q.dequeue_last()
    assert q.enqueue_last(22)
    assert q.dequeue_front()
    assert q.enqueue_last(33)
    assert q.front == 33
    assert q.rear == 33
    assert q.dequeue_last()
    assert q.is_empty()
    assert not q.dequeue_front()
    assert q.enqueue_front(44)
    assert q.front == 44
    assert q.rear == 44
