""" Unit tests for a stack. """

import pytest
from data_structures.stacks import Stack


@pytest.fixture
def stack() -> Stack:
    """ Gets a HT instance with 3 elements. """

    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    return st


def test_pop(stack: Stack):
    """ Tests LIFO pop. """

    stack.pop()
    assert stack.head.val == 2
    stack.pop()
    assert stack.head.val == 1
    stack.pop()
    assert stack.head is None
    stack.pop()


def test_peek(stack: Stack):
    """ Tests LIFO peek. """

    assert stack.peek() == 3
    stack.push(4)
    assert stack.peek() == 4
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.peek() is None


def test_is_empty(stack: Stack):
    """ Tests empty checker. """

    assert not stack.is_empty()
    stack.pop()
    stack.pop()
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()
