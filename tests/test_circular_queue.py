""" Unit tests for a circular queue. """

from data_structures.queues import CircularQueue


def test_enqueue():
    q = CircularQueue(3)
    assert q.is_empty()
    assert not q.is_full()
    assert q.enqueue(11)
    assert q.enqueue(22)
    assert not q.is_empty()
    assert not q.is_full()
    assert q.enqueue(33)
    assert not q.enqueue(44)
    assert q.size == 3
    assert not q.is_empty()
    assert q.is_full()


def test_front_rear():
    q = CircularQueue(3)
    q.enqueue(11)
    assert q.front == 11
    assert q.rear == 11
    q.enqueue(22)
    assert q.front == 11
    assert q.rear == 22
    q.enqueue(33)
    assert q.front == 11
    assert q.rear == 33
    q.enqueue(44)
    assert q.front == 11
    assert q.rear == 33


def test_dequeue():
    q = CircularQueue(3)
    q.enqueue(11)
    assert q.dequeue()
    q.enqueue(22)
    assert q.dequeue()
    q.enqueue(33)
    assert q.front == 33
    assert q.rear == 33
    assert q.dequeue()
    assert q.is_empty()
    assert not q.dequeue()
    q.enqueue(44)
    assert q.front == 44
    assert q.rear == 44
